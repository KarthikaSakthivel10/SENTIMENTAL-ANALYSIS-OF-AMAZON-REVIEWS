import pandas as pd
from textblob import TextBlob

df = pd.read_csv('/home/karthika/Downloads/amazon.csv')
# print(df.columns)
def analyze_sentiment(text):
    analysis = TextBlob(text)

    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

df['Sentiment'] = df['Review_Text'].apply(analyze_sentiment)

df.to_csv('amazon_reviews.csv', index=False)

print("Sentiment analysis completed. Results saved to 'amazon_reviews.csv'.")
