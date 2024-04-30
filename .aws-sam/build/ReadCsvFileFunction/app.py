import boto3

print('Loading function')

s3 = boto3.client('s3')


def lambda_handler(event, context):
    try:
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']
        print(f"File: {key}")

        object = s3.get_object(Bucket=bucket, Key=key)
        print(object)
        content = object['Body'].read().decode("utf-8")

        content = content.split("\n")
        print(content)
        gpas = parse_content(content)

        average_gpa = calculate_average_gpa(gpas)

        print(f"Result: {average_gpa}")

        sns_client = boto3.client('sns')
        sns_client.publish(TopicArn='arn:aws:sns:eu-north-1:730335325860:NewFileOnS3', Message=f"Result: {average_gpa}")

        return {
            'statusCode': 200,
            'body': str(average_gpa)
        }
    except Exception as e:
        print(e)
        print(
            'Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(
                key, bucket))
        raise e


def parse_content(content):
    return [float(line.split(',')[1]) for line in content[1:] if line.strip() and not line.startswith("GPA")]


def calculate_average_gpa(gpas):
    if not gpas:
        return 0
    return sum(gpas) / len(gpas)
