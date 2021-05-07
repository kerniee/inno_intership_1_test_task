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


class SeasonStep(object):
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
        'autumn': 'bool',
        'autumn_norm': 'int',
        'autumn_value': 'int',
        'autumn_weight': 'int',
        'calculation_method': 'str',
        'calculator_id': 'int',
        'fertilizer': 'Fertilizer',
        'fertilizer_type': 'FertilizerType',
        'fertilizer_weight': 'str',
        'first': 'bool',
        'first_norm': 'int',
        'first_value': 'int',
        'first_weight': 'int',
        'id': 'int',
        'second': 'bool',
        'second_norm': 'int',
        'second_value': 'int',
        'second_weight': 'int',
        'spring': 'bool',
        'spring_norm': 'int',
        'spring_value': 'int',
        'spring_weight': 'int'
    }

    attribute_map = {
        'autumn': 'autumn',
        'autumn_norm': 'autumnNorm',
        'autumn_value': 'autumnValue',
        'autumn_weight': 'autumnWeight',
        'calculation_method': 'calculationMethod',
        'calculator_id': 'calculatorId',
        'fertilizer': 'fertilizer',
        'fertilizer_type': 'fertilizerType',
        'fertilizer_weight': 'fertilizerWeight',
        'first': 'first',
        'first_norm': 'firstNorm',
        'first_value': 'firstValue',
        'first_weight': 'firstWeight',
        'id': 'id',
        'second': 'second',
        'second_norm': 'secondNorm',
        'second_value': 'secondValue',
        'second_weight': 'secondWeight',
        'spring': 'spring',
        'spring_norm': 'springNorm',
        'spring_value': 'springValue',
        'spring_weight': 'springWeight'
    }

    def __init__(self, autumn=None, autumn_norm=None, autumn_value=None, autumn_weight=None, calculation_method=None, calculator_id=None, fertilizer=None, fertilizer_type=None, fertilizer_weight=None, first=None, first_norm=None, first_value=None, first_weight=None, id=None, second=None, second_norm=None, second_value=None, second_weight=None, spring=None, spring_norm=None, spring_value=None, spring_weight=None, _configuration=None):  # noqa: E501
        """SeasonStep - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._autumn = None
        self._autumn_norm = None
        self._autumn_value = None
        self._autumn_weight = None
        self._calculation_method = None
        self._calculator_id = None
        self._fertilizer = None
        self._fertilizer_type = None
        self._fertilizer_weight = None
        self._first = None
        self._first_norm = None
        self._first_value = None
        self._first_weight = None
        self._id = None
        self._second = None
        self._second_norm = None
        self._second_value = None
        self._second_weight = None
        self._spring = None
        self._spring_norm = None
        self._spring_value = None
        self._spring_weight = None
        self.discriminator = None

        if autumn is not None:
            self.autumn = autumn
        if autumn_norm is not None:
            self.autumn_norm = autumn_norm
        if autumn_value is not None:
            self.autumn_value = autumn_value
        if autumn_weight is not None:
            self.autumn_weight = autumn_weight
        if calculation_method is not None:
            self.calculation_method = calculation_method
        if calculator_id is not None:
            self.calculator_id = calculator_id
        if fertilizer is not None:
            self.fertilizer = fertilizer
        if fertilizer_type is not None:
            self.fertilizer_type = fertilizer_type
        if fertilizer_weight is not None:
            self.fertilizer_weight = fertilizer_weight
        if first is not None:
            self.first = first
        if first_norm is not None:
            self.first_norm = first_norm
        if first_value is not None:
            self.first_value = first_value
        if first_weight is not None:
            self.first_weight = first_weight
        if id is not None:
            self.id = id
        if second is not None:
            self.second = second
        if second_norm is not None:
            self.second_norm = second_norm
        if second_value is not None:
            self.second_value = second_value
        if second_weight is not None:
            self.second_weight = second_weight
        if spring is not None:
            self.spring = spring
        if spring_norm is not None:
            self.spring_norm = spring_norm
        if spring_value is not None:
            self.spring_value = spring_value
        if spring_weight is not None:
            self.spring_weight = spring_weight

    @property
    def autumn(self):
        """Gets the autumn of this SeasonStep.  # noqa: E501


        :return: The autumn of this SeasonStep.  # noqa: E501
        :rtype: bool
        """
        return self._autumn

    @autumn.setter
    def autumn(self, autumn):
        """Sets the autumn of this SeasonStep.


        :param autumn: The autumn of this SeasonStep.  # noqa: E501
        :type: bool
        """

        self._autumn = autumn

    @property
    def autumn_norm(self):
        """Gets the autumn_norm of this SeasonStep.  # noqa: E501


        :return: The autumn_norm of this SeasonStep.  # noqa: E501
        :rtype: int
        """
        return self._autumn_norm

    @autumn_norm.setter
    def autumn_norm(self, autumn_norm):
        """Sets the autumn_norm of this SeasonStep.


        :param autumn_norm: The autumn_norm of this SeasonStep.  # noqa: E501
        :type: int
        """

        self._autumn_norm = autumn_norm

    @property
    def autumn_value(self):
        """Gets the autumn_value of this SeasonStep.  # noqa: E501


        :return: The autumn_value of this SeasonStep.  # noqa: E501
        :rtype: int
        """
        return self._autumn_value

    @autumn_value.setter
    def autumn_value(self, autumn_value):
        """Sets the autumn_value of this SeasonStep.


        :param autumn_value: The autumn_value of this SeasonStep.  # noqa: E501
        :type: int
        """

        self._autumn_value = autumn_value

    @property
    def autumn_weight(self):
        """Gets the autumn_weight of this SeasonStep.  # noqa: E501


        :return: The autumn_weight of this SeasonStep.  # noqa: E501
        :rtype: int
        """
        return self._autumn_weight

    @autumn_weight.setter
    def autumn_weight(self, autumn_weight):
        """Sets the autumn_weight of this SeasonStep.


        :param autumn_weight: The autumn_weight of this SeasonStep.  # noqa: E501
        :type: int
        """

        self._autumn_weight = autumn_weight

    @property
    def calculation_method(self):
        """Gets the calculation_method of this SeasonStep.  # noqa: E501


        :return: The calculation_method of this SeasonStep.  # noqa: E501
        :rtype: str
        """
        return self._calculation_method

    @calculation_method.setter
    def calculation_method(self, calculation_method):
        """Sets the calculation_method of this SeasonStep.


        :param calculation_method: The calculation_method of this SeasonStep.  # noqa: E501
        :type: str
        """
        allowed_values = ["REGULATORY", "SETTLEMENT_BALANCE", "LIQUID", "FED"]  # noqa: E501
        if (self._configuration.client_side_validation and
                calculation_method not in allowed_values):
            raise ValueError(
                "Invalid value for `calculation_method` ({0}), must be one of {1}"  # noqa: E501
                .format(calculation_method, allowed_values)
            )

        self._calculation_method = calculation_method

    @property
    def calculator_id(self):
        """Gets the calculator_id of this SeasonStep.  # noqa: E501


        :return: The calculator_id of this SeasonStep.  # noqa: E501
        :rtype: int
        """
        return self._calculator_id

    @calculator_id.setter
    def calculator_id(self, calculator_id):
        """Sets the calculator_id of this SeasonStep.


        :param calculator_id: The calculator_id of this SeasonStep.  # noqa: E501
        :type: int
        """

        self._calculator_id = calculator_id

    @property
    def fertilizer(self):
        """Gets the fertilizer of this SeasonStep.  # noqa: E501


        :return: The fertilizer of this SeasonStep.  # noqa: E501
        :rtype: Fertilizer
        """
        return self._fertilizer

    @fertilizer.setter
    def fertilizer(self, fertilizer):
        """Sets the fertilizer of this SeasonStep.


        :param fertilizer: The fertilizer of this SeasonStep.  # noqa: E501
        :type: Fertilizer
        """

        self._fertilizer = fertilizer

    @property
    def fertilizer_type(self):
        """Gets the fertilizer_type of this SeasonStep.  # noqa: E501


        :return: The fertilizer_type of this SeasonStep.  # noqa: E501
        :rtype: FertilizerType
        """
        return self._fertilizer_type

    @fertilizer_type.setter
    def fertilizer_type(self, fertilizer_type):
        """Sets the fertilizer_type of this SeasonStep.


        :param fertilizer_type: The fertilizer_type of this SeasonStep.  # noqa: E501
        :type: FertilizerType
        """

        self._fertilizer_type = fertilizer_type

    @property
    def fertilizer_weight(self):
        """Gets the fertilizer_weight of this SeasonStep.  # noqa: E501


        :return: The fertilizer_weight of this SeasonStep.  # noqa: E501
        :rtype: str
        """
        return self._fertilizer_weight

    @fertilizer_weight.setter
    def fertilizer_weight(self, fertilizer_weight):
        """Sets the fertilizer_weight of this SeasonStep.


        :param fertilizer_weight: The fertilizer_weight of this SeasonStep.  # noqa: E501
        :type: str
        """

        self._fertilizer_weight = fertilizer_weight

    @property
    def first(self):
        """Gets the first of this SeasonStep.  # noqa: E501


        :return: The first of this SeasonStep.  # noqa: E501
        :rtype: bool
        """
        return self._first

    @first.setter
    def first(self, first):
        """Sets the first of this SeasonStep.


        :param first: The first of this SeasonStep.  # noqa: E501
        :type: bool
        """

        self._first = first

    @property
    def first_norm(self):
        """Gets the first_norm of this SeasonStep.  # noqa: E501


        :return: The first_norm of this SeasonStep.  # noqa: E501
        :rtype: int
        """
        return self._first_norm

    @first_norm.setter
    def first_norm(self, first_norm):
        """Sets the first_norm of this SeasonStep.


        :param first_norm: The first_norm of this SeasonStep.  # noqa: E501
        :type: int
        """

        self._first_norm = first_norm

    @property
    def first_value(self):
        """Gets the first_value of this SeasonStep.  # noqa: E501


        :return: The first_value of this SeasonStep.  # noqa: E501
        :rtype: int
        """
        return self._first_value

    @first_value.setter
    def first_value(self, first_value):
        """Sets the first_value of this SeasonStep.


        :param first_value: The first_value of this SeasonStep.  # noqa: E501
        :type: int
        """

        self._first_value = first_value

    @property
    def first_weight(self):
        """Gets the first_weight of this SeasonStep.  # noqa: E501


        :return: The first_weight of this SeasonStep.  # noqa: E501
        :rtype: int
        """
        return self._first_weight

    @first_weight.setter
    def first_weight(self, first_weight):
        """Sets the first_weight of this SeasonStep.


        :param first_weight: The first_weight of this SeasonStep.  # noqa: E501
        :type: int
        """

        self._first_weight = first_weight

    @property
    def id(self):
        """Gets the id of this SeasonStep.  # noqa: E501


        :return: The id of this SeasonStep.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SeasonStep.


        :param id: The id of this SeasonStep.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def second(self):
        """Gets the second of this SeasonStep.  # noqa: E501


        :return: The second of this SeasonStep.  # noqa: E501
        :rtype: bool
        """
        return self._second

    @second.setter
    def second(self, second):
        """Sets the second of this SeasonStep.


        :param second: The second of this SeasonStep.  # noqa: E501
        :type: bool
        """

        self._second = second

    @property
    def second_norm(self):
        """Gets the second_norm of this SeasonStep.  # noqa: E501


        :return: The second_norm of this SeasonStep.  # noqa: E501
        :rtype: int
        """
        return self._second_norm

    @second_norm.setter
    def second_norm(self, second_norm):
        """Sets the second_norm of this SeasonStep.


        :param second_norm: The second_norm of this SeasonStep.  # noqa: E501
        :type: int
        """

        self._second_norm = second_norm

    @property
    def second_value(self):
        """Gets the second_value of this SeasonStep.  # noqa: E501


        :return: The second_value of this SeasonStep.  # noqa: E501
        :rtype: int
        """
        return self._second_value

    @second_value.setter
    def second_value(self, second_value):
        """Sets the second_value of this SeasonStep.


        :param second_value: The second_value of this SeasonStep.  # noqa: E501
        :type: int
        """

        self._second_value = second_value

    @property
    def second_weight(self):
        """Gets the second_weight of this SeasonStep.  # noqa: E501


        :return: The second_weight of this SeasonStep.  # noqa: E501
        :rtype: int
        """
        return self._second_weight

    @second_weight.setter
    def second_weight(self, second_weight):
        """Sets the second_weight of this SeasonStep.


        :param second_weight: The second_weight of this SeasonStep.  # noqa: E501
        :type: int
        """

        self._second_weight = second_weight

    @property
    def spring(self):
        """Gets the spring of this SeasonStep.  # noqa: E501


        :return: The spring of this SeasonStep.  # noqa: E501
        :rtype: bool
        """
        return self._spring

    @spring.setter
    def spring(self, spring):
        """Sets the spring of this SeasonStep.


        :param spring: The spring of this SeasonStep.  # noqa: E501
        :type: bool
        """

        self._spring = spring

    @property
    def spring_norm(self):
        """Gets the spring_norm of this SeasonStep.  # noqa: E501


        :return: The spring_norm of this SeasonStep.  # noqa: E501
        :rtype: int
        """
        return self._spring_norm

    @spring_norm.setter
    def spring_norm(self, spring_norm):
        """Sets the spring_norm of this SeasonStep.


        :param spring_norm: The spring_norm of this SeasonStep.  # noqa: E501
        :type: int
        """

        self._spring_norm = spring_norm

    @property
    def spring_value(self):
        """Gets the spring_value of this SeasonStep.  # noqa: E501


        :return: The spring_value of this SeasonStep.  # noqa: E501
        :rtype: int
        """
        return self._spring_value

    @spring_value.setter
    def spring_value(self, spring_value):
        """Sets the spring_value of this SeasonStep.


        :param spring_value: The spring_value of this SeasonStep.  # noqa: E501
        :type: int
        """

        self._spring_value = spring_value

    @property
    def spring_weight(self):
        """Gets the spring_weight of this SeasonStep.  # noqa: E501


        :return: The spring_weight of this SeasonStep.  # noqa: E501
        :rtype: int
        """
        return self._spring_weight

    @spring_weight.setter
    def spring_weight(self, spring_weight):
        """Sets the spring_weight of this SeasonStep.


        :param spring_weight: The spring_weight of this SeasonStep.  # noqa: E501
        :type: int
        """

        self._spring_weight = spring_weight

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
        if issubclass(SeasonStep, dict):
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
        if not isinstance(other, SeasonStep):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SeasonStep):
            return True

        return self.to_dict() != other.to_dict()
