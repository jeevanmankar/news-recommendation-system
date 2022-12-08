from nltk.tokenize import word_tokenize
import pandas as pd
from operator import itemgetter
import joblib
tfidf_news_model = joblib.load('tfidf_news_model_pkl')
lsi_news_model = joblib.load('lsi_news_model_pkl')
index = joblib.load('index_model_pkl')
dictionary = joblib.load('dictionary')
data_df = joblib.load('data_df_pkl')

def news_search(search_term):

    query_bow = dictionary.doc2bow(word_tokenize(search_term))
    query_tfidf = tfidf_news_model[query_bow]
    query_lsi = lsi_news_model[query_tfidf]

    index.num_best = 10

    news_list = index[query_lsi]

    news_list.sort(key=itemgetter(1), reverse=True)
    news = []

    for j, result in enumerate(news_list):

        news.append (      {
            'Relevance': round((result[1] * 100),2),
            'Title': data_df['headline'][result[0]],
            'Description': data_df['short_description'][result[0]],
            'Link' : data_df['links'][result[0]],
            'Keywords':data_df['keywords'][result[0]]

        } )

        if j == (index.num_best-1):
            break

    return pd.DataFrame(news, columns=['Relevance','Title','Description','Link','Keywords'])







