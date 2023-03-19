import boto3


text = []
type = []

def detect_entity(input: str) -> dict:
    comprehend = boto3.client(service_name="comprehend", region_name="us-east-1")
    result = comprehend.detect_entities(Text=input, LanguageCode="en")
    
    for i in result["Entities"]:
        text.append(i["Text"])
        type.append(i["Type"])
    
    entity_dict = dict(zip(text, type))
    return entity_dict
    
print(detect_entity("i hate you"))