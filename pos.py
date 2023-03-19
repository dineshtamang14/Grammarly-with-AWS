import boto3


text = []
pos = []

def detect_pos(input: str) -> dict:
    comprehend = boto3.client(service_name="comprehend", region_name="us-east-1")
    result = comprehend.detect_syntax(Text=input, LanguageCode="en")
    
    for i in result["SyntaxTokens"]:
        text.append(i["Text"])
        pos.append(i["PartOfSpeech"])
        
    pos_dict = dict(zip(text, pos))
    return pos_dict