def update_student_passed_status(student_id, student_grades, dynamodb):
    table = dynamodb.Table('workshop-users')
    average_grades = sum(student_grades) / len(student_grades)
    student_passed = average_grades > 10
    response = table.update_item(
        Key={
            'UserId': student_id
        },
        UpdateExpression="set passed=:p",
        ExpressionAttributeValues={
            ':p': student_passed
        },
        ReturnValues="UPDATED_NEW"
    )
    return response
