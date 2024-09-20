import boto3
import subprocess
import os

def fetch_data():
    subprocess.run(['python3','src/fetch_data.py'])

def process_data():
    subprocess.run(['python3','src/process_data.py'])

def uploadToS3(fileName, bucket, objectName = None):
    s3Client = boto3.client('s3')
    if objectName is None:
        objectName = fileName
    
    try:
        s3Client.upload_file(fileName, bucket, objectName)
        print(f"uploaded {fileName} to {bucket}/{objectName}")
    except Exception as e:
        print(f"error uploading: {str(e)}")
    
def main():
    fetch_data()
    process_data()

    processedDataPath = os.path.join('data','processed','processed_sp500_data.csv')
    bucketName = 'market-index-data'
    uploadToS3(processedDataPath,bucketName)

if __name__ == '__main__':
    main()