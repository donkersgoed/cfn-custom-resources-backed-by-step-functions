#!/usr/bin/env python3
"""The main app. Contains all the stacks."""

# Standard library imports
# -

# Related third party imports
# -

# Local application/library specific imports
from aws_cdk import core as cdk
from config import Config
from cfn_custom_resources_backed_by_step_functions.cfn_custom_resources_backed_by_step_functions_stack import (  # pylint: disable=line-too-long
    CfnCustomResourcesBackedByStepFunctionsStack,
)

config = Config()

app = cdk.App()
CfnCustomResourcesBackedByStepFunctionsStack(
    scope=app,
    construct_id="CfnCustomResourcesBackedByStepFunctionsStack",
    config=config.base(),
)

app.synth()
