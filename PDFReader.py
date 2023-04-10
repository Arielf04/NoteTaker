import pdfplumber
import openai

pdf_file_path = ''
api_key = ''

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

    return parsed_text

def call_chatgpt_api(prompt, max_response_tokens=500):
    openai.api_key = api_key

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=max_response_tokens,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return(response.choices[0].text.strip())

def split_string_into_chunks(input_string, chunk_size=3000):
    # Split the input string into tokens using whitespace as a delimiter
    tokens = input_string.split()

    # Initialize variables
    chunks = []
    current_chunk = []
    current_chunk_size = 0

    # Iterate through the tokens
    for token in tokens:
        # Add the current token length and 1 for the space character to the current chunk size
        token_size = len(token) + 1

        # If adding the current token to the current chunk would exceed the chunk_size, create a new chunk
        if current_chunk_size + token_size > chunk_size:
            # Join the tokens in the current chunk with a space character and add it to the list of chunks
            chunks.append(' '.join(current_chunk))

            # Reset the current chunk and its size
            current_chunk = [token]
            current_chunk_size = token_size
        else:
            # Otherwise, add the current token to the current chunk and update its size
            current_chunk.append(token)
            current_chunk_size += token_size

    # Add the last chunk to the list of chunks
    chunks.append(' '.join(current_chunk))

    return chunks

def take_notes(user_pages):
    results = ''
    parsed_text = parse_text_from_pdf(user_pages)
    parsed_text_as_chunks = split_string_into_chunks(parsed_text, chunk_size=3500)
    for chunk in parsed_text_as_chunks:
        prompt = "The following is text parsed from a university lecture slides. It migth include artifacts of the text not being parsed correctly, so extract the useful information first, then ummarize it in bullet points, return result in markdown format: " + chunk,
        temp_result = call_chatgpt_api(prompt)
        print("\nNew run: " + temp_result + "\n")
        results = results + temp_result

    results_as_chunks = split_string_into_chunks(results, chunk_size=3500)
    for chunk in results_as_chunks:
        prompt = "Take the following set of bullet points and summarize it further, leaving only the key information:\n" + results,
        temp_result = call_chatgpt_api(prompt, 256)
        print("\nNew run(summary): " + temp_result + "\n")
        results = results + temp_result
    print(results)
    

