import pytest
import mock
import boto3
from moto import mock_dynamodb2


@pytest.fixture(scope='session')
def aws_credentials():
    """Mock AWS Credentials for moto."""
    os.environ['AWS_ACCESS_KEY_ID'] = 'testing'
    os.environ['AWS_SECRET_ACCESS_KEY'] = 'testing'
    os.environ['AWS_SECURITY_TOKEN'] = 'testing'
    os.environ['AWS_SESSION_TOKEN'] = 'testing'


@pytest.fixture(scope='function')
def dynamodb():
    """Mock AWS DynamoDB using moto."""
    with mock_dynamodb2():
        yield boto3.client("dynamodb", region_name="eu-west-1")


@pytest.fixture(scope='function')
def db_setup(dynamodb):
    """Mock Send notification function."""
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.create_table(
        TableName='workshop-users',
        KeySchema=[
            {
                'AttributeName': 'UserId',
                'KeyType': 'HASH'  # Partition key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'UserId',
                'AttributeType': 'S'
            }
        ])
    response = table.put_item(
        Item={
            'UserId': '1',
            'name': 'Bruce'
        }
    )
