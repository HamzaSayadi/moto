import pytest
import mock
import boto3
from moto import mock_dynamodb2
import os


@pytest.fixture(scope='session')
def aws_credentials():
    """Mock AWS Credentials for moto."""
    os.environ['AWS_ACCESS_KEY_ID'] = 'testing'
    os.environ['AWS_SECRET_ACCESS_KEY'] = 'testing'
    os.environ['AWS_SECURITY_TOKEN'] = 'testing'
    os.environ['AWS_SESSION_TOKEN'] = 'testing'


@pytest.fixture(scope='function')
def mock_config():
    """Mock AWS DynamoDB using moto."""
    os.environ['database_url'] = 'test_url'
