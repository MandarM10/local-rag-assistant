import pypdf
import re
from pathlib import Path

class PdfReader:
    PDF_PATH = Path(__file__).parent / "pdfs" / "BIG DATA FUNDAMENTALS.pdf"     #Example: Used for testing, PDF path, can change it to your own PDF file path
    # initializing our pdf reader class
    def __init__(self, path=PDF_PATH):
        
        try:
            self.reader = pypdf.PdfReader(str(path))
        except FileNotFoundError:
            raise FileNotFoundError(f"PDF not found: {path}")
        except Exception as e:
            raise RuntimeError(f"Failed to load PDF: {e}")
        self.pages_text = ""         #Returs text of whole pages

    # extracting from pdf to text
    def extract_text(self):
        all_pages_text= []      #extracting the pages of the pdf into a string 
        for _,page in enumerate(self.reader.pages):
            page_text = page.extract_text()
            if page_text:
                all_pages_text.append(page_text)        # Only add if text extraction was successful

        # Join the text from all pages and normalize whitespace
        pdf_text = "\n".join(all_pages_text)
        pdf_text = re.sub(r'\n([ \t]*\n)?[ \t]{2,}', '¶', pdf_text)     # 1. mark paragraph breaks BEFORE space normalization
        pdf_text = re.sub(r' +', ' ', pdf_text)                         # 2. collapse multiple spaces
        pdf_text = re.sub(r'[ \t]*\n[ \t]*', ' ', pdf_text)             # 3. collapse word-wrap newlines → space
        pdf_text = pdf_text.replace('¶', '\n')                          # 4. restore paragraph breaks as \n
        pdf_text = re.sub(r' +', ' ', pdf_text).strip()                 # 5. final space cleanup
        print(f"Successfully extracted text. Total characters: {len(pdf_text)}")
        self.pages_text = pdf_text
        return pdf_text
            

    def extract_small_portion_of_the_pdf(self, min=0, max=None):    #showing a portion of the book to allow the user to see what it looks like
        if self.pages_text == "":
            self.extract_text()
        return self.pages_text[min:max]
    

    def get_paragraphs(self):            #returns a list of paragraphs extracted from the pdf text. 
        if self.pages_text == "":       # Call extract_text() first before using this method.
            self.extract_text()
        return [p.strip() for p in self.pages_text.split('\n') if p.strip()]

        


### testing
#pdf_reader = PdfReader()
#pdf_reader.extract_text()
#print(pdf_reader.extract_small_portion_of_the_pdf(min=0, max=100))  # Display the first 500 characters of the extracted text
#print(pdf_reader.get_paragraphs()[:3])  # Display the first 3 paragraphs of the extracted text