from modules import dictionary_generator
from modules import hash_analyzer
from modules import brute_force_simulator
from modules import password_strength_analyzer
from modules import security_audit_engine
from modules import report_generator


def display_menu():
    print("\n" + "=" * 55)
    print("       PASSWORD CRACKING & CREDENTIAL ATTACK SUITE")
    print("=" * 55)
    print("1. Dictionary Generator")
    print("2. Hash Analyzer")
    print("3. Brute-Force Simulator")
    print("4. Password Strength Analyzer")
    print("5. Security Audit Engine")
    print("6. Report Generator")
    print("7. Run All Security Checks")
    print("8. Exit")
    print("=" * 55)


def run_dictionary_generator():
    dictionary_generator.generate_from_files(
        "datasets/sample_profiles.json",
        "datasets/common_passwords.txt",
        "reports/generated_wordlist.txt",
        max_entries=5000
    )


def run_hash_analyzer():
    hash_analyzer.analyze_hashes("datasets/sample_hashes.txt")


def run_all_checks():
    print("\n===== RUNNING ALL EDUCATIONAL MODULES =====")

    print("\n[1] Dictionary Generator")
    run_dictionary_generator()

    print("\n[2] Hash Analyzer")
    run_hash_analyzer()

    print("\n[3] Brute-Force Simulator")
    brute_force_simulator.run_simulation()

    print("\n[4] Password Strength Analyzer")
    password_strength_analyzer.main()

    print("\n[5] Security Audit Engine")
    audit_results = security_audit_engine.main()

    print("\n[6] Report Generator")
    report_generator.main(audit_results)

    print("\n===== ALL MODULES COMPLETED =====")


def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ").strip()

        try:
            if choice == "1":
                run_dictionary_generator()

            elif choice == "2":
                run_hash_analyzer()

            elif choice == "3":
                brute_force_simulator.run_simulation()

            elif choice == "4":
                password_strength_analyzer.main()

            elif choice == "5":
                security_audit_engine.main()

            elif choice == "6":
                report_generator.main()

            elif choice == "7":
                run_all_checks()

            elif choice == "8":
                print("\nThank you for using the Password Security Suite!")
                break

            else:
                print("\nInvalid choice. Please select a number from 1 to 8.")

        except Exception as error:
            print(f"\nAn error occurred: {error}")

        if choice != "8":
            input("\nPress Enter to return to the main menu...")


if __name__ == "__main__":
    main()
