# coding: utf-8

"""
    ORY Hydra

    Welcome to the ORY Hydra HTTP API documentation. You will find documentation for all HTTP APIs here.  # noqa: E501

    The version of the OpenAPI document: v1.9.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ory_hydra_client.configuration import Configuration


class CompletedRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'redirect_to': 'str'
    }

    attribute_map = {
        'redirect_to': 'redirect_to'
    }

    def __init__(self, redirect_to=None, local_vars_configuration=None):  # noqa: E501
        """CompletedRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._redirect_to = None
        self.discriminator = None

        self.redirect_to = redirect_to

    @property
    def redirect_to(self):
        """Gets the redirect_to of this CompletedRequest.  # noqa: E501

        RedirectURL is the URL which you should redirect the user to once the authentication process is completed.  # noqa: E501

        :return: The redirect_to of this CompletedRequest.  # noqa: E501
        :rtype: str
        """
        return self._redirect_to

    @redirect_to.setter
    def redirect_to(self, redirect_to):
        """Sets the redirect_to of this CompletedRequest.

        RedirectURL is the URL which you should redirect the user to once the authentication process is completed.  # noqa: E501

        :param redirect_to: The redirect_to of this CompletedRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and redirect_to is None:  # noqa: E501
            raise ValueError("Invalid value for `redirect_to`, must not be `None`")  # noqa: E501

        self._redirect_to = redirect_to

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CompletedRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CompletedRequest):
            return True

        return self.to_dict() != other.to_dict()