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


class PluginInterfaceType(object):
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
        'capability': 'str',
        'prefix': 'str',
        'version': 'str'
    }

    attribute_map = {
        'capability': 'Capability',
        'prefix': 'Prefix',
        'version': 'Version'
    }

    def __init__(self, capability=None, prefix=None, version=None, local_vars_configuration=None):  # noqa: E501
        """PluginInterfaceType - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._capability = None
        self._prefix = None
        self._version = None
        self.discriminator = None

        self.capability = capability
        self.prefix = prefix
        self.version = version

    @property
    def capability(self):
        """Gets the capability of this PluginInterfaceType.  # noqa: E501

        capability  # noqa: E501

        :return: The capability of this PluginInterfaceType.  # noqa: E501
        :rtype: str
        """
        return self._capability

    @capability.setter
    def capability(self, capability):
        """Sets the capability of this PluginInterfaceType.

        capability  # noqa: E501

        :param capability: The capability of this PluginInterfaceType.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and capability is None:  # noqa: E501
            raise ValueError("Invalid value for `capability`, must not be `None`")  # noqa: E501

        self._capability = capability

    @property
    def prefix(self):
        """Gets the prefix of this PluginInterfaceType.  # noqa: E501

        prefix  # noqa: E501

        :return: The prefix of this PluginInterfaceType.  # noqa: E501
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this PluginInterfaceType.

        prefix  # noqa: E501

        :param prefix: The prefix of this PluginInterfaceType.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and prefix is None:  # noqa: E501
            raise ValueError("Invalid value for `prefix`, must not be `None`")  # noqa: E501

        self._prefix = prefix

    @property
    def version(self):
        """Gets the version of this PluginInterfaceType.  # noqa: E501

        version  # noqa: E501

        :return: The version of this PluginInterfaceType.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PluginInterfaceType.

        version  # noqa: E501

        :param version: The version of this PluginInterfaceType.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and version is None:  # noqa: E501
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

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
        if not isinstance(other, PluginInterfaceType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PluginInterfaceType):
            return True

        return self.to_dict() != other.to_dict()