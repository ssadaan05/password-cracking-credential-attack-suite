# Password Cracking & Credential Attack Suite

An educational Python-based cybersecurity project that demonstrates password security concepts through dictionary generation, hash analysis, brute-force search-space estimation, password strength evaluation, security auditing, and automated report generation.

This project was developed for cybersecurity learning, practical experimentation, and portfolio demonstration using synthetic sample data.

## Project Overview

The Password Cracking & Credential Attack Suite provides a menu-driven environment to explore common password security concepts.

It combines multiple educational modules into one application and generates security audit reports in TXT, CSV, and PDF formats.

**Important:** This is an educational security auditing project. It does not access real accounts, collect credentials, or perform attacks against live systems.

## Features

### 1. Dictionary Generator
- Generates sample password candidates using synthetic profile data.
- Creates variations of sample words.
- Removes duplicate entries.
- Applies a configurable maximum entry limit.
- Saves generated candidates to a text file.

### 2. Hash Analyzer
- Identifies possible hash formats using hash length.
- Supports sample MD5, SHA-1, and SHA-256 demonstrations.
- Generates hashes using supported algorithms.
- Analyzes synthetic hash samples.

*Note: Hash identification based on length is approximate and cannot reliably identify every hash algorithm.*

### 3. Brute-Force Simulator
- Demonstrates password search-space calculations.
- Supports different character sets.
- Calculates possible combinations.
- Estimates theoretical guessing time using a configurable guessing rate.

*This module performs mathematical estimation only. It does not attempt to crack passwords.*

### 4. Password Strength Analyzer
- Evaluates password strength using the zxcvbn library.
- Displays a strength score from 0 to 4.
- Estimates password guessing difficulty.
- Provides security feedback and recommendations.
- Masks passwords in displayed output.

### 5. Security Audit Engine
- Checks passwords against a sample common-password list.
- Evaluates password strength.
- Analyzes synthetic sample hashes.
- Generates security recommendations.

### 6. Report Generator
- Generates security audit reports.
- Supports TXT, CSV, and PDF formats.
- Uses audit results from the security audit engine.
- Saves reports inside the reports directory.

## Technologies Used

- Python 3
- Bash
- Kali Linux
- zxcvbn
- Colorama
- ReportLab
- CSV
- JSON
- Pytest / Python unittest

## Project Structure

```text
password-cracking-credential-attack-suite/
│
├── datasets/
│   ├── common_passwords.txt
│   └── sample_hashes.txt
│
├── modules/
│   ├── __init__.py
│   ├── dictionary_generator.py
│   ├── hash_analyzer.py
│   ├── brute_force_simulator.py
│   ├── password_strength_analyzer.py
│   ├── security_audit_engine.py
│   └── report_generator.py
│
├── reports/
│   ├── generated_wordlist.txt
│   ├── security_audit_report.txt
│   ├── security_audit_report.csv
│   └── security_audit_report.pdf
│
├── screenshots/
│
├── tests/
│   ├── __init__.py
│   ├── test_brute_force_simulator.py
│   ├── test_dictionary_generator.py
│   ├── test_hash_analyzer.py
│   ├── test_password_strength_analyzer.py
│   ├── test_report_generator.py
│   └── test_security_audit_engine.py
│
├── main.py
├── requirements.txt
└── README.md
```

## Installation

### Requirements

- Kali Linux or another Linux distribution
- Python 3
- Git
- pip

### 1. Clone the repository

```bash
git clone https://github.com/ssadaan05/password-cracking-credential-attack-suite.git
```

### 2. Navigate to the project directory

```bash
cd password-cracking-credential-attack-suite
```

### 3. Create a virtual environment

```bash
python3 -m venv venv
```

### 4. Activate the virtual environment

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

Start the application:

```bash
python main.py
```

The application provides the following menu:

| Option | Module |
|---|---|
| 1 | Dictionary Generator |
| 2 | Hash Analyzer |
| 3 | Brute-Force Simulator |
| 4 | Password Strength Analyzer |
| 5 | Security Audit Engine |
| 6 | Report Generator |
| 7 | Run All Security Checks |
| 8 | Exit |

Select an option and follow the on-screen instructions.

Use synthetic sample passwords only.

## Running Tests

Run the complete test suite:

```bash
python -m unittest discover -s tests -v
```

The project includes **36 unit tests** covering the six modules and their functionality.

## Generated Reports

The application can generate the following reports:

- `reports/security_audit_report.txt`
- `reports/security_audit_report.csv`
- `reports/security_audit_report.pdf`

Generated dictionary candidates are saved to:

- `reports/generated_wordlist.txt`

## Screenshots

The `screenshots/` directory contains project execution screenshots, including:

- Python environment setup
- Project directory structure
- Dictionary generation
- Hash analysis
- Brute-force simulation
- Password strength analysis
- Security audit execution
- Report generation
- Unit test results
- Main application menu

These screenshots demonstrate the implementation and execution of the project.

## Learning Outcomes

Through this project, I gained practical experience with:

- Python programming and modular application development.
- Password security and password strength evaluation.
- Hash formats and cryptographic hashing concepts.
- Search-space calculations and theoretical brute-force estimation.
- Security auditing and automated recommendations.
- Report generation using TXT, CSV, and PDF formats.
- Unit testing and debugging.
- Git and GitHub version control.

## Security Disclaimer

This project is intended strictly for educational purposes and authorized cybersecurity learning.

- Uses synthetic sample data.
- Does not access real user accounts.
- Does not collect or extract credentials.
- Does not perform attacks against live systems.
- Brute-force functionality is limited to theoretical search-space estimation.

Use cybersecurity knowledge responsibly and only in authorized environments.

## Author

**Mohammed Sadaan Imran Shaikh**

GitHub: [@ssadaan05](https://github.com/ssadaan05)

LinkedIn: [Mohammed Sadaan Shaikh](https://www.linkedin.com/in/mohammed-sadaan-shaikh-810482152/)
