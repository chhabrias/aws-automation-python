# coding: utf-8
new_bucket = s3.create_bucket(Bucket='automating-boto3')
new_bucket = s3.create_bucket(Bucket='automating-boto3', CreateBucketConfiguration={'LocationConstraint': 'us-east-1'})
aws s3 ls
for bucket in s3.buckets.all():
    print(bucket)
    
for bucket in s3.buckets.all():
    print(bucket)
    
s3 = session.resource('s3')
session = boto3.Session(profile_name='pythonAutomation')
import boto3
session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')
