
import csv
from datetime import datetime
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

from modules import security_audit_engine


BASE_DIR = Path(__file__).resolve().parent.parent
REPORT_DIR = BASE_DIR / "reports"


def prepare_report_data(audit_results=None):

    # Retain the original demonstration data for compatibility.
    if audit_results is None:
        return [
            ["Security Check", "Result", "Status"],
            ["Common Password Detection", "Sample password: password", "Weak"],
            ["Password Strength", "0/4 - Very Weak", "Warning"],
            ["Hash Analysis", "4 sample hashes analyzed", "Completed"],
            ["Brute-Force Simulation", "Educational calculation only", "Completed"],
        ]

    password_audit = audit_results["password_audit"]
    hash_results = audit_results["hash_results"]

    common_password = password_audit["common_password"]
    strength = password_audit["strength"]
    score = password_audit["score"]
    recommendations = password_audit["recommendations"]

    common_result = (
        "Found in common password list"
        if common_password
        else "Not found in common password list"
    )

    common_status = "Warning" if common_password else "Clear"

    if score <= 1:
        strength_status = "Warning"
    elif score == 2:
        strength_status = "Review"
    else:
        strength_status = "Good"

    recommendation_text = "; ".join(recommendations)

    return [
        ["Security Check", "Result", "Status"],
        ["Common Password Detection", common_result, common_status],
        ["Password Strength", f"{score}/4 - {strength}", strength_status],
        [
            "Hash Analysis",
            f"{len(hash_results)} sample hashes analyzed",
            "Completed",
        ],
        ["Audit Recommendations", recommendation_text, "Review"],
    ]


def generate_txt_report(data):
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    file_path = REPORT_DIR / "security_audit_report.txt"

    with open(file_path, "w", encoding="utf-8") as file:
        file.write("PASSWORD SECURITY AUDIT REPORT\n")
        file.write("=" * 45 + "\n")
        file.write(f"Generated: {datetime.now()}\n\n")

        for row in data[1:]:
            file.write(f"Check: {row[0]}\n")
            file.write(f"Result: {row[1]}\n")
            file.write(f"Status: {row[2]}\n")
            file.write("-" * 45 + "\n")

        file.write("\nEducational report using synthetic sample data.\n")

    return file_path


def generate_csv_report(data):
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    file_path = REPORT_DIR / "security_audit_report.csv"

    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(data)

    return file_path


def generate_pdf_report(data):
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    file_path = REPORT_DIR / "security_audit_report.pdf"

    document = SimpleDocTemplate(
        str(file_path),
        pagesize=A4,
    )

    styles = getSampleStyleSheet()
    elements = []

    elements.append(
        Paragraph("Password Security Audit Report", styles["Title"])
    )

    elements.append(Spacer(1, 20))

    elements.append(
        Paragraph(
            f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            styles["Normal"],
        )
    )

    elements.append(Spacer(1, 20))

    table = Table(data, repeatRows=1)

    table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
            ("PADDING", (0, 0), (-1, -1), 8),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ])
    )

    elements.append(table)
    elements.append(Spacer(1, 20))

    elements.append(
        Paragraph(
            "This report is generated for educational purposes "
            "using synthetic sample data.",
            styles["Normal"],
        )
    )

    document.build(elements)

    return file_path


def main(audit_results=None):
    print("\n===== SECURITY REPORT GENERATOR =====")

    if audit_results is None:
        print("\nA new synthetic password audit is required.")
        audit_results = security_audit_engine.main()

    if audit_results is None:
        print("\nReport generation cancelled: No audit results available.")
        return

    data = prepare_report_data(audit_results)

    txt_file = generate_txt_report(data)
    csv_file = generate_csv_report(data)
    pdf_file = generate_pdf_report(data)

    print("\nReports generated successfully:")
    print(f"TXT: {txt_file}")
    print(f"CSV: {csv_file}")
    print(f"PDF: {pdf_file}")

    print("\n===== REPORT GENERATION COMPLETED =====")


if __name__ == "__main__":
    main()
