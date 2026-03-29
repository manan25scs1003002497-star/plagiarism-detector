from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def check_plagiarism(text1, text2):
    documents = [text1, text2]
    
    tfidf = TfidfVectorizer().fit_transform(documents)
    similarity = cosine_similarity(tfidf[0:1], tfidf[1:2])
    
    return round(float(similarity[0][0]) * 100, 2)
