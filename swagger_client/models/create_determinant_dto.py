# coding: utf-8

"""
    Api Documentation

    Api Documentation  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class CreateDeterminantDto(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'culture_id': 'int',
        'title': 'str',
        'user_id': 'int'
    }

    attribute_map = {
        'culture_id': 'cultureId',
        'title': 'title',
        'user_id': 'userId'
    }

    def __init__(self, culture_id=None, title=None, user_id=None, _configuration=None):  # noqa: E501
        """CreateDeterminantDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._culture_id = None
        self._title = None
        self._user_id = None
        self.discriminator = None

        if culture_id is not None:
            self.culture_id = culture_id
        if title is not None:
            self.title = title
        if user_id is not None:
            self.user_id = user_id

    @property
    def culture_id(self):
        """Gets the culture_id of this CreateDeterminantDto.  # noqa: E501


        :return: The culture_id of this CreateDeterminantDto.  # noqa: E501
        :rtype: int
        """
        return self._culture_id

    @culture_id.setter
    def culture_id(self, culture_id):
        """Sets the culture_id of this CreateDeterminantDto.


        :param culture_id: The culture_id of this CreateDeterminantDto.  # noqa: E501
        :type: int
        """

        self._culture_id = culture_id

    @property
    def title(self):
        """Gets the title of this CreateDeterminantDto.  # noqa: E501


        :return: The title of this CreateDeterminantDto.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this CreateDeterminantDto.


        :param title: The title of this CreateDeterminantDto.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def user_id(self):
        """Gets the user_id of this CreateDeterminantDto.  # noqa: E501


        :return: The user_id of this CreateDeterminantDto.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this CreateDeterminantDto.


        :param user_id: The user_id of this CreateDeterminantDto.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(CreateDeterminantDto, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateDeterminantDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateDeterminantDto):
            return True

        return self.to_dict() != other.to_dict()
