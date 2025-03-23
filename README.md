This project is a PDF Search and Highlight Tool powered by AI that helps you search for answers within PDF 
files using a natural language query. It highlights the relevant text and opens the PDF on the exact matching 
page in Google Chrome.

🚀 Features

1- Extracts text from PDFs using PyMuPDF

2- Generates embeddings using Sentence Transformers

3- Efficiently searches for the most relevant answer using FAISS

4- Highlights matching text in yellow

5- Opens the highlighted PDF directly on the correct page in Chrome

6-Prints "No match found" if no relevant text is detected

🧑‍💻 Technologies Used

1-Python for development

2-PyMuPDF for PDF processing

3-Sentence Transformers for text embeddings

4-FAISS for similarity search

5-NumPy for numerical computations

6-Google Chrome for PDF viewing

🛠️ Installation

1-Clone the repository:

git clone https://github.com/yourusername/pdf-search-highlight.git
cd pdf-search-highlight

2-Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3-Install dependencies:

pip install -r requirements.txt

4-Place your PDF files in the pdfs folder.

🚦 Usage

1-Run the script:

python pdf_search_highlight.py

2-Enter your question when prompted.

3-If a match is found, the PDF will be highlighted and opened in Google Chrome on the exact matching page.

4-If no match is found, it will print No match found.

📁 Project Structure

pdf-search-highlight/
├── pdf_search_highlight.py   # Main script
├── pdfs/                     # Folder to store PDF files
├── requirements.txt          # Required dependencies
└── README.md                 # Project documentation

🛡️ Requirements

1-Python 3.8+

2-Google Chrome installed

3-Internet connection for downloading SentenceTransformer models

✨ Example

Enter your question: What is artificial intelligence?
Match found in: pdfs/ai_basics.pdf, Page: 4
Highlighted PDF saved to pdfs/ai_basics_highlighted.pdf
