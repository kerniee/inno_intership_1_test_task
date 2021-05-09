# coding: utf-8

"""
    Teleagronom

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class TeleagronomUser(object):
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
        'email': 'str',
        'id': 'int',
        'username': 'str',
        'region': 'int',
        'phone': 'str',
        'about': 'str',
        'groups': 'list[str]'
    }

    attribute_map = {
        'email': 'email',
        'id': 'id',
        'username': 'username',
        'region': 'region',
        'phone': 'phone',
        'about': 'about',
        'groups': 'groups'
    }

    def __init__(self, email=None, id=None, username=None, region=None, phone=None, about=None, groups=None):  # noqa: E501
        """TeleagronomUser - a model defined in Swagger"""  # noqa: E501
        self._email = None
        self._id = None
        self._username = None
        self._region = None
        self._phone = None
        self._about = None
        self._groups = None
        self.discriminator = None
        if email is not None:
            self.email = email
        self.id = id
        self.username = username
        if region is not None:
            self.region = region
        if phone is not None:
            self.phone = phone
        if about is not None:
            self.about = about
        self.groups = groups

    @property
    def email(self):
        """Gets the email of this TeleagronomUser.  # noqa: E501


        :return: The email of this TeleagronomUser.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this TeleagronomUser.


        :param email: The email of this TeleagronomUser.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def id(self):
        """Gets the id of this TeleagronomUser.  # noqa: E501


        :return: The id of this TeleagronomUser.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TeleagronomUser.


        :param id: The id of this TeleagronomUser.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def username(self):
        """Gets the username of this TeleagronomUser.  # noqa: E501

        Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.  # noqa: E501

        :return: The username of this TeleagronomUser.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this TeleagronomUser.

        Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.  # noqa: E501

        :param username: The username of this TeleagronomUser.  # noqa: E501
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def region(self):
        """Gets the region of this TeleagronomUser.  # noqa: E501


        :return: The region of this TeleagronomUser.  # noqa: E501
        :rtype: int
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this TeleagronomUser.


        :param region: The region of this TeleagronomUser.  # noqa: E501
        :type: int
        """

        self._region = region

    @property
    def phone(self):
        """Gets the phone of this TeleagronomUser.  # noqa: E501


        :return: The phone of this TeleagronomUser.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this TeleagronomUser.


        :param phone: The phone of this TeleagronomUser.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def about(self):
        """Gets the about of this TeleagronomUser.  # noqa: E501


        :return: The about of this TeleagronomUser.  # noqa: E501
        :rtype: str
        """
        return self._about

    @about.setter
    def about(self, about):
        """Sets the about of this TeleagronomUser.


        :param about: The about of this TeleagronomUser.  # noqa: E501
        :type: str
        """

        self._about = about

    @property
    def groups(self):
        """Gets the groups of this TeleagronomUser.  # noqa: E501


        :return: The groups of this TeleagronomUser.  # noqa: E501
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this TeleagronomUser.


        :param groups: The groups of this TeleagronomUser.  # noqa: E501
        :type: list[str]
        """
        if groups is None:
            raise ValueError("Invalid value for `groups`, must not be `None`")  # noqa: E501

        self._groups = groups

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
        if issubclass(TeleagronomUser, dict):
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
        if not isinstance(other, TeleagronomUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
