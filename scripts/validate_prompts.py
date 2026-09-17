from __future__ import annotations

from pathlib import Path

README_PATH = Path(__file__).resolve().parents[1] / "README.md"
EXPECTED_SECTIONS = [
    "ZORG👽 Jailbreak Prompt Text",
    "## Scope and intended use",
    "## Prompt catalog",
    "Base prompt — copy and paste into a chat box",
    "Google Gemini variant",
    "DeepSeek variant",
]


def main() -> None:
    text = README_PATH.read_text(encoding="utf-8")
    missing = [section for section in EXPECTED_SECTIONS if section not in text]
    if missing:
        raise SystemExit(
            "README validation failed. Missing sections: " + ", ".join(missing)
        )

    print(f"README validation passed for {README_PATH.name}.")


if __name__ == "__main__":
    main()
