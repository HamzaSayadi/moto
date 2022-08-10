from students import update_student_passed_status
from moto import mock_s3
import boto3


def test_student(db_setup):
    # given
    resource = boto3.resource('dynamodb')

    # when
    update_student_passed_status('1', [10, 12, 13], resource)

    # then
    table = resource.Table('workshop-users')
    item = table.get_item(Key={'UserId': '1'})
    assert item['Item']['passed'] == True

    # when
    update_student_passed_status('1', [7, 3, 0], resource)

    # then
    table = resource.Table('workshop-users')
    item = table.get_item(Key={'UserId': '1'})
    assert item['Item']['passed'] == False
