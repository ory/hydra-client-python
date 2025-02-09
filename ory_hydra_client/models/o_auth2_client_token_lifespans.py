# coding: utf-8

"""
    Ory Hydra API

    Documentation for all of Ory Hydra's APIs. 

    The version of the OpenAPI document: v2.4.0-alpha.1
    Contact: hi@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class OAuth2ClientTokenLifespans(BaseModel):
    """
    Lifespans of different token types issued for this OAuth 2.0 Client.
    """ # noqa: E501
    authorization_code_grant_access_token_lifespan: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Specify a time duration in milliseconds, seconds, minutes, hours.")
    authorization_code_grant_id_token_lifespan: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Specify a time duration in milliseconds, seconds, minutes, hours.")
    authorization_code_grant_refresh_token_lifespan: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Specify a time duration in milliseconds, seconds, minutes, hours.")
    client_credentials_grant_access_token_lifespan: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Specify a time duration in milliseconds, seconds, minutes, hours.")
    device_authorization_grant_access_token_lifespan: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Specify a time duration in milliseconds, seconds, minutes, hours.")
    device_authorization_grant_id_token_lifespan: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Specify a time duration in milliseconds, seconds, minutes, hours.")
    device_authorization_grant_refresh_token_lifespan: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Specify a time duration in milliseconds, seconds, minutes, hours.")
    implicit_grant_access_token_lifespan: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Specify a time duration in milliseconds, seconds, minutes, hours.")
    implicit_grant_id_token_lifespan: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Specify a time duration in milliseconds, seconds, minutes, hours.")
    jwt_bearer_grant_access_token_lifespan: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Specify a time duration in milliseconds, seconds, minutes, hours.")
    refresh_token_grant_access_token_lifespan: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Specify a time duration in milliseconds, seconds, minutes, hours.")
    refresh_token_grant_id_token_lifespan: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Specify a time duration in milliseconds, seconds, minutes, hours.")
    refresh_token_grant_refresh_token_lifespan: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Specify a time duration in milliseconds, seconds, minutes, hours.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["authorization_code_grant_access_token_lifespan", "authorization_code_grant_id_token_lifespan", "authorization_code_grant_refresh_token_lifespan", "client_credentials_grant_access_token_lifespan", "device_authorization_grant_access_token_lifespan", "device_authorization_grant_id_token_lifespan", "device_authorization_grant_refresh_token_lifespan", "implicit_grant_access_token_lifespan", "implicit_grant_id_token_lifespan", "jwt_bearer_grant_access_token_lifespan", "refresh_token_grant_access_token_lifespan", "refresh_token_grant_id_token_lifespan", "refresh_token_grant_refresh_token_lifespan"]

    @field_validator('authorization_code_grant_access_token_lifespan')
    def authorization_code_grant_access_token_lifespan_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^([0-9]+(ns|us|ms|s|m|h))*$", value):
            raise ValueError(r"must validate the regular expression /^([0-9]+(ns|us|ms|s|m|h))*$/")
        return value

    @field_validator('authorization_code_grant_id_token_lifespan')
    def authorization_code_grant_id_token_lifespan_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^([0-9]+(ns|us|ms|s|m|h))*$", value):
            raise ValueError(r"must validate the regular expression /^([0-9]+(ns|us|ms|s|m|h))*$/")
        return value

    @field_validator('authorization_code_grant_refresh_token_lifespan')
    def authorization_code_grant_refresh_token_lifespan_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^([0-9]+(ns|us|ms|s|m|h))*$", value):
            raise ValueError(r"must validate the regular expression /^([0-9]+(ns|us|ms|s|m|h))*$/")
        return value

    @field_validator('client_credentials_grant_access_token_lifespan')
    def client_credentials_grant_access_token_lifespan_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^([0-9]+(ns|us|ms|s|m|h))*$", value):
            raise ValueError(r"must validate the regular expression /^([0-9]+(ns|us|ms|s|m|h))*$/")
        return value

    @field_validator('device_authorization_grant_access_token_lifespan')
    def device_authorization_grant_access_token_lifespan_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^([0-9]+(ns|us|ms|s|m|h))*$", value):
            raise ValueError(r"must validate the regular expression /^([0-9]+(ns|us|ms|s|m|h))*$/")
        return value

    @field_validator('device_authorization_grant_id_token_lifespan')
    def device_authorization_grant_id_token_lifespan_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^([0-9]+(ns|us|ms|s|m|h))*$", value):
            raise ValueError(r"must validate the regular expression /^([0-9]+(ns|us|ms|s|m|h))*$/")
        return value

    @field_validator('device_authorization_grant_refresh_token_lifespan')
    def device_authorization_grant_refresh_token_lifespan_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^([0-9]+(ns|us|ms|s|m|h))*$", value):
            raise ValueError(r"must validate the regular expression /^([0-9]+(ns|us|ms|s|m|h))*$/")
        return value

    @field_validator('implicit_grant_access_token_lifespan')
    def implicit_grant_access_token_lifespan_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^([0-9]+(ns|us|ms|s|m|h))*$", value):
            raise ValueError(r"must validate the regular expression /^([0-9]+(ns|us|ms|s|m|h))*$/")
        return value

    @field_validator('implicit_grant_id_token_lifespan')
    def implicit_grant_id_token_lifespan_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^([0-9]+(ns|us|ms|s|m|h))*$", value):
            raise ValueError(r"must validate the regular expression /^([0-9]+(ns|us|ms|s|m|h))*$/")
        return value

    @field_validator('jwt_bearer_grant_access_token_lifespan')
    def jwt_bearer_grant_access_token_lifespan_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^([0-9]+(ns|us|ms|s|m|h))*$", value):
            raise ValueError(r"must validate the regular expression /^([0-9]+(ns|us|ms|s|m|h))*$/")
        return value

    @field_validator('refresh_token_grant_access_token_lifespan')
    def refresh_token_grant_access_token_lifespan_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^([0-9]+(ns|us|ms|s|m|h))*$", value):
            raise ValueError(r"must validate the regular expression /^([0-9]+(ns|us|ms|s|m|h))*$/")
        return value

    @field_validator('refresh_token_grant_id_token_lifespan')
    def refresh_token_grant_id_token_lifespan_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^([0-9]+(ns|us|ms|s|m|h))*$", value):
            raise ValueError(r"must validate the regular expression /^([0-9]+(ns|us|ms|s|m|h))*$/")
        return value

    @field_validator('refresh_token_grant_refresh_token_lifespan')
    def refresh_token_grant_refresh_token_lifespan_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^([0-9]+(ns|us|ms|s|m|h))*$", value):
            raise ValueError(r"must validate the regular expression /^([0-9]+(ns|us|ms|s|m|h))*$/")
        return value

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
        """Create an instance of OAuth2ClientTokenLifespans from a JSON string"""
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
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OAuth2ClientTokenLifespans from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "authorization_code_grant_access_token_lifespan": obj.get("authorization_code_grant_access_token_lifespan"),
            "authorization_code_grant_id_token_lifespan": obj.get("authorization_code_grant_id_token_lifespan"),
            "authorization_code_grant_refresh_token_lifespan": obj.get("authorization_code_grant_refresh_token_lifespan"),
            "client_credentials_grant_access_token_lifespan": obj.get("client_credentials_grant_access_token_lifespan"),
            "device_authorization_grant_access_token_lifespan": obj.get("device_authorization_grant_access_token_lifespan"),
            "device_authorization_grant_id_token_lifespan": obj.get("device_authorization_grant_id_token_lifespan"),
            "device_authorization_grant_refresh_token_lifespan": obj.get("device_authorization_grant_refresh_token_lifespan"),
            "implicit_grant_access_token_lifespan": obj.get("implicit_grant_access_token_lifespan"),
            "implicit_grant_id_token_lifespan": obj.get("implicit_grant_id_token_lifespan"),
            "jwt_bearer_grant_access_token_lifespan": obj.get("jwt_bearer_grant_access_token_lifespan"),
            "refresh_token_grant_access_token_lifespan": obj.get("refresh_token_grant_access_token_lifespan"),
            "refresh_token_grant_id_token_lifespan": obj.get("refresh_token_grant_id_token_lifespan"),
            "refresh_token_grant_refresh_token_lifespan": obj.get("refresh_token_grant_refresh_token_lifespan")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


