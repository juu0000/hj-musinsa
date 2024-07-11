import boto3
import os
from datetime import datetime, timedelta, timezone

def get_old_iam(n_hours):
    iam = boto3.client(
        'iam', 
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
        )
    users = iam.list_users()['Users']
    old_users = []

    threshold_time = datetime.now(timezone.utc) - timedelta(hours=n_hours)

    for user in users:
        user_name = user['UserName']
        access_keys = iam.list_access_keys(UserName=user_name)['AccessKeyMetadata']
        
        for key in access_keys:
            create_date = key['CreateDate']
            if create_date < threshold_time:
                old_users.append({
                    'UserID': user['UserId'],
                    'AccessKeyID': key['AccessKeyId']
                })
    
    return old_users
