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

class FluidCalculatorCalculationParametersDtoSerializer_(object):
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
        'consumption_rate_from_catalog': 'int',
        'fluid_consumption_rate_for_nozzle': 'float',
        'number_of_nozzles_on_the_rod': 'int',
        'rod_width': 'float',
        'actual_spraying_speed': 'float'
    }

    attribute_map = {
        'consumption_rate_from_catalog': 'consumption_rate_from_catalog',
        'fluid_consumption_rate_for_nozzle': 'fluid_consumption_rate_for_nozzle',
        'number_of_nozzles_on_the_rod': 'number_of_nozzles_on_the_rod',
        'rod_width': 'rod_width',
        'actual_spraying_speed': 'actual_spraying_speed'
    }

    def __init__(self, consumption_rate_from_catalog=None, fluid_consumption_rate_for_nozzle=None, number_of_nozzles_on_the_rod=None, rod_width=None, actual_spraying_speed=None):  # noqa: E501
        """FluidCalculatorCalculationParametersDtoSerializer_ - a model defined in Swagger"""  # noqa: E501
        self._consumption_rate_from_catalog = None
        self._fluid_consumption_rate_for_nozzle = None
        self._number_of_nozzles_on_the_rod = None
        self._rod_width = None
        self._actual_spraying_speed = None
        self.discriminator = None
        if consumption_rate_from_catalog is not None:
            self.consumption_rate_from_catalog = consumption_rate_from_catalog
        if fluid_consumption_rate_for_nozzle is not None:
            self.fluid_consumption_rate_for_nozzle = fluid_consumption_rate_for_nozzle
        if number_of_nozzles_on_the_rod is not None:
            self.number_of_nozzles_on_the_rod = number_of_nozzles_on_the_rod
        if rod_width is not None:
            self.rod_width = rod_width
        if actual_spraying_speed is not None:
            self.actual_spraying_speed = actual_spraying_speed

    @property
    def consumption_rate_from_catalog(self):
        """Gets the consumption_rate_from_catalog of this FluidCalculatorCalculationParametersDtoSerializer_.  # noqa: E501


        :return: The consumption_rate_from_catalog of this FluidCalculatorCalculationParametersDtoSerializer_.  # noqa: E501
        :rtype: int
        """
        return self._consumption_rate_from_catalog

    @consumption_rate_from_catalog.setter
    def consumption_rate_from_catalog(self, consumption_rate_from_catalog):
        """Sets the consumption_rate_from_catalog of this FluidCalculatorCalculationParametersDtoSerializer_.


        :param consumption_rate_from_catalog: The consumption_rate_from_catalog of this FluidCalculatorCalculationParametersDtoSerializer_.  # noqa: E501
        :type: int
        """

        self._consumption_rate_from_catalog = consumption_rate_from_catalog

    @property
    def fluid_consumption_rate_for_nozzle(self):
        """Gets the fluid_consumption_rate_for_nozzle of this FluidCalculatorCalculationParametersDtoSerializer_.  # noqa: E501


        :return: The fluid_consumption_rate_for_nozzle of this FluidCalculatorCalculationParametersDtoSerializer_.  # noqa: E501
        :rtype: float
        """
        return self._fluid_consumption_rate_for_nozzle

    @fluid_consumption_rate_for_nozzle.setter
    def fluid_consumption_rate_for_nozzle(self, fluid_consumption_rate_for_nozzle):
        """Sets the fluid_consumption_rate_for_nozzle of this FluidCalculatorCalculationParametersDtoSerializer_.


        :param fluid_consumption_rate_for_nozzle: The fluid_consumption_rate_for_nozzle of this FluidCalculatorCalculationParametersDtoSerializer_.  # noqa: E501
        :type: float
        """

        self._fluid_consumption_rate_for_nozzle = fluid_consumption_rate_for_nozzle

    @property
    def number_of_nozzles_on_the_rod(self):
        """Gets the number_of_nozzles_on_the_rod of this FluidCalculatorCalculationParametersDtoSerializer_.  # noqa: E501


        :return: The number_of_nozzles_on_the_rod of this FluidCalculatorCalculationParametersDtoSerializer_.  # noqa: E501
        :rtype: int
        """
        return self._number_of_nozzles_on_the_rod

    @number_of_nozzles_on_the_rod.setter
    def number_of_nozzles_on_the_rod(self, number_of_nozzles_on_the_rod):
        """Sets the number_of_nozzles_on_the_rod of this FluidCalculatorCalculationParametersDtoSerializer_.


        :param number_of_nozzles_on_the_rod: The number_of_nozzles_on_the_rod of this FluidCalculatorCalculationParametersDtoSerializer_.  # noqa: E501
        :type: int
        """

        self._number_of_nozzles_on_the_rod = number_of_nozzles_on_the_rod

    @property
    def rod_width(self):
        """Gets the rod_width of this FluidCalculatorCalculationParametersDtoSerializer_.  # noqa: E501


        :return: The rod_width of this FluidCalculatorCalculationParametersDtoSerializer_.  # noqa: E501
        :rtype: float
        """
        return self._rod_width

    @rod_width.setter
    def rod_width(self, rod_width):
        """Sets the rod_width of this FluidCalculatorCalculationParametersDtoSerializer_.


        :param rod_width: The rod_width of this FluidCalculatorCalculationParametersDtoSerializer_.  # noqa: E501
        :type: float
        """

        self._rod_width = rod_width

    @property
    def actual_spraying_speed(self):
        """Gets the actual_spraying_speed of this FluidCalculatorCalculationParametersDtoSerializer_.  # noqa: E501


        :return: The actual_spraying_speed of this FluidCalculatorCalculationParametersDtoSerializer_.  # noqa: E501
        :rtype: float
        """
        return self._actual_spraying_speed

    @actual_spraying_speed.setter
    def actual_spraying_speed(self, actual_spraying_speed):
        """Sets the actual_spraying_speed of this FluidCalculatorCalculationParametersDtoSerializer_.


        :param actual_spraying_speed: The actual_spraying_speed of this FluidCalculatorCalculationParametersDtoSerializer_.  # noqa: E501
        :type: float
        """

        self._actual_spraying_speed = actual_spraying_speed

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
        if issubclass(FluidCalculatorCalculationParametersDtoSerializer_, dict):
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
        if not isinstance(other, FluidCalculatorCalculationParametersDtoSerializer_):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
