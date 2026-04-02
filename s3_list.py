import boto3

s3 = boto3.client("s3")
response = s3.list_buckets()

print("My Buckets: S3:\n")
for bucket in response["Buckets"]:
    name = bucket["Name"]
    date = bucket["CreationDate"].strftime('%Y-%m-%d')
    print(f" 🪣 {name} - created at {date}")
