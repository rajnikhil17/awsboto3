import boto3
dynamodb = boto3.client('dynamodb',region_name='us-east-1')

dynamodb.put_item(TableName='customerInfo', Item= {'Name': {'S':'AshokRajan'},'Phone Number': {'N':'+17034660228'}})