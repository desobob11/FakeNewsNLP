from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
import pandas as pd

def tf_idf_vectorize(df: pd.DataFrame, corpus: pd.Series[str]) -> pd.DataFrame
    stop_words = stopwords.words("english")
    vectorizer = TfidfVectorizer(strip_accents="ascii", lowercase=True, stop_words=stop_words, max_features=1000, min_df=50, ngram_range=(1,3))
    features = vectorizer.fit_transform(corpus).toarray()
    names = vectorizer.get_feature_names_out()
    headers = [f"__word{i}" for i in range(len(names))]
    feature_frame = pd.DataFrame(features, columns=headers)
    df = pd.concat([df, feature_frame], axis=1)
    return df