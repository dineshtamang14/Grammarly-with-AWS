import boto3 


def text_to_speech(text: str):
    polly = boto3.client("polly")
    text = polly.synthesize_speech(Text=text, OutputFormat="mp3", VoiceId="Joanna")
    with open("output.mp3", "wb") as file:
        file.write(text["AudioStream"].read())
        file.close()
    # upload_audio()
    return True
        

# uploading audio file to s3 bucket
# def upload_audio():
#     bucket_name = "bigprodcompany-builds"       
#     boto_client = boto3.client("s3")
#     filename = "output.mp3"
#     boto_client.upload_file(filename, bucket_name, filename)