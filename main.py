import pyttsx3, PyPDF2

pdfreader = PyPDF2.PdfReader(open("/home/hexie/projects/pdf2audiobook/books/id.pdf", "rb"))
speaker = pyttsx3.init()

for page_num in range(len(pdfreader.pages)):
    page = pdfreader.pages[page_num].extract_text()
    text = page.strip().replace('\n', ' ')    
speaker.save_to_file(text, "output.mp3")
speaker.runAndWait()

speaker.stop()