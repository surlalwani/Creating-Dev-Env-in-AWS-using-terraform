import json

def lambda_handler(event, context):
    for k,v in event.items();
    print(k,v)
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }