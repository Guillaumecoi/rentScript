import pypdf
    
def read_pdf(file_path: str) -> str:
    with open(file_path, 'rb') as file:
        reader = pypdf.PdfReader(file)
        pages = []
        print(len(reader.pages))
        for page_num in range(len(reader.pages)):
            pages.append(reader.pages[page_num].extract_text())
    return pages