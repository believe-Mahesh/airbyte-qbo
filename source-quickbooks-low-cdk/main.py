#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from source_quickbooks_low_cdk import SourceQuickbooksLowCdk

if __name__ == "__main__":
    source = SourceQuickbooksLowCdk()
    launch(source, sys.argv[1:])
