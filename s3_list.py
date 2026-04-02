import boto3

s3 = boto3.client("s3")
response = s3.list_buckets()
print("My Buckets: S3:\n")
for bucket in response["Buckets"]:
  print(f" 🪣 {bucket['Name']} - created at {bucket['CreationDate'].strftime('%Y-%m-%d')}")