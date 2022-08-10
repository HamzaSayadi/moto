from main import list_s3_buckets_with_prefix
from moto import mock_s3
import boto3


@mock_s3
def test_list_s3_buckets_with_prefix():
    # given
    client = boto3.client('s3', region_name='us-east-1')

    client.create_bucket(Bucket='mybucket')
    client.create_bucket(Bucket='myotherbucket')
    client.create_bucket(Bucket='abucket')

    expected_result = ["mybucket", "myotherbucket"]

    # when
    buckets = list_s3_buckets_with_prefix("my", client)

    # then
    assert buckets == expected_result
