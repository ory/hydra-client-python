# coding: utf-8

"""
    Ory Hydra API

    Documentation for all of Ory Hydra's APIs. 

    The version of the OpenAPI document: v2.2.1
    Contact: hi@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ory_hydra_client.models.credential_supported_draft00 import CredentialSupportedDraft00
from typing import Optional, Set
from typing_extensions import Self

class OidcConfiguration(BaseModel):
    """
    Includes links to several endpoints (for example `/oauth2/token`) and exposes information on supported signature algorithms among others.
    """ # noqa: E501
    authorization_endpoint: StrictStr = Field(description="OAuth 2.0 Authorization Endpoint URL")
    backchannel_logout_session_supported: Optional[StrictBool] = Field(default=None, description="OpenID Connect Back-Channel Logout Session Required  Boolean value specifying whether the OP can pass a sid (session ID) Claim in the Logout Token to identify the RP session with the OP. If supported, the sid Claim is also included in ID Tokens issued by the OP")
    backchannel_logout_supported: Optional[StrictBool] = Field(default=None, description="OpenID Connect Back-Channel Logout Supported  Boolean value specifying whether the OP supports back-channel logout, with true indicating support.")
    claims_parameter_supported: Optional[StrictBool] = Field(default=None, description="OpenID Connect Claims Parameter Parameter Supported  Boolean value specifying whether the OP supports use of the claims parameter, with true indicating support.")
    claims_supported: Optional[List[StrictStr]] = Field(default=None, description="OpenID Connect Supported Claims  JSON array containing a list of the Claim Names of the Claims that the OpenID Provider MAY be able to supply values for. Note that for privacy or other reasons, this might not be an exhaustive list.")
    code_challenge_methods_supported: Optional[List[StrictStr]] = Field(default=None, description="OAuth 2.0 PKCE Supported Code Challenge Methods  JSON array containing a list of Proof Key for Code Exchange (PKCE) [RFC7636] code challenge methods supported by this authorization server.")
    credentials_endpoint_draft_00: Optional[StrictStr] = Field(default=None, description="OpenID Connect Verifiable Credentials Endpoint  Contains the URL of the Verifiable Credentials Endpoint.")
    credentials_supported_draft_00: Optional[List[CredentialSupportedDraft00]] = Field(default=None, description="OpenID Connect Verifiable Credentials Supported  JSON array containing a list of the Verifiable Credentials supported by this authorization server.")
    end_session_endpoint: Optional[StrictStr] = Field(default=None, description="OpenID Connect End-Session Endpoint  URL at the OP to which an RP can perform a redirect to request that the End-User be logged out at the OP.")
    frontchannel_logout_session_supported: Optional[StrictBool] = Field(default=None, description="OpenID Connect Front-Channel Logout Session Required  Boolean value specifying whether the OP can pass iss (issuer) and sid (session ID) query parameters to identify the RP session with the OP when the frontchannel_logout_uri is used. If supported, the sid Claim is also included in ID Tokens issued by the OP.")
    frontchannel_logout_supported: Optional[StrictBool] = Field(default=None, description="OpenID Connect Front-Channel Logout Supported  Boolean value specifying whether the OP supports HTTP-based logout, with true indicating support.")
    grant_types_supported: Optional[List[StrictStr]] = Field(default=None, description="OAuth 2.0 Supported Grant Types  JSON array containing a list of the OAuth 2.0 Grant Type values that this OP supports.")
    id_token_signed_response_alg: List[StrictStr] = Field(description="OpenID Connect Default ID Token Signing Algorithms  Algorithm used to sign OpenID Connect ID Tokens.")
    id_token_signing_alg_values_supported: List[StrictStr] = Field(description="OpenID Connect Supported ID Token Signing Algorithms  JSON array containing a list of the JWS signing algorithms (alg values) supported by the OP for the ID Token to encode the Claims in a JWT.")
    issuer: StrictStr = Field(description="OpenID Connect Issuer URL  An URL using the https scheme with no query or fragment component that the OP asserts as its IssuerURL Identifier. If IssuerURL discovery is supported , this value MUST be identical to the issuer value returned by WebFinger. This also MUST be identical to the iss Claim value in ID Tokens issued from this IssuerURL.")
    jwks_uri: StrictStr = Field(description="OpenID Connect Well-Known JSON Web Keys URL  URL of the OP's JSON Web Key Set [JWK] document. This contains the signing key(s) the RP uses to validate signatures from the OP. The JWK Set MAY also contain the Server's encryption key(s), which are used by RPs to encrypt requests to the Server. When both signing and encryption keys are made available, a use (Key Use) parameter value is REQUIRED for all keys in the referenced JWK Set to indicate each key's intended usage. Although some algorithms allow the same key to be used for both signatures and encryption, doing so is NOT RECOMMENDED, as it is less secure. The JWK x5c parameter MAY be used to provide X.509 representations of keys provided. When used, the bare key values MUST still be present and MUST match those in the certificate.")
    registration_endpoint: Optional[StrictStr] = Field(default=None, description="OpenID Connect Dynamic Client Registration Endpoint URL")
    request_object_signing_alg_values_supported: Optional[List[StrictStr]] = Field(default=None, description="OpenID Connect Supported Request Object Signing Algorithms  JSON array containing a list of the JWS signing algorithms (alg values) supported by the OP for Request Objects, which are described in Section 6.1 of OpenID Connect Core 1.0 [OpenID.Core]. These algorithms are used both when the Request Object is passed by value (using the request parameter) and when it is passed by reference (using the request_uri parameter).")
    request_parameter_supported: Optional[StrictBool] = Field(default=None, description="OpenID Connect Request Parameter Supported  Boolean value specifying whether the OP supports use of the request parameter, with true indicating support.")
    request_uri_parameter_supported: Optional[StrictBool] = Field(default=None, description="OpenID Connect Request URI Parameter Supported  Boolean value specifying whether the OP supports use of the request_uri parameter, with true indicating support.")
    require_request_uri_registration: Optional[StrictBool] = Field(default=None, description="OpenID Connect Requires Request URI Registration  Boolean value specifying whether the OP requires any request_uri values used to be pre-registered using the request_uris registration parameter.")
    response_modes_supported: Optional[List[StrictStr]] = Field(default=None, description="OAuth 2.0 Supported Response Modes  JSON array containing a list of the OAuth 2.0 response_mode values that this OP supports.")
    response_types_supported: List[StrictStr] = Field(description="OAuth 2.0 Supported Response Types  JSON array containing a list of the OAuth 2.0 response_type values that this OP supports. Dynamic OpenID Providers MUST support the code, id_token, and the token id_token Response Type values.")
    revocation_endpoint: Optional[StrictStr] = Field(default=None, description="OAuth 2.0 Token Revocation URL  URL of the authorization server's OAuth 2.0 revocation endpoint.")
    scopes_supported: Optional[List[StrictStr]] = Field(default=None, description="OAuth 2.0 Supported Scope Values  JSON array containing a list of the OAuth 2.0 [RFC6749] scope values that this server supports. The server MUST support the openid scope value. Servers MAY choose not to advertise some supported scope values even when this parameter is used")
    subject_types_supported: List[StrictStr] = Field(description="OpenID Connect Supported Subject Types  JSON array containing a list of the Subject Identifier types that this OP supports. Valid types include pairwise and public.")
    token_endpoint: StrictStr = Field(description="OAuth 2.0 Token Endpoint URL")
    token_endpoint_auth_methods_supported: Optional[List[StrictStr]] = Field(default=None, description="OAuth 2.0 Supported Client Authentication Methods  JSON array containing a list of Client Authentication methods supported by this Token Endpoint. The options are client_secret_post, client_secret_basic, client_secret_jwt, and private_key_jwt, as described in Section 9 of OpenID Connect Core 1.0")
    userinfo_endpoint: Optional[StrictStr] = Field(default=None, description="OpenID Connect Userinfo URL  URL of the OP's UserInfo Endpoint.")
    userinfo_signed_response_alg: List[StrictStr] = Field(description="OpenID Connect User Userinfo Signing Algorithm  Algorithm used to sign OpenID Connect Userinfo Responses.")
    userinfo_signing_alg_values_supported: Optional[List[StrictStr]] = Field(default=None, description="OpenID Connect Supported Userinfo Signing Algorithm  JSON array containing a list of the JWS [JWS] signing algorithms (alg values) [JWA] supported by the UserInfo Endpoint to encode the Claims in a JWT [JWT].")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["authorization_endpoint", "backchannel_logout_session_supported", "backchannel_logout_supported", "claims_parameter_supported", "claims_supported", "code_challenge_methods_supported", "credentials_endpoint_draft_00", "credentials_supported_draft_00", "end_session_endpoint", "frontchannel_logout_session_supported", "frontchannel_logout_supported", "grant_types_supported", "id_token_signed_response_alg", "id_token_signing_alg_values_supported", "issuer", "jwks_uri", "registration_endpoint", "request_object_signing_alg_values_supported", "request_parameter_supported", "request_uri_parameter_supported", "require_request_uri_registration", "response_modes_supported", "response_types_supported", "revocation_endpoint", "scopes_supported", "subject_types_supported", "token_endpoint", "token_endpoint_auth_methods_supported", "userinfo_endpoint", "userinfo_signed_response_alg", "userinfo_signing_alg_values_supported"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of OidcConfiguration from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in credentials_supported_draft_00 (list)
        _items = []
        if self.credentials_supported_draft_00:
            for _item in self.credentials_supported_draft_00:
                if _item:
                    _items.append(_item.to_dict())
            _dict['credentials_supported_draft_00'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OidcConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "authorization_endpoint": obj.get("authorization_endpoint"),
            "backchannel_logout_session_supported": obj.get("backchannel_logout_session_supported"),
            "backchannel_logout_supported": obj.get("backchannel_logout_supported"),
            "claims_parameter_supported": obj.get("claims_parameter_supported"),
            "claims_supported": obj.get("claims_supported"),
            "code_challenge_methods_supported": obj.get("code_challenge_methods_supported"),
            "credentials_endpoint_draft_00": obj.get("credentials_endpoint_draft_00"),
            "credentials_supported_draft_00": [CredentialSupportedDraft00.from_dict(_item) for _item in obj["credentials_supported_draft_00"]] if obj.get("credentials_supported_draft_00") is not None else None,
            "end_session_endpoint": obj.get("end_session_endpoint"),
            "frontchannel_logout_session_supported": obj.get("frontchannel_logout_session_supported"),
            "frontchannel_logout_supported": obj.get("frontchannel_logout_supported"),
            "grant_types_supported": obj.get("grant_types_supported"),
            "id_token_signed_response_alg": obj.get("id_token_signed_response_alg"),
            "id_token_signing_alg_values_supported": obj.get("id_token_signing_alg_values_supported"),
            "issuer": obj.get("issuer"),
            "jwks_uri": obj.get("jwks_uri"),
            "registration_endpoint": obj.get("registration_endpoint"),
            "request_object_signing_alg_values_supported": obj.get("request_object_signing_alg_values_supported"),
            "request_parameter_supported": obj.get("request_parameter_supported"),
            "request_uri_parameter_supported": obj.get("request_uri_parameter_supported"),
            "require_request_uri_registration": obj.get("require_request_uri_registration"),
            "response_modes_supported": obj.get("response_modes_supported"),
            "response_types_supported": obj.get("response_types_supported"),
            "revocation_endpoint": obj.get("revocation_endpoint"),
            "scopes_supported": obj.get("scopes_supported"),
            "subject_types_supported": obj.get("subject_types_supported"),
            "token_endpoint": obj.get("token_endpoint"),
            "token_endpoint_auth_methods_supported": obj.get("token_endpoint_auth_methods_supported"),
            "userinfo_endpoint": obj.get("userinfo_endpoint"),
            "userinfo_signed_response_alg": obj.get("userinfo_signed_response_alg"),
            "userinfo_signing_alg_values_supported": obj.get("userinfo_signing_alg_values_supported")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


