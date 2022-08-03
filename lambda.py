import json
import boto3
import logging
logger=logging.getLogger()
logger.setLevel(logging.INFO)
dynamodb=boto3.resource('dynamodb')
table=dynamodb.Table('students')

def lambda_handler(event, context):
    # TODO implement
    httpMethod=event['httpMethod']
    path = event['path']
    if  httpMethod == "GET" and path == "/students":
        response = table.scan()
        return {
            'statusCode': 200,
            'body': json.dumps(response["Items"])
        }
        
    elif httpMethod == "POST" and path == "/student":
        body = json.loads(event["body"])
        table.put_item(Item=body)
        return {
            'statusCode': 200,
            'body': json.dumps("success")
        }
