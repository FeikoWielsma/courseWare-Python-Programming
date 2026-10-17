from cameras3 import canon_info, nikon_info


def main() -> None:
    print("Cameras package entry point:")
    canon_info()
    nikon_info()


if __name__ == "__main__":
    main()
