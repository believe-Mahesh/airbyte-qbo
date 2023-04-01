#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from source_zoho_book_low_cdk import SourceZohoBookLowCdk

if __name__ == "__main__":
    source = SourceZohoBookLowCdk()
    launch(source, sys.argv[1:])
