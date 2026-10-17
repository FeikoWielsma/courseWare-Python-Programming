import argparse
import sys

# Kept in memory so the demo has no side effects; a real tool would use a file.
INVENTORY: dict[str, int] = {"db01": 5432, "web01": 80}


def cmd_add(args: argparse.Namespace) -> int:
    INVENTORY[args.host] = args.port
    print(f"added {args.host} on port {args.port}")
    return 0


def cmd_list(args: argparse.Namespace) -> int:
    hosts = sorted(INVENTORY, reverse=args.reverse)
    for host in hosts:
        print(f"{host:<8} {INVENTORY[host]}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="A small host inventory.")
    # dest names the attribute holding the chosen verb; required refuses a bare call.
    verbs = parser.add_subparsers(dest="command", required=True, metavar="COMMAND")

    add = verbs.add_parser("add", help="add a host to the inventory")
    add.add_argument("host", help="the host name")
    add.add_argument("--port", type=int, default=22, help="the port it answers on")
    # Each subparser carries the function that implements it, so main stays flat.
    add.set_defaults(handler=cmd_add)

    listing = verbs.add_parser("list", help="list the known hosts")
    listing.add_argument("--reverse", action="store_true", help="sort Z to A")
    listing.set_defaults(handler=cmd_list)

    return parser


def main(argv: list[str]) -> int:
    args = build_parser().parse_args(argv)
    return args.handler(args)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        raise SystemExit(main(sys.argv[1:]))
    main(["add", "web01", "--port", "443"])
    main(["list", "--reverse"])
