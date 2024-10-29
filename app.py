#!/usr/bin/env python3
import aws_cdk
from pipelinePOC import PipelinePOCStack

app = aws_cdk.App()
PipelinePOCStack(app, "CDKPipelinePOC",
    env=aws_cdk.Environment(account="111111111111", region="eu-central-1")
)

app.synth()
