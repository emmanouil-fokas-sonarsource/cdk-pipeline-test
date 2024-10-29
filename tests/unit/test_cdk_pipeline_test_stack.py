import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_pipeline_test.cdk_pipeline_test_stack import CdkPipelineTestStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_pipeline_test/cdk_pipeline_test_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkPipelineTestStack(app, "cdk-pipeline-test")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
