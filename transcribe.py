import boto3 
import time
import urllib
from urllib.request import urlopen
import json
import os



# ACCESS_KEY_ID = os.getenv("ACCESS_KEY_ID")
# SECRET_ACCESS_KEY = os.getenv("SECRET_ACCESS_KEY")


def do_transcribe(file_name):
    transcribe = boto3.client(service_name="transcribe", region_name="us-east-1")

    transcribe_job_name = "sample_transcribe_job"
    job_uri = 'https://s3.amazonaws.com/bigprodcompany-builds/' + file_name + ''

    transcribe.start_transcription_job(TranscriptionJobName=transcribe_job_name, Media={"MediaFileUri": job_uri}, MediaFormat="mp3", LanguageCode="en-US")

    time.sleep(30)
    output = transcribe.get_transcription_job(TranscriptionJobName=transcribe_job_name)
    url = output["TranscriptionJob"]["Transcript"]["TranscriptFileUri"]
    response = urlopen(url)
    data_json = json.loads(response.read())
    text = data_json["results"]["transcripts"][0]["transcript"]
    
    # deleting the transcribe job after work is done
    transcribe.delete_transcription_job(TranscriptionJobName=transcribe_job_name)
    # deleting file from s3 bucket
    s3 = boto3.client('s3')
    s3.delete_object(Bucket="bigprodcompany-builds", Key=file_name)
    return text