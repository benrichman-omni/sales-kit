#!/usr/bin/env python3
"""Summarize the pipeline: totals by stage and forecast category,
deals needing attention, and upcoming close dates.

Reads either the markdown pipeline doc (opps/pipeline.md, "Open" and
"Closed" tables) or a CSV with the same columns.

Usage: python3 pipeline_summary.py path/to/pipeline.md|.csv [--today YYYY-MM-DD] [--json]
"""
import csv
import json
import sys
from collections import defaultdict
from datetime import date, datetime

MEDDPICC = ["meddpicc_m", "meddpicc_e", "meddpicc_d1", "meddpicc_d2",
            "meddpicc_p", "meddpicc_i", "meddpicc_c1", "meddpicc_c2"]


def parse_date(value):
    try:
        return datetime.strptime((value or "").strip(), "%Y-%m-%d").date()
    except ValueError:
        return None


def parse_amount(value):
    try:
        return float(str(value).replace(",", "").replace("$", "").strip() or 0)
    except ValueError:
        return 0.0


def read_markdown_tables(path):
    """Return rows from every markdown table in the file, tagging each with
    the nearest preceding '## ' heading as _section."""
    rows, header, section = [], None, ""
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("## "):
                section, header = line[3:].strip().lower(), None
                continue
            if not line.startswith("|"):
                header = None
                continue
            cells = [c.strip() for c in line.strip("|").split("|")]
            if header is None:
                header = cells
            elif all(set(c) <= set("-: ") for c in cells):
                continue
            else:
                row = dict(zip(header, cells))
                row["_section"] = section
                rows.append(row)
    return rows


def load_rows(path):
    if path.lower().endswith((".md", ".markdown", ".txt")):
        rows = read_markdown_tables(path)
        for r in rows:
            if r.get("_section") == "closed" and not r.get("stage"):
                outcome = (r.get("outcome") or "").lower()
                r["stage"] = "6. Closed Won" if "won" in outcome else "6. Closed Lost"
        return rows
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def score(row, key):
    try:
        return int(row.get(key) or 0)
    except ValueError:
        return 0


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 1
    path = argv[1]
    today = date.today()
    if "--today" in argv:
        today = parse_date(argv[argv.index("--today") + 1]) or today
    as_json = "--json" in argv

    rows = load_rows(path)

    open_rows = [r for r in rows if not (r.get("stage") or "").startswith("6.")]
    by_stage = defaultdict(lambda: {"count": 0, "amount": 0.0})
    by_forecast = defaultdict(lambda: {"count": 0, "amount": 0.0})
    attention = []
    upcoming = []

    for r in open_rows:
        amt = parse_amount(r.get("amount"))
        stage = r.get("stage") or "(none)"
        fc = r.get("forecast_category") or "(none)"
        by_stage[stage]["count"] += 1
        by_stage[stage]["amount"] += amt
        by_forecast[fc]["count"] += 1
        by_forecast[fc]["amount"] += amt

        if (r.get("meddpicc_total") or "").strip():
            total = score(r, "meddpicc_total")
        else:
            total = sum(score(r, k) for k in MEDDPICC)

        reasons = []
        nsd = parse_date(r.get("next_step_date"))
        cd = parse_date(r.get("close_date"))
        lu = parse_date(r.get("last_updated"))
        if not (r.get("next_step") or "").strip():
            reasons.append("no next step")
        if nsd and nsd < today:
            reasons.append(f"next step overdue ({nsd.isoformat()})")
        elif nsd and (nsd - today).days <= 2:
            reasons.append(f"next step due {nsd.isoformat()}")
        if cd and cd < today:
            reasons.append(f"close date passed ({cd.isoformat()})")
        if cd and 0 <= (cd - today).days <= 30:
            upcoming.append({"deal_id": r.get("deal_id"), "account": r.get("account"),
                             "amount": amt, "close_date": cd.isoformat(),
                             "forecast": fc, "meddpicc_total": total})
            if score(r, "meddpicc_p") < 2:
                reasons.append("closing ≤30d with paper process unconfirmed")
        if lu and (today - lu).days >= 14:
            reasons.append(f"no update in {(today - lu).days}d")
        if fc == "Commit":
            if score(r, "meddpicc_e") < 2 or score(r, "meddpicc_c1") < 2:
                reasons.append("Commit without confirmed EB/champion")
        if reasons:
            attention.append({"deal_id": r.get("deal_id"), "account": r.get("account"),
                              "amount": amt, "reasons": reasons})

    attention.sort(key=lambda d: (-len(d["reasons"]), -d["amount"]))
    upcoming.sort(key=lambda d: d["close_date"])

    result = {
        "as_of": today.isoformat(),
        "open_deals": len(open_rows),
        "open_amount": sum(parse_amount(r.get("amount")) for r in open_rows),
        "by_stage": dict(sorted(by_stage.items())),
        "by_forecast": dict(by_forecast),
        "needs_attention": attention,
        "closing_next_30_days": upcoming,
        "closed_won": sum(parse_amount(r.get("amount")) for r in rows
                          if (r.get("stage") or "").startswith("6. Closed Won")),
    }

    if as_json:
        print(json.dumps(result, indent=2))
        return 0

    print(f"Pipeline as of {result['as_of']}: {result['open_deals']} open deals, "
          f"${result['open_amount']:,.0f}")
    print("\nBy stage:")
    for k, v in result["by_stage"].items():
        print(f"  {k:<22} {v['count']:>3}  ${v['amount']:>12,.0f}")
    print("\nBy forecast category:")
    for k, v in result["by_forecast"].items():
        print(f"  {k:<22} {v['count']:>3}  ${v['amount']:>12,.0f}")
    print("\nNeeds attention:")
    for d in attention or [{"account": "(none)", "amount": 0, "reasons": []}]:
        print(f"  {d['account']} (${d['amount']:,.0f}): {'; '.join(d['reasons'])}")
    print("\nClosing in next 30 days:")
    for d in upcoming or [{"account": "(none)", "amount": 0, "close_date": "", "forecast": "", "meddpicc_total": 0}]:
        print(f"  {d['close_date']} {d['account']} ${d['amount']:,.0f} "
              f"[{d['forecast']}] MEDDPICC {d['meddpicc_total']}/24")
    print(f"\nClosed won to date: ${result['closed_won']:,.0f}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
