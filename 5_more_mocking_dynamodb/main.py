import requests
import boto3
from students import update_student_passed_status


def main():
    resource = boto3.resource('dynamodb')
    buckets = update_student_passed_status('3', [10, 12, 13], resource)
    print(buckets)


if __name__ == "__main__":
    main()
