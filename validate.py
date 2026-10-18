from pathlib import Path

from build import load, render


def validate(root: Path) -> None:
    catalog, entries, packages = load(root)
    for filename, expected in render(root).items():
        content = (root / filename).read_text(encoding="utf-8", errors="strict")
        if content != expected:
            raise ValueError(f"Generated file differs: {filename}; run python build.py")
    for name, words in packages.items():
        print(f"PASS {name}.txt: {len(words)} forms")
    print(f"PASS {len(entries)} concepts, {sum(map(len, packages.values()))} forms, {len(catalog['sources'])} sources")


if __name__ == "__main__":
    validate(Path(__file__).resolve().parent)

