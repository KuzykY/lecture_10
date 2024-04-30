from aws_cdk import (
    aws_s3,
    aws_s3_notifications,
    core,
    aws_sns
)


class CdkExampleStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # create S3 bucket
        s3 = aws_s3.Bucket(self, "aws-course-rd-cdk")

        # define SNS topic ans assign it
        sns_topic = aws_sns.Topic(self, "CDK Notification")
        sns_notification = aws_s3_notifications.SnsDestination(sns_topic)

        # assign notification for the s3 event type when new object created
        s3.add_event_notification(aws_s3.EventType.OBJECT_CREATED, sns_notification)