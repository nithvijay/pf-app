from aws_cdk import (
    # Duration,
    Stack,
    aws_dynamodb as dynamodb,
    aws_lambda as lambda_
)
from constructs import Construct


class BackendStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        table = dynamodb.Table(
            self,
            "Table",
            partition_key=dynamodb.Attribute(
                name="id", type=dynamodb.AttributeType.STRING
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
        )
        function = lambda_.Function(
            self, 
                                    "ApiHandler",
            code=lambda_.Code.from_asset("../backend/lambda/"),
            handler="handler.handler",
            runtime=lambda_.Runtime.PYTHON_3_10
        )

        table.grant_read_write_data(function)
        function.add_environment("TABLE_NAME", table.table_name)
