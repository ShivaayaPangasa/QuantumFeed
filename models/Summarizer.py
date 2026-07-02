import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD

def summarize_news(csv_path, top_n=5):
    # Step 1: Load and clean the CSV data
    df = pd.read_csv(csv_path)
    df.dropna(subset=['description'], inplace=True)

    # Step 2: TF-IDF Vectorization
    tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_df=0.8)
    tfidf_matrix = tfidf_vectorizer.fit_transform(df['description'])

    # Step 3: Latent Semantic Analysis (LSA)
    lsa_model = TruncatedSVD(n_components=1, random_state=42)
    lsa_topic_matrix = lsa_model.fit_transform(tfidf_matrix)

    # Step 4: Score & rank
    df['lsa_score'] = lsa_topic_matrix[:, 0]
    top_summaries = df.sort_values(by='lsa_score', ascending=False).head(top_n)

    # Step 5: Format output
    summaries = top_summaries[['title', 'description']].reset_index(drop=True)
    return summaries.to_dict('records')

# Example usage (backend integration)
summarized_news = summarize_news('bbcnews.csv')
print(summarized_news)
'''PS C:\Users\shiva\OneDrive\Documents\GitHub\QuantumFeed> & C:/Users/shiva/anaconda3/python.exe c:/Users/shiva/OneDrive/Documents/GitHub/QuantumFeed/Summarizer
[{'title': 'Cricket World Cup: England and Australia set for final',
'description': "England will attempt to win a second successive Women's World 
Cup when they face Australia in Sunday's final."}, {'title': "Spain v England: 
Key moments from the 2023 Fifa Women's World Cup", 'description': "England and 
Spain have both reached the Women's World Cup final for the first time. BBC 
Sport takes a look back at some of their key moments on the way."}, 
{'title': 'James scores as Chelsea beat Man City to reach League Cup final', 
'description': "Watch highlights as Chelsea beat Manchester City 1-0 to reach 
the Women's League Cup final against Arsenal."}, {'title': 'Rugby World Cup 
final: All you need to know as England face New Zealand', 'description': 
"Who, when, where - everything you need to know about Saturday's Rugby World 
Cup final between New Zealand and England."}, {'title': 'What next for England 
and Wiegman?', 'description': "England return from Australia following defeat
 in the Women's World Cup final - but what will they be looking ahead to now?"}]
PS C:\Users\shiva\OneDrive\Documents\GitHub\QuantumFeed>'''