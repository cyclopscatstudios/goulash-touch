#!/usr/bin/env python3
"""Check word-count budgets for Kampánykörút campaign question JSON.

Usage: python scripts/check_campaign_copy.py path/to/questions.json
No extra packages required. Exits 1 for hard-limit violations, 0 otherwise.
"""
import argparse
import json
from pathlib import Path

HARD = {"title": 8, "question": 55, "answer": 25, "total": 120}
WARN = {"title": 6, "question": 45, "answer": 22, "total": 110}


def wc(value):
    return len(value.split())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="Kampánykörút questions JSON array")
    args = parser.parse_args()
    data = json.loads(args.path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        parser.error("Expected a JSON array of questions")
    warnings = errors = 0

    def check(identifier, part, count):
        nonlocal warnings, errors
        limit = HARD[part]
        if count > limit:
            errors += 1
            print(f"ERROR {identifier}: {part} {count} words > {limit}")
        elif count > WARN[part]:
            warnings += 1
            print(f"WARN  {identifier}: {part} {count} words (preferred ≤{WARN[part]})")

    for index, item in enumerate(data):
        if not isinstance(item, dict):
            parser.error(f"Question at index {index} is not an object")
        identifier = item.get("id", f"index-{index}")
        question = item.get("question", "")
        title = item.get("title", "")
        answers = item.get("possibleAnswers", [])
        if not isinstance(question, str) or not isinstance(title, str) or not isinstance(answers, list):
            parser.error(f"Invalid schema for {identifier}")
        check(identifier, "title", wc(title))
        check(identifier, "question", wc(question))
        answer_total = 0
        for aindex, answer in enumerate(answers):
            if not isinstance(answer, dict) or not isinstance(answer.get("label"), str):
                parser.error(f"Invalid answer at {identifier}/{aindex}")
            word_count = wc(answer["label"])
            answer_total += word_count
            check(f"{identifier}/{answer.get('id', aindex)}", "answer", word_count)
        if len(answers) == 4:
            check(identifier, "total", wc(question) + answer_total)
        else:
            print(f"INFO  {identifier}: {len(answers)} answers; 4-option total budget not applied")
    print(f"\nChecked {len(data)} questions: {warnings} warnings, {errors} errors.")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
