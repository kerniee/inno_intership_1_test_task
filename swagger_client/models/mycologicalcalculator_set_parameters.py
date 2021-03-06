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

class MycologicalcalculatorSetParameters(object):
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
        'sampling_coordinates': 'str',
        'probe_number': 'int',
        'preceding_culture': 'int',
        'culture': 'int',
        'report': 'list[MicroorganismsGenusDtoSerializer_]'
    }

    attribute_map = {
        'sampling_coordinates': 'sampling_coordinates',
        'probe_number': 'probe_number',
        'preceding_culture': 'preceding_culture',
        'culture': 'culture',
        'report': 'report'
    }

    def __init__(self, sampling_coordinates=None, probe_number=None, preceding_culture=None, culture=None, report=None):  # noqa: E501
        """MycologicalcalculatorSetParameters - a model defined in Swagger"""  # noqa: E501
        self._sampling_coordinates = None
        self._probe_number = None
        self._preceding_culture = None
        self._culture = None
        self._report = None
        self.discriminator = None
        if sampling_coordinates is not None:
            self.sampling_coordinates = sampling_coordinates
        if probe_number is not None:
            self.probe_number = probe_number
        self.preceding_culture = preceding_culture
        self.culture = culture
        self.report = report

    @property
    def sampling_coordinates(self):
        """Gets the sampling_coordinates of this MycologicalcalculatorSetParameters.  # noqa: E501


        :return: The sampling_coordinates of this MycologicalcalculatorSetParameters.  # noqa: E501
        :rtype: str
        """
        return self._sampling_coordinates

    @sampling_coordinates.setter
    def sampling_coordinates(self, sampling_coordinates):
        """Sets the sampling_coordinates of this MycologicalcalculatorSetParameters.


        :param sampling_coordinates: The sampling_coordinates of this MycologicalcalculatorSetParameters.  # noqa: E501
        :type: str
        """

        self._sampling_coordinates = sampling_coordinates

    @property
    def probe_number(self):
        """Gets the probe_number of this MycologicalcalculatorSetParameters.  # noqa: E501


        :return: The probe_number of this MycologicalcalculatorSetParameters.  # noqa: E501
        :rtype: int
        """
        return self._probe_number

    @probe_number.setter
    def probe_number(self, probe_number):
        """Sets the probe_number of this MycologicalcalculatorSetParameters.


        :param probe_number: The probe_number of this MycologicalcalculatorSetParameters.  # noqa: E501
        :type: int
        """

        self._probe_number = probe_number

    @property
    def preceding_culture(self):
        """Gets the preceding_culture of this MycologicalcalculatorSetParameters.  # noqa: E501


        :return: The preceding_culture of this MycologicalcalculatorSetParameters.  # noqa: E501
        :rtype: int
        """
        return self._preceding_culture

    @preceding_culture.setter
    def preceding_culture(self, preceding_culture):
        """Sets the preceding_culture of this MycologicalcalculatorSetParameters.


        :param preceding_culture: The preceding_culture of this MycologicalcalculatorSetParameters.  # noqa: E501
        :type: int
        """
        if preceding_culture is None:
            raise ValueError("Invalid value for `preceding_culture`, must not be `None`")  # noqa: E501

        self._preceding_culture = preceding_culture

    @property
    def culture(self):
        """Gets the culture of this MycologicalcalculatorSetParameters.  # noqa: E501


        :return: The culture of this MycologicalcalculatorSetParameters.  # noqa: E501
        :rtype: int
        """
        return self._culture

    @culture.setter
    def culture(self, culture):
        """Sets the culture of this MycologicalcalculatorSetParameters.


        :param culture: The culture of this MycologicalcalculatorSetParameters.  # noqa: E501
        :type: int
        """
        if culture is None:
            raise ValueError("Invalid value for `culture`, must not be `None`")  # noqa: E501

        self._culture = culture

    @property
    def report(self):
        """Gets the report of this MycologicalcalculatorSetParameters.  # noqa: E501


        :return: The report of this MycologicalcalculatorSetParameters.  # noqa: E501
        :rtype: list[MicroorganismsGenusDtoSerializer_]
        """
        return self._report

    @report.setter
    def report(self, report):
        """Sets the report of this MycologicalcalculatorSetParameters.


        :param report: The report of this MycologicalcalculatorSetParameters.  # noqa: E501
        :type: list[MicroorganismsGenusDtoSerializer_]
        """
        if report is None:
            raise ValueError("Invalid value for `report`, must not be `None`")  # noqa: E501

        self._report = report

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
        if issubclass(MycologicalcalculatorSetParameters, dict):
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
        if not isinstance(other, MycologicalcalculatorSetParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
