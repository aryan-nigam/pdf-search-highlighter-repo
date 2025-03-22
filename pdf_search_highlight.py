import os
import fitz  # PyMuPDF
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss

# Initialize model and directory
model = SentenceTransformer('all-MiniLM-L6-v2')
pdf_directory = './pdfs'

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = []
    for page in doc:
        text.append(page.get_text())
    return text

def create_embeddings(texts):
    embeddings = model.encode(texts)
    return embeddings

def build_index():
    texts = []
    pdf_map = []
    for root, _, files in os.walk(pdf_directory):
        for file in files:
            if file.endswith('.pdf'):
                pdf_path = os.path.join(root, file)
                extracted_texts = extract_text_from_pdf(pdf_path)
                texts.extend(extracted_texts)
                pdf_map.extend([(pdf_path, i) for i in range(len(extracted_texts))])
    
    embeddings = create_embeddings(texts)
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))
    return index, texts, pdf_map

def search_and_highlight(question):
    index, texts, pdf_map = build_index()
    query_embedding = model.encode([question])
    distances, indices = index.search(np.array(query_embedding), 1)
    
    best_index = indices[0][0]
    pdf_path, page_number = pdf_map[best_index]
    best_text = texts[best_index]
    
    print(f"Match found in: {pdf_path}, Page: {page_number + 1}")
    
    doc = fitz.open(pdf_path)
    page = doc[page_number]
    words = question.split()
    
    for word in words:
        areas = page.search_for(word)
        for area in areas:
            page.draw_rect(area, color=(1, 1, 0), fill_opacity=0.3)

    output_path = pdf_path.replace('.pdf', '_highlighted.pdf')
    doc.save(output_path)
    doc.close()
    print(f"Highlighted PDF saved to {output_path}")

if __name__ == "__main__":
    user_question = input("Enter your question: ")
    search_and_highlight(user_question)
