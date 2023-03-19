from werkzeug.utils import secure_filename
import boto3


bucket_name = "bigprodcompany-builds"


def upload_file_s3(f):
    filename = secure_filename(f.filename)
    f.save(filename)
    
    boto_client = boto3.client("s3")
    boto_client.upload_file(filename, bucket_name, filename)
    return filename