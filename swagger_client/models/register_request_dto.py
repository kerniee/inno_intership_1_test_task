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


class RegisterRequestDto(object):
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
        'description': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'password': 'str',
        'phone': 'str',
        'region': 'str',
        'user_type': 'str',
        'username': 'str'
    }

    attribute_map = {
        'description': 'description',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'password': 'password',
        'phone': 'phone',
        'region': 'region',
        'user_type': 'userType',
        'username': 'username'
    }

    def __init__(self, description=None, first_name=None, last_name=None, password=None, phone=None, region=None, user_type=None, username=None, _configuration=None):  # noqa: E501
        """RegisterRequestDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._description = None
        self._first_name = None
        self._last_name = None
        self._password = None
        self._phone = None
        self._region = None
        self._user_type = None
        self._username = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if password is not None:
            self.password = password
        if phone is not None:
            self.phone = phone
        if region is not None:
            self.region = region
        if user_type is not None:
            self.user_type = user_type
        if username is not None:
            self.username = username

    @property
    def description(self):
        """Gets the description of this RegisterRequestDto.  # noqa: E501


        :return: The description of this RegisterRequestDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RegisterRequestDto.


        :param description: The description of this RegisterRequestDto.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def first_name(self):
        """Gets the first_name of this RegisterRequestDto.  # noqa: E501


        :return: The first_name of this RegisterRequestDto.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this RegisterRequestDto.


        :param first_name: The first_name of this RegisterRequestDto.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this RegisterRequestDto.  # noqa: E501


        :return: The last_name of this RegisterRequestDto.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this RegisterRequestDto.


        :param last_name: The last_name of this RegisterRequestDto.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def password(self):
        """Gets the password of this RegisterRequestDto.  # noqa: E501


        :return: The password of this RegisterRequestDto.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this RegisterRequestDto.


        :param password: The password of this RegisterRequestDto.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def phone(self):
        """Gets the phone of this RegisterRequestDto.  # noqa: E501


        :return: The phone of this RegisterRequestDto.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this RegisterRequestDto.


        :param phone: The phone of this RegisterRequestDto.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def region(self):
        """Gets the region of this RegisterRequestDto.  # noqa: E501


        :return: The region of this RegisterRequestDto.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this RegisterRequestDto.


        :param region: The region of this RegisterRequestDto.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def user_type(self):
        """Gets the user_type of this RegisterRequestDto.  # noqa: E501


        :return: The user_type of this RegisterRequestDto.  # noqa: E501
        :rtype: str
        """
        return self._user_type

    @user_type.setter
    def user_type(self, user_type):
        """Sets the user_type of this RegisterRequestDto.


        :param user_type: The user_type of this RegisterRequestDto.  # noqa: E501
        :type: str
        """

        self._user_type = user_type

    @property
    def username(self):
        """Gets the username of this RegisterRequestDto.  # noqa: E501


        :return: The username of this RegisterRequestDto.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this RegisterRequestDto.


        :param username: The username of this RegisterRequestDto.  # noqa: E501
        :type: str
        """

        self._username = username

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
        if issubclass(RegisterRequestDto, dict):
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
        if not isinstance(other, RegisterRequestDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RegisterRequestDto):
            return True

        return self.to_dict() != other.to_dict()
