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

class MycologicalCalculator(object):
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
        'id': 'int',
        'name': 'str',
        'user': 'int',
        'creation_date': 'datetime',
        'is_done': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'user': 'user',
        'creation_date': 'creation_date',
        'is_done': 'is_done'
    }

    def __init__(self, id=None, name=None, user=None, creation_date=None, is_done=None):  # noqa: E501
        """MycologicalCalculator - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._user = None
        self._creation_date = None
        self._is_done = None
        self.discriminator = None
        self.id = id
        self.name = name
        self.user = user
        self.creation_date = creation_date
        self.is_done = is_done

    @property
    def id(self):
        """Gets the id of this MycologicalCalculator.  # noqa: E501


        :return: The id of this MycologicalCalculator.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MycologicalCalculator.


        :param id: The id of this MycologicalCalculator.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this MycologicalCalculator.  # noqa: E501


        :return: The name of this MycologicalCalculator.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MycologicalCalculator.


        :param name: The name of this MycologicalCalculator.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def user(self):
        """Gets the user of this MycologicalCalculator.  # noqa: E501


        :return: The user of this MycologicalCalculator.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this MycologicalCalculator.


        :param user: The user of this MycologicalCalculator.  # noqa: E501
        :type: int
        """
        if user is None:
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    @property
    def creation_date(self):
        """Gets the creation_date of this MycologicalCalculator.  # noqa: E501


        :return: The creation_date of this MycologicalCalculator.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this MycologicalCalculator.


        :param creation_date: The creation_date of this MycologicalCalculator.  # noqa: E501
        :type: datetime
        """
        if creation_date is None:
            raise ValueError("Invalid value for `creation_date`, must not be `None`")  # noqa: E501

        self._creation_date = creation_date

    @property
    def is_done(self):
        """Gets the is_done of this MycologicalCalculator.  # noqa: E501


        :return: The is_done of this MycologicalCalculator.  # noqa: E501
        :rtype: bool
        """
        return self._is_done

    @is_done.setter
    def is_done(self, is_done):
        """Sets the is_done of this MycologicalCalculator.


        :param is_done: The is_done of this MycologicalCalculator.  # noqa: E501
        :type: bool
        """
        if is_done is None:
            raise ValueError("Invalid value for `is_done`, must not be `None`")  # noqa: E501

        self._is_done = is_done

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
        if issubclass(MycologicalCalculator, dict):
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
        if not isinstance(other, MycologicalCalculator):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
