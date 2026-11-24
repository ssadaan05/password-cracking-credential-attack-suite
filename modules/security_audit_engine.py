
from pathlib import Path

from modules.hash_analyzer import identify_hash
from zxcvbn import zxcvbn


BASE_DIR = Path(__file__).resolve().parent.parent

COMMON_PASSWORD_FILE = BASE_DIR / "datasets" / "common_passwords.txt"
SAMPLE_HASH_FILE = BASE_DIR / "datasets" / "sample_hashes.txt"


def load_common_passwords():
    with open(COMMON_PASSWORD_FILE, "r", encoding="utf-8") as file:
        return {
            line.strip().lower()
            for line in file
            if line.strip()
        }


def check_common_password(password):
    common_passwords = load_common_passwords()
    return password.lower() in common_passwords


def audit_password(password):
    result = zxcvbn(password)
    is_common = check_common_password(password)
    score = result["score"]

    strength_levels = {
        0: "Very Weak",
        1: "Weak",
        2: "Fair",
        3: "Strong",
        4: "Very Strong"
    }

    recommendations = []

    if score <= 1:
        recommendations.append(
            "Use a longer and less predictable password."
        )
    elif score == 2:
        recommendations.append(
            "Improve password length and uniqueness."
        )
    else:
        recommendations.append(
            "Continue using unique passwords for each account."
        )

    if is_common:
        recommendations.append(
            "Avoid commonly used passwords."
        )

    print("\n===== PASSWORD SECURITY AUDIT =====")

    print(
        "Common password check: "
        + ("FOUND" if is_common else "NOT FOUND")
    )

    print(f"Password strength: {strength_levels[score]}")
    print(f"Strength score: {score}/4")

    print("\n===== AUDIT RECOMMENDATIONS =====")

    for recommendation in recommendations:
        print(f"- {recommendation}")

    print("\nPassword audit completed.")

    return {
        "common_password": is_common,
        "strength": strength_levels[score],
        "score": score,
        "recommendations": recommendations
    }


def audit_sample_hashes():
    print("\n===== SAMPLE HASH AUDIT =====")

    with open(SAMPLE_HASH_FILE, "r", encoding="utf-8") as file:
        hashes = [
            line.strip()
            for line in file
            if line.strip()
        ]

    hash_results = []

    for index, hash_value in enumerate(hashes, start=1):
        analysis = identify_hash(hash_value)

        print(f"Hash {index}: {analysis}")

        hash_results.append({
            "hash_number": index,
            "analysis": analysis
        })

    return hash_results


def main():
    print("\n===== SECURITY AUDIT ENGINE =====")
    print("Educational audit using synthetic sample data.")

    password = input(
        "\nEnter a synthetic sample password: "
    )

    if not password:
        print("Error: Password cannot be empty.")
        return None

    password_result = audit_password(password)
    hash_results = audit_sample_hashes()

    print("\n===== SECURITY AUDIT COMPLETED =====")

    return {
        "password_audit": password_result,
        "hash_results": hash_results
    }


if __name__ == "__main__":
    main()
