"""
    Ory Oathkeeper API

    Documentation for all of Ory Oathkeeper's APIs.   # noqa: E501

    The version of the OpenAPI document: v1.11.4
    Contact: hi@ory.sh
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import ory_hydra_client
from ory_hydra_client.model.o_auth2_client import OAuth2Client
from ory_hydra_client.model.open_id_connect_context import OpenIDConnectContext
from ory_hydra_client.model.string_slice_pipe_delimiter import StringSlicePipeDelimiter
globals()['OAuth2Client'] = OAuth2Client
globals()['OpenIDConnectContext'] = OpenIDConnectContext
globals()['StringSlicePipeDelimiter'] = StringSlicePipeDelimiter
from ory_hydra_client.model.login_request import LoginRequest


class TestLoginRequest(unittest.TestCase):
    """LoginRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLoginRequest(self):
        """Test LoginRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LoginRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
