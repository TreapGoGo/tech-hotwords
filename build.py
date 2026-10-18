import argparse
import csv
import json
import re
import unicodedata
from datetime import date
from pathlib import Path
from urllib.parse import urlparse


PACKS = {
    "ai": "AI 模型、产品与人物",
    "dev": "开发工具与协议",
    "hardware": "芯片、算力与机器人",
    "topics": "AI 概念与创投话题",
}


def normalized(word: str) -> str:
    return unicodedata.normalize("NFKC", word).casefold()


def load(root: Path) -> tuple[dict, list[dict], dict[str, list[str]]]:
    catalog = json.loads((root / "sources.json").read_text(encoding="utf-8"))
    date.fromisoformat(catalog["reviewed"])
    sources = {}
    for source in catalog["sources"]:
        source_id = source["id"]
        if source_id in sources or not re.fullmatch(r"[a-z0-9-]+", source_id):
            raise ValueError(f"Duplicate or invalid source: {source_id}")
        address = urlparse(source["url"])
        if address.scheme != "https" or not address.netloc or not source["observed"]:
            raise ValueError(f"Invalid source: {source_id}")
        if source["kind"] not in {"official", "community", "media"}:
            raise ValueError(f"Invalid source kind: {source_id}")
        if source["language"] not in {"zh", "en"}:
            raise ValueError(f"Invalid source language: {source_id}")
        sources[source_id] = source
    packages = {name: [] for name in PACKS}
    seen_words = set()
    seen_concepts = set()
    with (root / "lexicon.tsv").open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if reader.fieldnames != ["pack", "canonical", "aliases", "sources"]:
            raise ValueError("Invalid lexicon header")
        entries = list(reader)
    for entry in entries:
        package = entry["pack"]
        canonical = entry["canonical"]
        if package not in PACKS or normalized(canonical) in seen_concepts:
            raise ValueError(f"Duplicate concept or invalid package: {canonical}")
        seen_concepts.add(normalized(canonical))
        references = entry["sources"].split("|")
        if not references or any(reference not in sources for reference in references):
            raise ValueError(f"Missing source: {canonical}")
        forms = [canonical] + (entry["aliases"].split("|") if entry["aliases"] else [])
        if len(forms) > 4:
            raise ValueError(f"Too many variants: {canonical}")
        for word in forms:
            if not word or word != word.strip() or len(word) > 80 or len(word.encode("utf-8")) > 256:
                raise ValueError(f"Invalid word length: {word}")
            if any(unicodedata.category(character).startswith("C") for character in word) or any(character in word for character in "<>#"):
                raise ValueError(f"Invalid word: {word}")
            if normalized(word) in seen_words:
                raise ValueError(f"Duplicate word: {word}")
            if re.search(r"[\u3400-\u9fff]", word) and not any(sources[reference]["language"] == "zh" for reference in references):
                raise ValueError(f"Chinese usage source missing: {word}")
            seen_words.add(normalized(word))
            packages[package].append(word)
    for package, words in packages.items():
        if not 1 <= len(words) <= 150:
            raise ValueError(f"Package exceeds client limit: {package}: {len(words)}")
    if len(seen_words) > 600:
        raise ValueError("Combined packs exceed the default client limit")
    return catalog, entries, packages


def render(root: Path) -> dict[str, str]:
    catalog, entries, packages = load(root)
    outputs = {}
    index = []
    for package, words in packages.items():
        filename = package + ".txt"
        outputs[filename] = f"# {PACKS[package]}；每行一个写法，来源与别称分组见 lexicon.tsv\n" + "\n".join(words) + "\n"
        index.append({"file": filename, "name": PACKS[package], "count": len(words), "updated": catalog["reviewed"]})
    outputs["index.json"] = json.dumps(index, ensure_ascii=False, indent=2) + "\n"
    return outputs


def main() -> None:
    parser = argparse.ArgumentParser(description="Build client wordpacks from the reviewed concept lexicon")
    parser.add_argument("--check", action="store_true", help="Check generated files without writing")
    arguments = parser.parse_args()
    root = Path(__file__).resolve().parent
    for filename, content in render(root).items():
        if arguments.check:
            if (root / filename).read_text(encoding="utf-8") != content:
                raise ValueError(f"Generated file differs: {filename}; run python build.py")
        else:
            (root / filename).write_text(content, encoding="utf-8", newline="\n")
        print(f"PASS {filename}")


if __name__ == "__main__":
    main()
