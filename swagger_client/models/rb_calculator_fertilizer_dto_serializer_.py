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

class RbCalculatorFertilizerDtoSerializer_(object):
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
        'fertilizer_type': 'int',
        'fertilizer': 'int'
    }

    attribute_map = {
        'fertilizer_type': 'fertilizer_type',
        'fertilizer': 'fertilizer'
    }

    def __init__(self, fertilizer_type=None, fertilizer=None):  # noqa: E501
        """RbCalculatorFertilizerDtoSerializer_ - a model defined in Swagger"""  # noqa: E501
        self._fertilizer_type = None
        self._fertilizer = None
        self.discriminator = None
        self.fertilizer_type = fertilizer_type
        self.fertilizer = fertilizer

    @property
    def fertilizer_type(self):
        """Gets the fertilizer_type of this RbCalculatorFertilizerDtoSerializer_.  # noqa: E501


        :return: The fertilizer_type of this RbCalculatorFertilizerDtoSerializer_.  # noqa: E501
        :rtype: int
        """
        return self._fertilizer_type

    @fertilizer_type.setter
    def fertilizer_type(self, fertilizer_type):
        """Sets the fertilizer_type of this RbCalculatorFertilizerDtoSerializer_.


        :param fertilizer_type: The fertilizer_type of this RbCalculatorFertilizerDtoSerializer_.  # noqa: E501
        :type: int
        """
        if fertilizer_type is None:
            raise ValueError("Invalid value for `fertilizer_type`, must not be `None`")  # noqa: E501

        self._fertilizer_type = fertilizer_type

    @property
    def fertilizer(self):
        """Gets the fertilizer of this RbCalculatorFertilizerDtoSerializer_.  # noqa: E501


        :return: The fertilizer of this RbCalculatorFertilizerDtoSerializer_.  # noqa: E501
        :rtype: int
        """
        return self._fertilizer

    @fertilizer.setter
    def fertilizer(self, fertilizer):
        """Sets the fertilizer of this RbCalculatorFertilizerDtoSerializer_.


        :param fertilizer: The fertilizer of this RbCalculatorFertilizerDtoSerializer_.  # noqa: E501
        :type: int
        """
        if fertilizer is None:
            raise ValueError("Invalid value for `fertilizer`, must not be `None`")  # noqa: E501

        self._fertilizer = fertilizer

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
        if issubclass(RbCalculatorFertilizerDtoSerializer_, dict):
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
        if not isinstance(other, RbCalculatorFertilizerDtoSerializer_):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
