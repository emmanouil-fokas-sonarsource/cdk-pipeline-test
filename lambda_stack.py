import aws_cdk as cdk
from constructs import Construct
from aws_cdk.aws_lambda import Function, InlineCode, Runtime


class LambdaStack(cdk.Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        Function(self, "LambdaFunction",
                 runtime=Runtime.PYTHON_3_12,
                 handler="index.handler",
                 code=InlineCode("exports.handler = _ => 'CDK Pipelines POC';")
                 )
