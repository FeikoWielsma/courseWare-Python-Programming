def with_status_column(columns: list[str]) -> list[str]:
    columns = columns + ["status"]
    return columns


fields = ["id", "total"]
updated = with_status_column(fields)
print(f"Original: {fields}")
print(f"Export: {updated}")
