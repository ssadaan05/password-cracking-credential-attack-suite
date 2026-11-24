from zxcvbn import zxcvbn


def analyze_password(password):
    result = zxcvbn(password)

    score = result["score"]

    strength_levels = {
        0: "Very Weak",
        1: "Weak",
        2: "Fair",
        3: "Strong",
        4: "Very Strong"
    }

    print("\n===== PASSWORD STRENGTH ANALYSIS =====")
    print(f"Password: {'*' * len(password)}")
    print(f"Strength: {strength_levels[score]}")
    print(f"Score: {score}/4")
    print(f"Estimated guesses: {result['guesses']:,}")
    print(
        "Estimated crack time: "
        + result["crack_times_display"]["offline_fast_hashing_1e10_per_second"]
    )

    feedback = result["feedback"]

    print("\n===== SECURITY FEEDBACK =====")

    if feedback["warning"]:
        print("Warning:", feedback["warning"])
    else:
        print("Warning: No specific warning.")

    if feedback["suggestions"]:
        for suggestion in feedback["suggestions"]:
            print("-", suggestion)
    else:
        print("- No additional suggestions.")

    print("\nThis is an educational estimate, not a guarantee of security.")


def main():
    print("\n===== PASSWORD STRENGTH ANALYZER =====")
    print("Use synthetic sample passwords only.")

    password = input("\nEnter a sample password: ")

    if not password:
        print("Error: Password cannot be empty.")
        return

    analyze_password(password)


if __name__ == "__main__":
    main()
