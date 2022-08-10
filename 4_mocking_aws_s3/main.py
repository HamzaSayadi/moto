import requests
import boto3


def list_s3_buckets_with_prefix(prefix, client):
    buckets = []
    response = client.list_buckets()
    print(response)
    for bucket in response['Buckets']:
        if bucket['Name'].startswith(prefix):
            buckets.append(bucket['Name'])
    print(buckets)
    return buckets


def main():
    client = boto3.client('s3')
    buckets = list_s3_buckets_with_prefix('amplify', client)
    print(buckets)


if __name__ == "__main__":
    main()
