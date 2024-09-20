#this should download the data from s3 and load it into sql database
import pandas as pd
from sqlalchemy import create_engine
import boto3
import os 

def downloadFromS3(bucket, objectName, localFile):
    s3Client = boto3.client('s3')
    try: 
        