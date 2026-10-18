def print_dispatch(destination: str, *items: str, **details: str) -> None:
    print(f"Send to {destination}")
    for item in items:
        print(f"- {item}")
    for name, value in details.items():
        print(f"{name}: {value}")


print_dispatch("London", "keyboard", "mouse", service="express", reference="A104")
print_dispatch("Paris", "monitor", service="standard")
