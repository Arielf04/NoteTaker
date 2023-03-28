import pdfplumber
import openai

pdf_file_path = ''

def get_page_range(user_pages):
    if not user_pages:
        return None
    user_pages_split = user_pages.split(',')
    user_pages_split_as_int = [int(x) for x in user_pages_split]
    return list(range(user_pages_split_as_int[0] - 1, user_pages_split_as_int[1]))

def parse_text_from_pdf(user_pages):
    # Initialize an empty string to store the parsed text
    parsed_text = ''

    pages_to_parse = get_page_range(user_pages)
    
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

    print(parsed_text)

    return parsed_text

def call_chatgpt_api(parsed_text, api_key):
    openai.api_key = api_key

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Summarize the following information in bullet points: " + parsed_text,
        max_tokens=256,
        n=1,
        stop=None,
        temperature=0.5,
    )

    print(response.choices[0].text.strip())