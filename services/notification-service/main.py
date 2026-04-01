import boto3
import json
import os
import time
from config import settings

def get_sqs_client():
    return boto3.client(
        'sqs',
        endpoint_url=settings.sqs_endpoint,
        region_name=settings.aws_region,
        aws_access_key_id='test',
        aws_secret_access_key='test'
    )

def get_ses_client():
    return boto3.client(
        'ses',
        endpoint_url=settings.ses_endpoint,
        region_name=settings.aws_region,
        aws_access_key_id='test',
        aws_secret_access_key='test'
    )

def save_email_to_file(to_email: str, subject: str, body: str):
    """Save email to /tmp/emails for local inspection instead of sending."""
    os.makedirs('/tmp/emails', exist_ok=True)
    filename = f"/tmp/emails/{int(time.time())}_{to_email.replace('@', '_')}.txt"
    with open(filename, 'w') as f:
        f.write(f"To: {to_email}\nSubject: {subject}\n\n{body}")
    print(f"Email saved to {filename}")

def process_message(message: dict):
    body = json.loads(message['Body'])
    # SNS wraps the message in another layer
    if 'Message' in body:
        order = json.loads(body['Message'])
    else:
        order = body

    order_id = order.get('order_id')
    user_email = order.get('user_email')
    total_amount = order.get('total_amount')
    items = order.get('items', [])

    items_text = "\n".join(
        f"  - Product {item['product_id']}: qty {item['quantity']} @ ${item['price']:.2f}"
        for item in items
    )
    subject = f"Order #{order_id} Confirmed"
    body_text = (
        f"Thank you for your order!\n\n"
        f"Order ID: {order_id}\n"
        f"Total: ${total_amount:.2f}\n\n"
        f"Items:\n{items_text}\n"
    )

    print(f"Processing order notification: order_id={order_id}, email={user_email}")
    save_email_to_file(user_email, subject, body_text)

def poll():
    sqs = get_sqs_client()
    print(f"Polling SQS queue: {settings.sqs_queue_url}")
    while True:
        try:
            response = sqs.receive_message(
                QueueUrl=settings.sqs_queue_url,
                MaxNumberOfMessages=10,
                WaitTimeSeconds=10
            )
            for msg in response.get('Messages', []):
                try:
                    process_message(msg)
                    sqs.delete_message(
                        QueueUrl=settings.sqs_queue_url,
                        ReceiptHandle=msg['ReceiptHandle']
                    )
                except Exception as e:
                    print(f"Error processing message: {e}")
        except Exception as e:
            print(f"Error polling SQS: {e}")
            time.sleep(5)

if __name__ == "__main__":
    poll()
