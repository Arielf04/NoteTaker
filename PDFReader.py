import pdfplumber

pdf_path = ""
startPage = 3
endPage = 10

def get_page_range(startPage, endPage):
    return list(range(startPage, endPage + 1))

pages = get_page_range(startPage, endPage)

def parse_text_from_pdf(pdf_file_path, pages_to_parse=None):
    # Initialize an empty string to store the parsed text
    parsed_text = ''

    # Open the PDF file with pdfplumber
    with pdfplumber.open(pdf_file_path) as pdf:
        # Get the total number of pages in the PDF
        num_pages = len(pdf.pages)

        # If no pages specified, parse all pages
        if pages_to_parse is None:
            pages_to_parse = range(num_pages)

        # Iterate through specified pages and extract the text
        for page_num in pages_to_parse:
            # Check if the page number is valid
            if 0 <= page_num < num_pages:
                page = pdf.pages[page_num]
                parsed_text += page.extract_text()
            else:
                print(f"Page number {page_num} is out of range.")

    return parsed_text

# Example usage:
parsed_text = parse_text_from_pdf(pdf_path, pages)
print(parsed_text)
