import string


def calculate_search_space(password_length, character_set_size):
    if not isinstance(password_length, int) or password_length <= 0:
        raise ValueError("Password length must be positive.")

    if not isinstance(character_set_size, int) or character_set_size <= 0:
        raise ValueError("Character set size must be positive.")

    if character_set_size > 100:
        raise ValueError("Character set size cannot exceed 100.")

    return character_set_size ** password_length


def estimate_time(total_combinations, guesses_per_second):
    if guesses_per_second <= 0:
        raise ValueError("Guess rate must be positive.")

    return total_combinations / guesses_per_second


def format_time(seconds):
    if seconds < 60:
        return f"{seconds:.2f} seconds"

    if seconds < 3600:
        return f"{seconds / 60:.2f} minutes"

    if seconds < 86400:
        return f"{seconds / 3600:.2f} hours"

    if seconds < 31536000:
        return f"{seconds / 86400:.2f} days"

    return f"{seconds / 31536000:.2f} years"


def run_simulation():
    print("\n===== BRUTE-FORCE SIMULATOR =====")
    print("Educational search-space demonstration")
    print("No real accounts or passwords are accessed.")

    print("\nCharacter set options:")
    print("1. Digits (10 characters)")
    print("2. Lowercase letters (26 characters)")
    print("3. Uppercase + lowercase letters (52 characters)")
    print("4. Letters + digits (62 characters)")

    options = {
        "1": 10,
        "2": 26,
        "3": 52,
        "4": 62
    }

    choice = input("\nSelect option (1-4): ").strip()

    if choice not in options:
        print("Invalid option.")
        return

    try:
        length = int(input("Enter password length (1-12): "))

        if not 1 <= length <= 12:
            print("Length must be between 1 and 12.")
            return

        guesses_per_second = 1000

        combinations = calculate_search_space(
            length,
            options[choice]
        )

        estimated_seconds = estimate_time(
            combinations,
            guesses_per_second
        )

        print("\n===== SIMULATION RESULTS =====")
        print(f"Password length: {length}")
        print(f"Character set size: {options[choice]}")
        print(f"Possible combinations: {combinations:,}")
        print(f"Assumed guess rate: {guesses_per_second:,}/second")
        print(
            "Estimated exhaustive search time: "
            + format_time(estimated_seconds)
        )

        print("\nThis is a mathematical estimate, not a real attack.")

    except ValueError as error:
        print(f"Input error: {error}")


if __name__ == "__main__":
    run_simulation()
