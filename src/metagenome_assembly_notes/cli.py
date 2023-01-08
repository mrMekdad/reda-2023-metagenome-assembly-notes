import argparse
from metagenome_assembly_notes.core import build_snapshot


def main() -> None:
    parser = argparse.ArgumentParser(description="Assembly tracking helpers with sample manifests and reporting utilities.")
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args()
    if args.summary:
        print(build_snapshot())


if __name__ == "__main__":
    main()
