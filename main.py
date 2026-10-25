
import os
import subprocess
import shutil

# Project directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

INPUT_DIR = os.path.join(BASE_DIR, "input")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

# LibreOffice executable
LIBREOFFICE = (
    shutil.which("soffice")
    or "/Applications/LibreOffice.app/Contents/MacOS/soffice"
)


def convert_word_to_pdf(filename):

    # Create full input path
    input_path = os.path.join(INPUT_DIR, filename)

    # Check if input file exists
    if not os.path.isfile(input_path):
        print(f"Error: {filename} not found.")
        return None

    # Create output directory if necessary
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Generate PDF filename
    pdf_filename = os.path.splitext(filename)[0] + ".pdf"
    output_path = os.path.join(OUTPUT_DIR, pdf_filename)

    # Check LibreOffice installation
    if not os.path.isfile(LIBREOFFICE):
        print("Error: LibreOffice not found.")
        return None

    # Convert Word to PDF
    command = [
        LIBREOFFICE,
        "--headless",
        "--convert-to", "pdf",
        "--outdir", OUTPUT_DIR,
        input_path
    ]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    # Check conversion result
    if result.returncode == 0 and os.path.isfile(output_path):
        print(f"Successfully converted: {filename}")
        print(f"PDF saved to: {output_path}")
        return output_path

    print(f"Conversion failed: {filename}")
    print(result.stderr)
    print(result.stdout)
    return None


if __name__ == "__main__":
    convert_word_to_pdf("cv_Attia.docx")
