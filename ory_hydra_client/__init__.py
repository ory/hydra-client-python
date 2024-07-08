# coding: utf-8

# flake8: noqa

"""
    Ory Hydra API

    Documentation for all of Ory Hydra's APIs. 

    The version of the OpenAPI document: v2.2.1
    Contact: hi@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "v2.2.1"

# import apis into sdk package
from ory_hydra_client.api.jwk_api import JwkApi
from ory_hydra_client.api.metadata_api import MetadataApi
from ory_hydra_client.api.o_auth2_api import OAuth2Api
from ory_hydra_client.api.oidc_api import OidcApi
from ory_hydra_client.api.wellknown_api import WellknownApi

# import ApiClient
from ory_hydra_client.api_response import ApiResponse
from ory_hydra_client.api_client import ApiClient
from ory_hydra_client.configuration import Configuration
from ory_hydra_client.exceptions import OpenApiException
from ory_hydra_client.exceptions import ApiTypeError
from ory_hydra_client.exceptions import ApiValueError
from ory_hydra_client.exceptions import ApiKeyError
from ory_hydra_client.exceptions import ApiAttributeError
from ory_hydra_client.exceptions import ApiException

# import models into sdk package
from ory_hydra_client.models.accept_o_auth2_consent_request import AcceptOAuth2ConsentRequest
from ory_hydra_client.models.accept_o_auth2_consent_request_session import AcceptOAuth2ConsentRequestSession
from ory_hydra_client.models.accept_o_auth2_login_request import AcceptOAuth2LoginRequest
from ory_hydra_client.models.create_json_web_key_set import CreateJsonWebKeySet
from ory_hydra_client.models.create_verifiable_credential_request_body import CreateVerifiableCredentialRequestBody
from ory_hydra_client.models.credential_supported_draft00 import CredentialSupportedDraft00
from ory_hydra_client.models.error_o_auth2 import ErrorOAuth2
from ory_hydra_client.models.generic_error import GenericError
from ory_hydra_client.models.get_version200_response import GetVersion200Response
from ory_hydra_client.models.health_not_ready_status import HealthNotReadyStatus
from ory_hydra_client.models.health_status import HealthStatus
from ory_hydra_client.models.introspected_o_auth2_token import IntrospectedOAuth2Token
from ory_hydra_client.models.is_ready200_response import IsReady200Response
from ory_hydra_client.models.is_ready503_response import IsReady503Response
from ory_hydra_client.models.json_patch import JsonPatch
from ory_hydra_client.models.json_web_key import JsonWebKey
from ory_hydra_client.models.json_web_key_set import JsonWebKeySet
from ory_hydra_client.models.o_auth2_client import OAuth2Client
from ory_hydra_client.models.o_auth2_client_token_lifespans import OAuth2ClientTokenLifespans
from ory_hydra_client.models.o_auth2_consent_request import OAuth2ConsentRequest
from ory_hydra_client.models.o_auth2_consent_request_open_id_connect_context import OAuth2ConsentRequestOpenIDConnectContext
from ory_hydra_client.models.o_auth2_consent_session import OAuth2ConsentSession
from ory_hydra_client.models.o_auth2_consent_session_expires_at import OAuth2ConsentSessionExpiresAt
from ory_hydra_client.models.o_auth2_login_request import OAuth2LoginRequest
from ory_hydra_client.models.o_auth2_logout_request import OAuth2LogoutRequest
from ory_hydra_client.models.o_auth2_redirect_to import OAuth2RedirectTo
from ory_hydra_client.models.o_auth2_token_exchange import OAuth2TokenExchange
from ory_hydra_client.models.oidc_configuration import OidcConfiguration
from ory_hydra_client.models.oidc_user_info import OidcUserInfo
from ory_hydra_client.models.pagination import Pagination
from ory_hydra_client.models.pagination_headers import PaginationHeaders
from ory_hydra_client.models.rfc6749_error_json import RFC6749ErrorJson
from ory_hydra_client.models.reject_o_auth2_request import RejectOAuth2Request
from ory_hydra_client.models.token_pagination import TokenPagination
from ory_hydra_client.models.token_pagination_headers import TokenPaginationHeaders
from ory_hydra_client.models.token_pagination_request_parameters import TokenPaginationRequestParameters
from ory_hydra_client.models.token_pagination_response_headers import TokenPaginationResponseHeaders
from ory_hydra_client.models.trust_o_auth2_jwt_grant_issuer import TrustOAuth2JwtGrantIssuer
from ory_hydra_client.models.trusted_o_auth2_jwt_grant_issuer import TrustedOAuth2JwtGrantIssuer
from ory_hydra_client.models.trusted_o_auth2_jwt_grant_json_web_key import TrustedOAuth2JwtGrantJsonWebKey
from ory_hydra_client.models.verifiable_credential_priming_response import VerifiableCredentialPrimingResponse
from ory_hydra_client.models.verifiable_credential_proof import VerifiableCredentialProof
from ory_hydra_client.models.verifiable_credential_response import VerifiableCredentialResponse
from ory_hydra_client.models.version import Version
