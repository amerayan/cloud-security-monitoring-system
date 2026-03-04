import boto3
from botocore.exceptions import NoCredentialsError

def check_failed_logins():
    try:
        cloudtrail = boto3.client('cloudtrail', region_name='ap-south-1')

        response = cloudtrail.lookup_events(
            LookupAttributes=[
                {
                    'AttributeKey': 'EventName',
                    'AttributeValue': 'ConsoleLogin'
                }
            ],
            MaxResults=10
        )

        print("Recent Login Events:\n")

        for event in response['Events']:
            print(f"User: {event.get('Username', 'Unknown')}")
            print(f"Time: {event['EventTime']}")
            print("-" * 40)

    except NoCredentialsError:
        print("AWS credentials not configured.")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    check_failed_logins()