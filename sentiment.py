import boto3


def do_sentiment_analysis(input):
    comprehend = boto3.client(service_name="comprehend", region_name="us-east-1")
    result = comprehend.detect_sentiment(Text=input, LanguageCode="en")

    positive = round(((result["SentimentScore"]["Positive"]*100)))
    negative = round((result["SentimentScore"]["Negative"]*100))
    neutral = round((result["SentimentScore"]["Neutral"]*100))
    
    list = [positive, negative, neutral]
    
    return list