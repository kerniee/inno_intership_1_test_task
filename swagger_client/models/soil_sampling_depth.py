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

class SoilSamplingDepth(object):
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
        'min_depth': 'int',
        'max_depth': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'min_depth': 'min_depth',
        'max_depth': 'max_depth'
    }

    def __init__(self, id=None, name=None, min_depth=None, max_depth=None):  # noqa: E501
        """SoilSamplingDepth - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._min_depth = None
        self._max_depth = None
        self.discriminator = None
        self.id = id
        self.name = name
        if min_depth is not None:
            self.min_depth = min_depth
        if max_depth is not None:
            self.max_depth = max_depth

    @property
    def id(self):
        """Gets the id of this SoilSamplingDepth.  # noqa: E501


        :return: The id of this SoilSamplingDepth.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SoilSamplingDepth.


        :param id: The id of this SoilSamplingDepth.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this SoilSamplingDepth.  # noqa: E501


        :return: The name of this SoilSamplingDepth.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SoilSamplingDepth.


        :param name: The name of this SoilSamplingDepth.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def min_depth(self):
        """Gets the min_depth of this SoilSamplingDepth.  # noqa: E501


        :return: The min_depth of this SoilSamplingDepth.  # noqa: E501
        :rtype: int
        """
        return self._min_depth

    @min_depth.setter
    def min_depth(self, min_depth):
        """Sets the min_depth of this SoilSamplingDepth.


        :param min_depth: The min_depth of this SoilSamplingDepth.  # noqa: E501
        :type: int
        """

        self._min_depth = min_depth

    @property
    def max_depth(self):
        """Gets the max_depth of this SoilSamplingDepth.  # noqa: E501


        :return: The max_depth of this SoilSamplingDepth.  # noqa: E501
        :rtype: int
        """
        return self._max_depth

    @max_depth.setter
    def max_depth(self, max_depth):
        """Sets the max_depth of this SoilSamplingDepth.


        :param max_depth: The max_depth of this SoilSamplingDepth.  # noqa: E501
        :type: int
        """

        self._max_depth = max_depth

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
        if issubclass(SoilSamplingDepth, dict):
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
        if not isinstance(other, SoilSamplingDepth):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
