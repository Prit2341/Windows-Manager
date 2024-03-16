import PyPDF2
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from heapq import nlargest

def read_pdf(file_path):
    text = ""
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
    return text

def summarize(text, num_sentences=3):
    sentences = sent_tokenize(text)
    words = [word for word in text.split() if word.lower() not in stopwords.words('english')]
    frequency = FreqDist(words)
    ranking = {}
    for i, sentence in enumerate(sentences):
        ranking[i] = 0
        for word in sentence.split():
            if word.lower() in frequency:
                ranking[i] += frequency[word.lower()]
    indexes = nlargest(num_sentences, ranking, key=ranking.get)
    summarized_sentences = [sentences[j] for j in sorted(indexes)]
    return " ".join(summarized_sentences).replace("\n", " ")

def summarize_pdf(file_path, num_sentences=3):
    pdf_text = read_pdf(file_path)
    summarized_text = summarize(pdf_text, num_sentences)
    return summarized_text
