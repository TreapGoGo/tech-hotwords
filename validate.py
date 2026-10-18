import json
from pathlib import Path


def validate(root: Path) -> None:
    index = json.loads((root / "index.json").read_text(encoding="utf-8"))
    all_words = set()
    for package in index:
        name = package["file"]
        if name not in {"ai.txt", "dev.txt", "hardware.txt"}:
            raise ValueError(f"Unexpected package: {name}")
        text = (root / name).read_text(encoding="utf-8", errors="strict")
        words = [line.strip() for line in text.splitlines() if line.strip() and not line.startswith("#")]
        if not 50 <= len(words) <= 150 or len(words) != package["count"]:
            raise ValueError(f"Count mismatch: {name}")
        for word in words:
            normalized = word.casefold()
            if normalized in all_words:
                raise ValueError(f"Duplicate word: {word}")
            if len(word) > 128 or "<" in word or ">" in word:
                raise ValueError(f"Invalid word: {word}")
            all_words.add(normalized)
        print(f"PASS {name}: {len(words)} words")


if __name__ == "__main__":
    validate(Path(__file__).resolve().parent)

