def add_status_column(columns: list[str]) -> None:
    columns.append("status")
    print(f"Inside: {columns}")


fields = ["id", "total"]
add_status_column(fields)
print(f"After call: {fields}")
