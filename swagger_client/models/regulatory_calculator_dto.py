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


class RegulatoryCalculatorDto(object):
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
        'acidity_type': 'str',
        'calculation_method': 'str',
        'create_date': 'datetime',
        'culture': 'Culture',
        'distribution_of_soils': 'str',
        'fertilizer_type': 'FertilizerType',
        'id': 'int',
        'name': 'str',
        'norm_fertilizer_k': 'float',
        'norm_fertilizer_n': 'float',
        'norm_fertilizer_p': 'float',
        'percent_k': 'int',
        'percent_n': 'int',
        'percent_p': 'int',
        'planned_yield': 'int',
        'predecessor_type': 'str',
        'region_type': 'int',
        'season_steps': 'list[SeasonStep]',
        'soil_type': 'str',
        'status': 'str',
        'update_date': 'datetime'
    }

    attribute_map = {
        'acidity_type': 'acidityType',
        'calculation_method': 'calculationMethod',
        'create_date': 'createDate',
        'culture': 'culture',
        'distribution_of_soils': 'distributionOfSoils',
        'fertilizer_type': 'fertilizerType',
        'id': 'id',
        'name': 'name',
        'norm_fertilizer_k': 'normFertilizerK',
        'norm_fertilizer_n': 'normFertilizerN',
        'norm_fertilizer_p': 'normFertilizerP',
        'percent_k': 'percentK',
        'percent_n': 'percentN',
        'percent_p': 'percentP',
        'planned_yield': 'plannedYield',
        'predecessor_type': 'predecessorType',
        'region_type': 'regionType',
        'season_steps': 'seasonSteps',
        'soil_type': 'soilType',
        'status': 'status',
        'update_date': 'updateDate'
    }

    def __init__(self, acidity_type=None, calculation_method=None, create_date=None, culture=None, distribution_of_soils=None, fertilizer_type=None, id=None, name=None, norm_fertilizer_k=None, norm_fertilizer_n=None, norm_fertilizer_p=None, percent_k=None, percent_n=None, percent_p=None, planned_yield=None, predecessor_type=None, region_type=None, season_steps=None, soil_type=None, status=None, update_date=None, _configuration=None):  # noqa: E501
        """RegulatoryCalculatorDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._acidity_type = None
        self._calculation_method = None
        self._create_date = None
        self._culture = None
        self._distribution_of_soils = None
        self._fertilizer_type = None
        self._id = None
        self._name = None
        self._norm_fertilizer_k = None
        self._norm_fertilizer_n = None
        self._norm_fertilizer_p = None
        self._percent_k = None
        self._percent_n = None
        self._percent_p = None
        self._planned_yield = None
        self._predecessor_type = None
        self._region_type = None
        self._season_steps = None
        self._soil_type = None
        self._status = None
        self._update_date = None
        self.discriminator = None

        if acidity_type is not None:
            self.acidity_type = acidity_type
        if calculation_method is not None:
            self.calculation_method = calculation_method
        if create_date is not None:
            self.create_date = create_date
        if culture is not None:
            self.culture = culture
        if distribution_of_soils is not None:
            self.distribution_of_soils = distribution_of_soils
        if fertilizer_type is not None:
            self.fertilizer_type = fertilizer_type
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if norm_fertilizer_k is not None:
            self.norm_fertilizer_k = norm_fertilizer_k
        if norm_fertilizer_n is not None:
            self.norm_fertilizer_n = norm_fertilizer_n
        if norm_fertilizer_p is not None:
            self.norm_fertilizer_p = norm_fertilizer_p
        if percent_k is not None:
            self.percent_k = percent_k
        if percent_n is not None:
            self.percent_n = percent_n
        if percent_p is not None:
            self.percent_p = percent_p
        if planned_yield is not None:
            self.planned_yield = planned_yield
        if predecessor_type is not None:
            self.predecessor_type = predecessor_type
        if region_type is not None:
            self.region_type = region_type
        if season_steps is not None:
            self.season_steps = season_steps
        if soil_type is not None:
            self.soil_type = soil_type
        if status is not None:
            self.status = status
        if update_date is not None:
            self.update_date = update_date

    @property
    def acidity_type(self):
        """Gets the acidity_type of this RegulatoryCalculatorDto.  # noqa: E501


        :return: The acidity_type of this RegulatoryCalculatorDto.  # noqa: E501
        :rtype: str
        """
        return self._acidity_type

    @acidity_type.setter
    def acidity_type(self, acidity_type):
        """Sets the acidity_type of this RegulatoryCalculatorDto.


        :param acidity_type: The acidity_type of this RegulatoryCalculatorDto.  # noqa: E501
        :type: str
        """

        self._acidity_type = acidity_type

    @property
    def calculation_method(self):
        """Gets the calculation_method of this RegulatoryCalculatorDto.  # noqa: E501


        :return: The calculation_method of this RegulatoryCalculatorDto.  # noqa: E501
        :rtype: str
        """
        return self._calculation_method

    @calculation_method.setter
    def calculation_method(self, calculation_method):
        """Sets the calculation_method of this RegulatoryCalculatorDto.


        :param calculation_method: The calculation_method of this RegulatoryCalculatorDto.  # noqa: E501
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
    def create_date(self):
        """Gets the create_date of this RegulatoryCalculatorDto.  # noqa: E501


        :return: The create_date of this RegulatoryCalculatorDto.  # noqa: E501
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this RegulatoryCalculatorDto.


        :param create_date: The create_date of this RegulatoryCalculatorDto.  # noqa: E501
        :type: datetime
        """

        self._create_date = create_date

    @property
    def culture(self):
        """Gets the culture of this RegulatoryCalculatorDto.  # noqa: E501


        :return: The culture of this RegulatoryCalculatorDto.  # noqa: E501
        :rtype: Culture
        """
        return self._culture

    @culture.setter
    def culture(self, culture):
        """Sets the culture of this RegulatoryCalculatorDto.


        :param culture: The culture of this RegulatoryCalculatorDto.  # noqa: E501
        :type: Culture
        """

        self._culture = culture

    @property
    def distribution_of_soils(self):
        """Gets the distribution_of_soils of this RegulatoryCalculatorDto.  # noqa: E501


        :return: The distribution_of_soils of this RegulatoryCalculatorDto.  # noqa: E501
        :rtype: str
        """
        return self._distribution_of_soils

    @distribution_of_soils.setter
    def distribution_of_soils(self, distribution_of_soils):
        """Sets the distribution_of_soils of this RegulatoryCalculatorDto.


        :param distribution_of_soils: The distribution_of_soils of this RegulatoryCalculatorDto.  # noqa: E501
        :type: str
        """

        self._distribution_of_soils = distribution_of_soils

    @property
    def fertilizer_type(self):
        """Gets the fertilizer_type of this RegulatoryCalculatorDto.  # noqa: E501


        :return: The fertilizer_type of this RegulatoryCalculatorDto.  # noqa: E501
        :rtype: FertilizerType
        """
        return self._fertilizer_type

    @fertilizer_type.setter
    def fertilizer_type(self, fertilizer_type):
        """Sets the fertilizer_type of this RegulatoryCalculatorDto.


        :param fertilizer_type: The fertilizer_type of this RegulatoryCalculatorDto.  # noqa: E501
        :type: FertilizerType
        """

        self._fertilizer_type = fertilizer_type

    @property
    def id(self):
        """Gets the id of this RegulatoryCalculatorDto.  # noqa: E501


        :return: The id of this RegulatoryCalculatorDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RegulatoryCalculatorDto.


        :param id: The id of this RegulatoryCalculatorDto.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this RegulatoryCalculatorDto.  # noqa: E501


        :return: The name of this RegulatoryCalculatorDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RegulatoryCalculatorDto.


        :param name: The name of this RegulatoryCalculatorDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def norm_fertilizer_k(self):
        """Gets the norm_fertilizer_k of this RegulatoryCalculatorDto.  # noqa: E501


        :return: The norm_fertilizer_k of this RegulatoryCalculatorDto.  # noqa: E501
        :rtype: float
        """
        return self._norm_fertilizer_k

    @norm_fertilizer_k.setter
    def norm_fertilizer_k(self, norm_fertilizer_k):
        """Sets the norm_fertilizer_k of this RegulatoryCalculatorDto.


        :param norm_fertilizer_k: The norm_fertilizer_k of this RegulatoryCalculatorDto.  # noqa: E501
        :type: float
        """

        self._norm_fertilizer_k = norm_fertilizer_k

    @property
    def norm_fertilizer_n(self):
        """Gets the norm_fertilizer_n of this RegulatoryCalculatorDto.  # noqa: E501


        :return: The norm_fertilizer_n of this RegulatoryCalculatorDto.  # noqa: E501
        :rtype: float
        """
        return self._norm_fertilizer_n

    @norm_fertilizer_n.setter
    def norm_fertilizer_n(self, norm_fertilizer_n):
        """Sets the norm_fertilizer_n of this RegulatoryCalculatorDto.


        :param norm_fertilizer_n: The norm_fertilizer_n of this RegulatoryCalculatorDto.  # noqa: E501
        :type: float
        """

        self._norm_fertilizer_n = norm_fertilizer_n

    @property
    def norm_fertilizer_p(self):
        """Gets the norm_fertilizer_p of this RegulatoryCalculatorDto.  # noqa: E501


        :return: The norm_fertilizer_p of this RegulatoryCalculatorDto.  # noqa: E501
        :rtype: float
        """
        return self._norm_fertilizer_p

    @norm_fertilizer_p.setter
    def norm_fertilizer_p(self, norm_fertilizer_p):
        """Sets the norm_fertilizer_p of this RegulatoryCalculatorDto.


        :param norm_fertilizer_p: The norm_fertilizer_p of this RegulatoryCalculatorDto.  # noqa: E501
        :type: float
        """

        self._norm_fertilizer_p = norm_fertilizer_p

    @property
    def percent_k(self):
        """Gets the percent_k of this RegulatoryCalculatorDto.  # noqa: E501


        :return: The percent_k of this RegulatoryCalculatorDto.  # noqa: E501
        :rtype: int
        """
        return self._percent_k

    @percent_k.setter
    def percent_k(self, percent_k):
        """Sets the percent_k of this RegulatoryCalculatorDto.


        :param percent_k: The percent_k of this RegulatoryCalculatorDto.  # noqa: E501
        :type: int
        """

        self._percent_k = percent_k

    @property
    def percent_n(self):
        """Gets the percent_n of this RegulatoryCalculatorDto.  # noqa: E501


        :return: The percent_n of this RegulatoryCalculatorDto.  # noqa: E501
        :rtype: int
        """
        return self._percent_n

    @percent_n.setter
    def percent_n(self, percent_n):
        """Sets the percent_n of this RegulatoryCalculatorDto.


        :param percent_n: The percent_n of this RegulatoryCalculatorDto.  # noqa: E501
        :type: int
        """

        self._percent_n = percent_n

    @property
    def percent_p(self):
        """Gets the percent_p of this RegulatoryCalculatorDto.  # noqa: E501


        :return: The percent_p of this RegulatoryCalculatorDto.  # noqa: E501
        :rtype: int
        """
        return self._percent_p

    @percent_p.setter
    def percent_p(self, percent_p):
        """Sets the percent_p of this RegulatoryCalculatorDto.


        :param percent_p: The percent_p of this RegulatoryCalculatorDto.  # noqa: E501
        :type: int
        """

        self._percent_p = percent_p

    @property
    def planned_yield(self):
        """Gets the planned_yield of this RegulatoryCalculatorDto.  # noqa: E501


        :return: The planned_yield of this RegulatoryCalculatorDto.  # noqa: E501
        :rtype: int
        """
        return self._planned_yield

    @planned_yield.setter
    def planned_yield(self, planned_yield):
        """Sets the planned_yield of this RegulatoryCalculatorDto.


        :param planned_yield: The planned_yield of this RegulatoryCalculatorDto.  # noqa: E501
        :type: int
        """

        self._planned_yield = planned_yield

    @property
    def predecessor_type(self):
        """Gets the predecessor_type of this RegulatoryCalculatorDto.  # noqa: E501


        :return: The predecessor_type of this RegulatoryCalculatorDto.  # noqa: E501
        :rtype: str
        """
        return self._predecessor_type

    @predecessor_type.setter
    def predecessor_type(self, predecessor_type):
        """Sets the predecessor_type of this RegulatoryCalculatorDto.


        :param predecessor_type: The predecessor_type of this RegulatoryCalculatorDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["CLEAN_FALLOW", "FULL_FALLOW", "PERENNIAL", "OTHER", "NOT_FALLOW", "WINTER", "ANNUAL", "SPRING", "POTATO"]  # noqa: E501
        if (self._configuration.client_side_validation and
                predecessor_type not in allowed_values):
            raise ValueError(
                "Invalid value for `predecessor_type` ({0}), must be one of {1}"  # noqa: E501
                .format(predecessor_type, allowed_values)
            )

        self._predecessor_type = predecessor_type

    @property
    def region_type(self):
        """Gets the region_type of this RegulatoryCalculatorDto.  # noqa: E501


        :return: The region_type of this RegulatoryCalculatorDto.  # noqa: E501
        :rtype: int
        """
        return self._region_type

    @region_type.setter
    def region_type(self, region_type):
        """Sets the region_type of this RegulatoryCalculatorDto.


        :param region_type: The region_type of this RegulatoryCalculatorDto.  # noqa: E501
        :type: int
        """

        self._region_type = region_type

    @property
    def season_steps(self):
        """Gets the season_steps of this RegulatoryCalculatorDto.  # noqa: E501


        :return: The season_steps of this RegulatoryCalculatorDto.  # noqa: E501
        :rtype: list[SeasonStep]
        """
        return self._season_steps

    @season_steps.setter
    def season_steps(self, season_steps):
        """Sets the season_steps of this RegulatoryCalculatorDto.


        :param season_steps: The season_steps of this RegulatoryCalculatorDto.  # noqa: E501
        :type: list[SeasonStep]
        """

        self._season_steps = season_steps

    @property
    def soil_type(self):
        """Gets the soil_type of this RegulatoryCalculatorDto.  # noqa: E501


        :return: The soil_type of this RegulatoryCalculatorDto.  # noqa: E501
        :rtype: str
        """
        return self._soil_type

    @soil_type.setter
    def soil_type(self, soil_type):
        """Sets the soil_type of this RegulatoryCalculatorDto.


        :param soil_type: The soil_type of this RegulatoryCalculatorDto.  # noqa: E501
        :type: str
        """

        self._soil_type = soil_type

    @property
    def status(self):
        """Gets the status of this RegulatoryCalculatorDto.  # noqa: E501


        :return: The status of this RegulatoryCalculatorDto.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this RegulatoryCalculatorDto.


        :param status: The status of this RegulatoryCalculatorDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["IN_PROGRESS", "COMPLETED"]  # noqa: E501
        if (self._configuration.client_side_validation and
                status not in allowed_values):
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def update_date(self):
        """Gets the update_date of this RegulatoryCalculatorDto.  # noqa: E501


        :return: The update_date of this RegulatoryCalculatorDto.  # noqa: E501
        :rtype: datetime
        """
        return self._update_date

    @update_date.setter
    def update_date(self, update_date):
        """Sets the update_date of this RegulatoryCalculatorDto.


        :param update_date: The update_date of this RegulatoryCalculatorDto.  # noqa: E501
        :type: datetime
        """

        self._update_date = update_date

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
        if issubclass(RegulatoryCalculatorDto, dict):
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
        if not isinstance(other, RegulatoryCalculatorDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RegulatoryCalculatorDto):
            return True

        return self.to_dict() != other.to_dict()
