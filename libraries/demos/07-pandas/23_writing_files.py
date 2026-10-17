from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "data"

servers = pd.read_csv(DATA / "servers.csv")
servers["used_pct"] = (servers["used_gb"] / servers["disk_gb"] * 100).round(1)

report = servers.sort_values("used_pct", ascending=False)[
    ["hostname", "site", "role", "disk_gb", "used_pct"]
]

# index=False leaves out the row numbers, which nobody wants in a CSV that
# already has a hostname column.
csv_path = DATA / "servers-report.csv"
report.to_csv(csv_path, index=False)
print(csv_path.read_text(encoding="utf-8").splitlines()[:4])

report.to_csv(DATA / "servers-report.tsv", sep="\t", index=False)

# ExcelWriter puts several frames into one workbook, one sheet each, which is
# what makes this the format people ask for.
xlsx_path = DATA / "servers-report.xlsx"
per_site = servers.groupby("site", as_index=False).agg(
    servers=("hostname", "count"), total_disk_gb=("disk_gb", "sum")
)
with pd.ExcelWriter(xlsx_path, engine="openpyxl") as workbook:
    report.to_excel(workbook, sheet_name="servers", index=False)
    per_site.to_excel(workbook, sheet_name="per site", index=False)

print(pd.ExcelFile(xlsx_path).sheet_names)
print(pd.read_excel(xlsx_path, sheet_name="per site"))
