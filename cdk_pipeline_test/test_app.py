#!/usr/bin/env python3

import aws_cdk as cdk
from cdk_pipeline_test.cdk_pipeline_test_stack import CdkPipelineTestStack


app = cdk.App()
CdkPipelineTestStack(app, "CdkPipelineTestStack",
    env=cdk.Environment(account='111111111111', region='us-central-1'),
    )

app.synth()

