import boto3
import os


def main():
    print("Hello")


def build_config():
    # read secret
    client = boto3.client('secretsmanager')
    response = client.get_secret_value(
        SecretId='database_secre'
    )
    # read from env variables
    database_url = os.environ["database_url"]
    # return config
    return {
        "database_secret": response["SecretString"],
        "database_url": database_url
    }


if __name__ == "__main__":
    main()
