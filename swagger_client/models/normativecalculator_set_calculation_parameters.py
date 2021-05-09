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

class NormativecalculatorSetCalculationParameters(object):
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
        'calculation_parameters': 'NormativeCalculatorParametersDtoSerializer_'
    }

    attribute_map = {
        'calculation_parameters': 'calculation_parameters'
    }

    def __init__(self, calculation_parameters=None):  # noqa: E501
        """NormativecalculatorSetCalculationParameters - a model defined in Swagger"""  # noqa: E501
        self._calculation_parameters = None
        self.discriminator = None
        self.calculation_parameters = calculation_parameters

    @property
    def calculation_parameters(self):
        """Gets the calculation_parameters of this NormativecalculatorSetCalculationParameters.  # noqa: E501


        :return: The calculation_parameters of this NormativecalculatorSetCalculationParameters.  # noqa: E501
        :rtype: NormativeCalculatorParametersDtoSerializer_
        """
        return self._calculation_parameters

    @calculation_parameters.setter
    def calculation_parameters(self, calculation_parameters):
        """Sets the calculation_parameters of this NormativecalculatorSetCalculationParameters.


        :param calculation_parameters: The calculation_parameters of this NormativecalculatorSetCalculationParameters.  # noqa: E501
        :type: NormativeCalculatorParametersDtoSerializer_
        """
        if calculation_parameters is None:
            raise ValueError("Invalid value for `calculation_parameters`, must not be `None`")  # noqa: E501

        self._calculation_parameters = calculation_parameters

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
        if issubclass(NormativecalculatorSetCalculationParameters, dict):
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
        if not isinstance(other, NormativecalculatorSetCalculationParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
