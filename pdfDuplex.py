import PyPDF2
import argparse
import sys
import os

def combine_duplex(front_pdf_path, back_pdf_path, output_pdf_path):
    # Read both PDFs
    front_reader = PyPDF2.PdfReader(front_pdf_path)
    back_reader = PyPDF2.PdfReader(back_pdf_path)

    # Reverse back pages
    back_pages = list(back_reader.pages)[::-1]

    # Prepare writer
    writer = PyPDF2.PdfWriter()

    # Interleave pages
    for front_page, back_page in zip(front_reader.pages, back_pages):
        writer.add_page(front_page)
        writer.add_page(back_page)

    # Write output
    with open(output_pdf_path, "wb") as f_out:
        writer.write(f_out)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Combine front and back scanned PDFs into duplex order.")
    parser.add_argument("front_pdf", nargs="?", default="front.pdf", help="Path to the PDF with front pages")
    parser.add_argument("back_pdf", nargs="?", default="back.pdf", help="Path to the PDF with back pages")
    parser.add_argument("output_pdf", nargs="?", default="combined.pdf", help="Path to save the combined PDF")
    args = parser.parse_args()

    # Error handling for file existence
    if not os.path.isfile(args.front_pdf):
        print(f"Error: Front PDF '{args.front_pdf}' does not exist.")
        sys.exit(1)
    if not os.path.isfile(args.back_pdf):
        print(f"Error: Back PDF '{args.back_pdf}' does not exist.")
        sys.exit(1)

    try:
        combine_duplex(args.front_pdf, args.back_pdf, args.output_pdf)
        print(f"Combined PDF saved to '{args.output_pdf}'.")
    except Exception as e:
        print(f"Error combining PDFs: {e}")
        sys.exit(1)
