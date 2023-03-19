import boto3


def do_translate(input):
    translate = boto3.client(service_name="translate", region_name="us-east-1",use_ssl=True)
    result = translate.translate_text(Text=input, SourceLanguageCode="en", TargetLanguageCode="es")
    return result.get("TranslatedText")
