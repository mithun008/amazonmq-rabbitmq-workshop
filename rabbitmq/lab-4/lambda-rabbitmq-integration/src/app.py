import json
import logging as log
import base64
def lambda_handler(event, context):
    for queue in event["rmqMessagesByQueue"]:
        for message in event['rmqMessagesByQueue'][queue]:
            plainMessageBody  = base64.b64decode(message['data']).decode("utf-8")
            print(context.function_name, " received - ", plainMessageBody)
    return {
        'statusCode': 200,
        'body': json.dumps('Recieved messages from RabbitMQ broker')
    }