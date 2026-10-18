"""Check quoted stdout against executed Python fences or their named demos.

Annotated diagrams, syntax examples and machine-dependent benchmark recordings
are classified explicitly. New text fences must execute or have a classification.
"""

import re
import sys

from check_support import ROOT, run_case, workspace

FENCE = re.compile(r"^```(\w+)[ \t]*\n(.*?)^```[ \t]*$", re.MULTILINE | re.DOTALL)
# These text fences are not literal stdout. Keep the reason visible in the report.
ILLUSTRATIONS = {
    ("04-web-scraping", "Status Codes and Timeouts"): "HTTP status reference table",
    ("04-web-scraping", "SQL Injection"): "annotated SQL error and parameter example",
    ("05-sqlalchemy", "Engine and URL"): "connection URL syntax and examples",
    ("05-sqlalchemy", "Bound Parameters"): "SQL source illustrating an unescaped quote",
    ("09-appendix-subprocess", "pathlib Alternatives"): "command-to-API reference",
}
DEMO_SOURCES = {
    ("01-inheritance", "Enforcing the Contract"): "demos/01-inheritance/08_abstract_contract.py",
}


def main() -> int:
    failed = checked = classified = 0
    seen = set()
    with workspace() as (course, environment):
        for markdown in sorted((ROOT / "src").glob("*/**/*.md")):
            text = markdown.read_text(encoding="utf-8")
            # Blank fenced bodies before splitting, so examples cannot introduce pages.
            # Preserve offsets and ignore separator-like lines inside fenced code.
            boundaries = FENCE.sub(
                lambda match: re.sub(r"[^\n]", " ", match[0]), text,
            )
            starts = [0, *(match.end() for match in re.finditer(r"^---[ \t]*$", boundaries, re.M))]
            for start, end in zip(starts, [*starts[1:], len(text)], strict=True):
                page = text[start:end]
                title = re.search(r"^# (.+)$", FENCE.sub("", page), re.M)
                if not title:
                    continue
                key = (markdown.parent.name, title[1])
                blocks = list(FENCE.finditer(page))
                for index, block in enumerate(blocks):
                    if block[1] != "text":
                        continue
                    if key in ILLUSTRATIONS:
                        seen.add(key)
                        classified += 1
                        print(f"REFERENCE {key}: {ILLUSTRATIONS[key]}")
                        continue
                    checked += 1
                    previous = blocks[index - 1] if index else None
                    if key in DEMO_SOURCES:
                        relative = ROOT / DEMO_SOURCES[key]
                        relative = relative.relative_to(ROOT)
                    elif previous and previous[1] == "python":
                        relative = markdown.relative_to(ROOT).with_suffix(f".audit{index}.py")
                        (course / relative).write_text(previous[2], encoding="utf-8")
                    else:
                        pill = re.search(r"> `demo(\d+) · ([^`]+)`", page)
                        candidates = list((ROOT / "demos").glob(
                            f"{markdown.parent.name[:2]}*/*{pill[1]}_{pill[2]}.py"
                        )) if pill else []
                        if len(candidates) != 1:
                            print(f"FAIL {key}: text fence has no executable source")
                            failed += 1
                            continue
                        relative = candidates[0].relative_to(ROOT)
                    failed += not run_case(
                        course, environment, relative.as_posix(), label=f"output{index}",
                        quoted=block[2],
                    )
    for stale in ILLUSTRATIONS.keys() - seen:
        print(f"FAIL stale output classification: {stale}")
        failed += 1
    print(f"{checked} output quotes checked, {classified} references classified, {failed} failed")
    return int(failed > 0)


if __name__ == "__main__":
    sys.exit(main())
