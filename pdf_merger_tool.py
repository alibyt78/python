import PyPDF2
import os

def merge_pdfs(pdf_list, output_path):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output_path)
    merger.close()

if __name__ == "__main__":
    merge_pdfs(['file1.pdf', 'file2.pdf'], 'merged.pdf')
    print("PDFs merged successfully.")
