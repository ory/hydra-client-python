"""
    Ory Oathkeeper API

    Documentation for all of Ory Oathkeeper's APIs.   # noqa: E501

    The version of the OpenAPI document: v1.11.5
    Contact: hi@ory.sh
    Generated by: https://openapi-generator.tech
"""


import unittest

import ory_hydra_client
from ory_hydra_client.api.public_api import PublicApi  # noqa: E501


class TestPublicApi(unittest.TestCase):
    """PublicApi unit test stubs"""

    def setUp(self):
        self.api = PublicApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_disconnect_user(self):
        """Test case for disconnect_user

        OpenID Connect Front-Backchannel Enabled Logout  # noqa: E501
        """
        pass

    def test_discover_open_id_configuration(self):
        """Test case for discover_open_id_configuration

        OpenID Connect Discovery  # noqa: E501
        """
        pass

    def test_dynamic_client_registration_create_o_auth2_client(self):
        """Test case for dynamic_client_registration_create_o_auth2_client

        Register an OAuth 2.0 Client using the OpenID / OAuth2 Dynamic Client Registration Management Protocol  # noqa: E501
        """
        pass

    def test_dynamic_client_registration_delete_o_auth2_client(self):
        """Test case for dynamic_client_registration_delete_o_auth2_client

        Deletes an OAuth 2.0 Client using the OpenID / OAuth2 Dynamic Client Registration Management Protocol  # noqa: E501
        """
        pass

    def test_dynamic_client_registration_get_o_auth2_client(self):
        """Test case for dynamic_client_registration_get_o_auth2_client

        Get an OAuth 2.0 Client using the OpenID / OAuth2 Dynamic Client Registration Management Protocol  # noqa: E501
        """
        pass

    def test_dynamic_client_registration_update_o_auth2_client(self):
        """Test case for dynamic_client_registration_update_o_auth2_client

        Update an OAuth 2.0 Client using the OpenID / OAuth2 Dynamic Client Registration Management Protocol  # noqa: E501
        """
        pass

    def test_oauth2_token(self):
        """Test case for oauth2_token

        The OAuth 2.0 Token Endpoint  # noqa: E501
        """
        pass

    def test_oauth_auth(self):
        """Test case for oauth_auth

        The OAuth 2.0 Authorize Endpoint  # noqa: E501
        """
        pass

    def test_revoke_o_auth2_token(self):
        """Test case for revoke_o_auth2_token

        Revoke OAuth2 Tokens  # noqa: E501
        """
        pass

    def test_userinfo(self):
        """Test case for userinfo

        OpenID Connect Userinfo  # noqa: E501
        """
        pass

    def test_well_known(self):
        """Test case for well_known

        JSON Web Keys Discovery  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
