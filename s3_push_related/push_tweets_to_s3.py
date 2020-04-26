from airflow.hooks.S3_hook import S3Hook
import boto3
from airflow.models import Variable
def push_tweets_to_s3():
        #var.json.adfs.key   # If it is defined as Json i nth below format in the variable UI / CLI:
        # another_var      { "v_command": "ls /var/log", "v_some_var": "HELLO FROM CLI" }
        #access_key=var.value.access_key
        #secret_key=var.value.secret_key
        ACCESS_KEY=Variable.get("Access_Key")
        SECRET_KEY=Variable.get("Secret_key")
        local_file='/Users/anandkumar.r/airflow/dags/tweets.json'
        s3_file='tweets.json'
        bucket_name='tweets-bucket-airflow-raw'
        def upload_to_aws(local_file, bucket, s3_file):
            s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                            aws_secret_access_key=SECRET_KEY)

            try:
                s3.upload_file(local_file, bucket, s3_file)
                print("Upload Successful")
                return True
            except FileNotFoundError:
                print("The file was not found")
                return False
            #except NoCredentialsError:
            else :
                print("Credentials not available")
                return False

            return "Uploaded Successfully"
        uploaded = upload_to_aws(local_file, bucket_name, s3_file)
        
push_tweets_to_s3()