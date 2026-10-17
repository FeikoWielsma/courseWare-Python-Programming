from bs4 import BeautifulSoup

TABLE = """
<table class="quotes">
  <thead>
    <tr><th>Symbol</th><th>Close</th><th>Change</th><th>Volume</th></tr>
  </thead>
  <tbody>
    <tr><td>ASML</td><td>642.10</td><td>-1.4%</td><td>1204800</td></tr>
    <tr><td>PHIA</td><td>21.55</td><td>+0.8%</td><td>3980100</td></tr>
    <tr><td>INGA</td><td>15.92</td><td>+0.2%</td><td>8112400</td></tr>
    <tr><td>HEIA</td><td>78.44</td><td>-0.6%</td><td>612300</td></tr>
  </tbody>
</table>
"""

table = BeautifulSoup(TABLE).find("table")

headers = [cell.get_text(strip=True) for cell in table.select("tr th")]
print(headers)

rows = []
for row in table.select("tbody tr"):
    cells = [cell.get_text(strip=True) for cell in row.find_all("td")]
    # strict=True refuses to guess when a row is short, which is a far better
    # failure than a silently misaligned column.
    rows.append(dict(zip(headers, cells, strict=True)))

for row in rows:
    print(row)

# From here the markup has stopped mattering. It is ordinary Python.
busiest = max(rows, key=lambda row: int(row["Volume"]))
print(busiest["Symbol"], f"{int(busiest['Volume']):,}")
