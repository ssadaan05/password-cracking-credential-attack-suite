import json
from pathlib import Path

MAX_ALLOWED_ENTRIES = 10000

NUMBERS = ["1", "12", "123", "2024", "2025", "2026"]
SYMBOLS = ["!", "@", "#", "?"]

LEET_MAP = {
    "a": "4",
    "e": "3",
    "i": "1",
    "o": "0",
    "s": "5",
    "t": "7"
}


def validate_limit(limit):
    if not isinstance(limit, int) or limit <= 0:
        raise ValueError("Limit must be a positive integer.")

    if limit > MAX_ALLOWED_ENTRIES:
        raise ValueError(
            f"Maximum allowed entries: {MAX_ALLOWED_ENTRIES}"
        )

    return limit


def load_profiles(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        profiles = json.load(file)

    if not isinstance(profiles, list):
        raise ValueError("Profiles must be stored as a JSON list.")

    return profiles


def load_common_passwords(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return [
            line.strip()
            for line in file
            if line.strip()
        ]


def generate_variations(value):
    value = str(value).strip()

    if not value:
        return set()

    variations = {
        value.lower(),
        value.upper(),
        value.capitalize()
    }

    for number in NUMBERS:
        variations.add(value.lower() + number)

    for symbol in SYMBOLS:
        variations.add(value.lower() + symbol)

    leet_value = value.lower()

    for original, replacement in LEET_MAP.items():
        leet_value = leet_value.replace(original, replacement)

    variations.add(leet_value)

    return variations


def build_candidates(profiles, common_passwords, max_entries):
    limit = validate_limit(max_entries)
    candidates = set()

    for password in common_passwords:
        candidates.add(password)

        if len(candidates) >= limit:
            return sorted(candidates)[:limit]

    for profile in profiles:
        if not isinstance(profile, dict):
            continue

        for value in profile.values():
            for candidate in generate_variations(value):
                candidates.add(candidate)

                if len(candidates) >= limit:
                    return sorted(candidates)[:limit]

    return sorted(candidates)


def save_wordlist(candidates, output_path):
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    with output.open("w", encoding="utf-8") as file:
        for candidate in candidates:
            file.write(candidate + "\n")

    return len(candidates)


def generate_from_files(
    profiles_path,
    common_passwords_path,
    output_path,
    max_entries=5000
):
    profiles = load_profiles(profiles_path)
    common_passwords = load_common_passwords(
        common_passwords_path
    )

    candidates = build_candidates(
        profiles,
        common_passwords,
        max_entries
    )

    total = save_wordlist(candidates, output_path)

    print("\nDictionary generation completed!")
    print(f"Total entries: {total}")
    print(f"Output file: {output_path}")

    return total


if __name__ == "__main__":
    generate_from_files(
        "datasets/sample_profiles.json",
        "datasets/common_passwords.txt",
        "reports/generated_wordlist.txt",
        max_entries=5000
    )
