from textblob import TextBlob

def get_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment

if __name__ == "__main__":
    text = input("Enter text: ")
    sentiment = get_sentiment(text)
    print(f"Polarity: {sentiment.polarity}, Subjectivity: {sentiment.subjectivity}")
