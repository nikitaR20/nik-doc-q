from pathlib import Path
import pdfkit
import os
import shutil

def convert_htmls_and_collect_csvs(base_path, pdf_output_base=None):
    base_path = Path(base_path)
    pdf_output_base = Path(pdf_output_base) if pdf_output_base else base_path

    csv_paths = []

    html_files = base_path.rglob("*.html")

    for html_path in html_files:
        relative_path = html_path.relative_to(base_path)
        pdf_path = (pdf_output_base / relative_path).with_suffix(".pdf")
        pdf_path.parent.mkdir(parents=True, exist_ok=True)

        if not pdf_path.exists():  # avoid re-converting
            try:
                pdfkit.from_file(str(html_path), str(pdf_path))
                print(f"Converted: {html_path} → {pdf_path}")
            except Exception as e:
                print(f"Failed to convert {html_path}: {e}")

    # Collect CSV files
    for csv_path in base_path.rglob("*.csv"):
        relative_path = csv_path.relative_to(base_path)
        new_csv_path = pdf_output_base / relative_path
        new_csv_path.parent.mkdir(parents=True, exist_ok=True)

        shutil.copy2(csv_path, new_csv_path)
        csv_paths.append(str(new_csv_path))
        print(f"Copied CSV: {csv_path} → {new_csv_path}")
