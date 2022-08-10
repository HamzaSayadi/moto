from moto import mock_secretsmanager
import boto3
from main import build_config


@mock_secretsmanager
def test_build_config(mock_config):
    # given
    client = boto3.client('secretsmanager')
    client.create_secret(
        Name='database_secret',
        SecretString='test_string'
    )

    # when
    config = build_config()

    # then
    assert config["database_secret"] == 'test_string'
