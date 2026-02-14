from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(resume_text,jd_text):
    documents=[resume_text,jd_text]

    vectorizer =TfidfVectorizer(stop_words='english')
    tfidf=vectorizer.fit_transform(documents)

    similarity=cosine_similarity(tfidf[0:1],tfidf[1:2])
    return round(similarity[0][0]*100,2)

