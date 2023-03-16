import pdfplumber

def extract_text_from_pages(pdf_path, page_numbers):
    with pdfplumber.open(pdf_path) as pdf:
        text = ''
        for page_number in page_numbers:
            page = pdf.pages[page_number - 1]  # Subtract 1 since pages are 0-indexed
            text += page.extract_text()
    return text

pdf_path = 'E:\\NoteTaker\\cv_v1.pdf'
specified_pages = [2]  # List the page numbers you want to parse

extracted_text = extract_text_from_pages(pdf_path, specified_pages)
print(extracted_text)
