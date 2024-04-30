# CloudFormation
aws cloudformation package --template-file user_group_template.yml --s3-bucket aws-course-rd --output-template-file user_group_template.packaged.yml
aws cloudformation deploy --template-file user_group_template.packaged.yml --stack-name UserGroupStack --capabilities=CAPABILITY_NAMED_IAM

# SAM
sam init
sam build
sam deploy --guided
sam deploy --stack-name=test-lambda --s3-bucket=aws-course-rd --capabilities=CAPABILITY_IAM

sam local invoke "ReadCsvFileFunction" -e event.json


Properties:
https://github.com/aws/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction