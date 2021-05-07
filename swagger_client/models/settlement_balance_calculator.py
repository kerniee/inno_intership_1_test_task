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


class SettlementBalanceCalculator(object):
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
        'calculation_method': 'str',
        'create_date': 'datetime',
        'culture': 'Culture',
        'depth_type': 'int',
        'fertilizer_type': 'FertilizerType',
        'hydration_type': 'str',
        'hydration_value': 'float',
        'id': 'int',
        'method_analysis_depth': 'float',
        'method_analysis_type': 'str',
        'name': 'str',
        'norm_fertilizer': 'float',
        'planned_yield': 'float',
        'predecessor_type': 'str',
        'region_type': 'int',
        'status': 'str',
        'test_data': 'float',
        'texture_type': 'str',
        'update_date': 'datetime',
        'user_id': 'int',
        'year_type': 'str'
    }

    attribute_map = {
        'calculation_method': 'calculationMethod',
        'create_date': 'createDate',
        'culture': 'culture',
        'depth_type': 'depthType',
        'fertilizer_type': 'fertilizerType',
        'hydration_type': 'hydrationType',
        'hydration_value': 'hydrationValue',
        'id': 'id',
        'method_analysis_depth': 'methodAnalysisDepth',
        'method_analysis_type': 'methodAnalysisType',
        'name': 'name',
        'norm_fertilizer': 'normFertilizer',
        'planned_yield': 'plannedYield',
        'predecessor_type': 'predecessorType',
        'region_type': 'regionType',
        'status': 'status',
        'test_data': 'testData',
        'texture_type': 'textureType',
        'update_date': 'updateDate',
        'user_id': 'userId',
        'year_type': 'yearType'
    }

    def __init__(self, calculation_method=None, create_date=None, culture=None, depth_type=None, fertilizer_type=None, hydration_type=None, hydration_value=None, id=None, method_analysis_depth=None, method_analysis_type=None, name=None, norm_fertilizer=None, planned_yield=None, predecessor_type=None, region_type=None, status=None, test_data=None, texture_type=None, update_date=None, user_id=None, year_type=None, _configuration=None):  # noqa: E501
        """SettlementBalanceCalculator - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._calculation_method = None
        self._create_date = None
        self._culture = None
        self._depth_type = None
        self._fertilizer_type = None
        self._hydration_type = None
        self._hydration_value = None
        self._id = None
        self._method_analysis_depth = None
        self._method_analysis_type = None
        self._name = None
        self._norm_fertilizer = None
        self._planned_yield = None
        self._predecessor_type = None
        self._region_type = None
        self._status = None
        self._test_data = None
        self._texture_type = None
        self._update_date = None
        self._user_id = None
        self._year_type = None
        self.discriminator = None

        if calculation_method is not None:
            self.calculation_method = calculation_method
        if create_date is not None:
            self.create_date = create_date
        if culture is not None:
            self.culture = culture
        if depth_type is not None:
            self.depth_type = depth_type
        if fertilizer_type is not None:
            self.fertilizer_type = fertilizer_type
        if hydration_type is not None:
            self.hydration_type = hydration_type
        if hydration_value is not None:
            self.hydration_value = hydration_value
        if id is not None:
            self.id = id
        if method_analysis_depth is not None:
            self.method_analysis_depth = method_analysis_depth
        if method_analysis_type is not None:
            self.method_analysis_type = method_analysis_type
        if name is not None:
            self.name = name
        if norm_fertilizer is not None:
            self.norm_fertilizer = norm_fertilizer
        if planned_yield is not None:
            self.planned_yield = planned_yield
        if predecessor_type is not None:
            self.predecessor_type = predecessor_type
        if region_type is not None:
            self.region_type = region_type
        if status is not None:
            self.status = status
        if test_data is not None:
            self.test_data = test_data
        if texture_type is not None:
            self.texture_type = texture_type
        if update_date is not None:
            self.update_date = update_date
        if user_id is not None:
            self.user_id = user_id
        if year_type is not None:
            self.year_type = year_type

    @property
    def calculation_method(self):
        """Gets the calculation_method of this SettlementBalanceCalculator.  # noqa: E501


        :return: The calculation_method of this SettlementBalanceCalculator.  # noqa: E501
        :rtype: str
        """
        return self._calculation_method

    @calculation_method.setter
    def calculation_method(self, calculation_method):
        """Sets the calculation_method of this SettlementBalanceCalculator.


        :param calculation_method: The calculation_method of this SettlementBalanceCalculator.  # noqa: E501
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
        """Gets the create_date of this SettlementBalanceCalculator.  # noqa: E501


        :return: The create_date of this SettlementBalanceCalculator.  # noqa: E501
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this SettlementBalanceCalculator.


        :param create_date: The create_date of this SettlementBalanceCalculator.  # noqa: E501
        :type: datetime
        """

        self._create_date = create_date

    @property
    def culture(self):
        """Gets the culture of this SettlementBalanceCalculator.  # noqa: E501


        :return: The culture of this SettlementBalanceCalculator.  # noqa: E501
        :rtype: Culture
        """
        return self._culture

    @culture.setter
    def culture(self, culture):
        """Sets the culture of this SettlementBalanceCalculator.


        :param culture: The culture of this SettlementBalanceCalculator.  # noqa: E501
        :type: Culture
        """

        self._culture = culture

    @property
    def depth_type(self):
        """Gets the depth_type of this SettlementBalanceCalculator.  # noqa: E501


        :return: The depth_type of this SettlementBalanceCalculator.  # noqa: E501
        :rtype: int
        """
        return self._depth_type

    @depth_type.setter
    def depth_type(self, depth_type):
        """Sets the depth_type of this SettlementBalanceCalculator.


        :param depth_type: The depth_type of this SettlementBalanceCalculator.  # noqa: E501
        :type: int
        """

        self._depth_type = depth_type

    @property
    def fertilizer_type(self):
        """Gets the fertilizer_type of this SettlementBalanceCalculator.  # noqa: E501


        :return: The fertilizer_type of this SettlementBalanceCalculator.  # noqa: E501
        :rtype: FertilizerType
        """
        return self._fertilizer_type

    @fertilizer_type.setter
    def fertilizer_type(self, fertilizer_type):
        """Sets the fertilizer_type of this SettlementBalanceCalculator.


        :param fertilizer_type: The fertilizer_type of this SettlementBalanceCalculator.  # noqa: E501
        :type: FertilizerType
        """

        self._fertilizer_type = fertilizer_type

    @property
    def hydration_type(self):
        """Gets the hydration_type of this SettlementBalanceCalculator.  # noqa: E501


        :return: The hydration_type of this SettlementBalanceCalculator.  # noqa: E501
        :rtype: str
        """
        return self._hydration_type

    @hydration_type.setter
    def hydration_type(self, hydration_type):
        """Sets the hydration_type of this SettlementBalanceCalculator.


        :param hydration_type: The hydration_type of this SettlementBalanceCalculator.  # noqa: E501
        :type: str
        """
        allowed_values = ["MODERATE_HYDRATION", "HEAVY_RAINFALL", "NO_HYDRATION", "EASY_HYDRATION"]  # noqa: E501
        if (self._configuration.client_side_validation and
                hydration_type not in allowed_values):
            raise ValueError(
                "Invalid value for `hydration_type` ({0}), must be one of {1}"  # noqa: E501
                .format(hydration_type, allowed_values)
            )

        self._hydration_type = hydration_type

    @property
    def hydration_value(self):
        """Gets the hydration_value of this SettlementBalanceCalculator.  # noqa: E501


        :return: The hydration_value of this SettlementBalanceCalculator.  # noqa: E501
        :rtype: float
        """
        return self._hydration_value

    @hydration_value.setter
    def hydration_value(self, hydration_value):
        """Sets the hydration_value of this SettlementBalanceCalculator.


        :param hydration_value: The hydration_value of this SettlementBalanceCalculator.  # noqa: E501
        :type: float
        """

        self._hydration_value = hydration_value

    @property
    def id(self):
        """Gets the id of this SettlementBalanceCalculator.  # noqa: E501


        :return: The id of this SettlementBalanceCalculator.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SettlementBalanceCalculator.


        :param id: The id of this SettlementBalanceCalculator.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def method_analysis_depth(self):
        """Gets the method_analysis_depth of this SettlementBalanceCalculator.  # noqa: E501


        :return: The method_analysis_depth of this SettlementBalanceCalculator.  # noqa: E501
        :rtype: float
        """
        return self._method_analysis_depth

    @method_analysis_depth.setter
    def method_analysis_depth(self, method_analysis_depth):
        """Sets the method_analysis_depth of this SettlementBalanceCalculator.


        :param method_analysis_depth: The method_analysis_depth of this SettlementBalanceCalculator.  # noqa: E501
        :type: float
        """

        self._method_analysis_depth = method_analysis_depth

    @property
    def method_analysis_type(self):
        """Gets the method_analysis_type of this SettlementBalanceCalculator.  # noqa: E501


        :return: The method_analysis_type of this SettlementBalanceCalculator.  # noqa: E501
        :rtype: str
        """
        return self._method_analysis_type

    @method_analysis_type.setter
    def method_analysis_type(self, method_analysis_type):
        """Sets the method_analysis_type of this SettlementBalanceCalculator.


        :param method_analysis_type: The method_analysis_type of this SettlementBalanceCalculator.  # noqa: E501
        :type: str
        """

        self._method_analysis_type = method_analysis_type

    @property
    def name(self):
        """Gets the name of this SettlementBalanceCalculator.  # noqa: E501


        :return: The name of this SettlementBalanceCalculator.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SettlementBalanceCalculator.


        :param name: The name of this SettlementBalanceCalculator.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def norm_fertilizer(self):
        """Gets the norm_fertilizer of this SettlementBalanceCalculator.  # noqa: E501


        :return: The norm_fertilizer of this SettlementBalanceCalculator.  # noqa: E501
        :rtype: float
        """
        return self._norm_fertilizer

    @norm_fertilizer.setter
    def norm_fertilizer(self, norm_fertilizer):
        """Sets the norm_fertilizer of this SettlementBalanceCalculator.


        :param norm_fertilizer: The norm_fertilizer of this SettlementBalanceCalculator.  # noqa: E501
        :type: float
        """

        self._norm_fertilizer = norm_fertilizer

    @property
    def planned_yield(self):
        """Gets the planned_yield of this SettlementBalanceCalculator.  # noqa: E501


        :return: The planned_yield of this SettlementBalanceCalculator.  # noqa: E501
        :rtype: float
        """
        return self._planned_yield

    @planned_yield.setter
    def planned_yield(self, planned_yield):
        """Sets the planned_yield of this SettlementBalanceCalculator.


        :param planned_yield: The planned_yield of this SettlementBalanceCalculator.  # noqa: E501
        :type: float
        """

        self._planned_yield = planned_yield

    @property
    def predecessor_type(self):
        """Gets the predecessor_type of this SettlementBalanceCalculator.  # noqa: E501


        :return: The predecessor_type of this SettlementBalanceCalculator.  # noqa: E501
        :rtype: str
        """
        return self._predecessor_type

    @predecessor_type.setter
    def predecessor_type(self, predecessor_type):
        """Sets the predecessor_type of this SettlementBalanceCalculator.


        :param predecessor_type: The predecessor_type of this SettlementBalanceCalculator.  # noqa: E501
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
        """Gets the region_type of this SettlementBalanceCalculator.  # noqa: E501


        :return: The region_type of this SettlementBalanceCalculator.  # noqa: E501
        :rtype: int
        """
        return self._region_type

    @region_type.setter
    def region_type(self, region_type):
        """Sets the region_type of this SettlementBalanceCalculator.


        :param region_type: The region_type of this SettlementBalanceCalculator.  # noqa: E501
        :type: int
        """

        self._region_type = region_type

    @property
    def status(self):
        """Gets the status of this SettlementBalanceCalculator.  # noqa: E501


        :return: The status of this SettlementBalanceCalculator.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SettlementBalanceCalculator.


        :param status: The status of this SettlementBalanceCalculator.  # noqa: E501
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
    def test_data(self):
        """Gets the test_data of this SettlementBalanceCalculator.  # noqa: E501


        :return: The test_data of this SettlementBalanceCalculator.  # noqa: E501
        :rtype: float
        """
        return self._test_data

    @test_data.setter
    def test_data(self, test_data):
        """Sets the test_data of this SettlementBalanceCalculator.


        :param test_data: The test_data of this SettlementBalanceCalculator.  # noqa: E501
        :type: float
        """

        self._test_data = test_data

    @property
    def texture_type(self):
        """Gets the texture_type of this SettlementBalanceCalculator.  # noqa: E501


        :return: The texture_type of this SettlementBalanceCalculator.  # noqa: E501
        :rtype: str
        """
        return self._texture_type

    @texture_type.setter
    def texture_type(self, texture_type):
        """Sets the texture_type of this SettlementBalanceCalculator.


        :param texture_type: The texture_type of this SettlementBalanceCalculator.  # noqa: E501
        :type: str
        """
        allowed_values = ["LOAMY", "SABULOUS", "SANDY"]  # noqa: E501
        if (self._configuration.client_side_validation and
                texture_type not in allowed_values):
            raise ValueError(
                "Invalid value for `texture_type` ({0}), must be one of {1}"  # noqa: E501
                .format(texture_type, allowed_values)
            )

        self._texture_type = texture_type

    @property
    def update_date(self):
        """Gets the update_date of this SettlementBalanceCalculator.  # noqa: E501


        :return: The update_date of this SettlementBalanceCalculator.  # noqa: E501
        :rtype: datetime
        """
        return self._update_date

    @update_date.setter
    def update_date(self, update_date):
        """Sets the update_date of this SettlementBalanceCalculator.


        :param update_date: The update_date of this SettlementBalanceCalculator.  # noqa: E501
        :type: datetime
        """

        self._update_date = update_date

    @property
    def user_id(self):
        """Gets the user_id of this SettlementBalanceCalculator.  # noqa: E501


        :return: The user_id of this SettlementBalanceCalculator.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this SettlementBalanceCalculator.


        :param user_id: The user_id of this SettlementBalanceCalculator.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def year_type(self):
        """Gets the year_type of this SettlementBalanceCalculator.  # noqa: E501


        :return: The year_type of this SettlementBalanceCalculator.  # noqa: E501
        :rtype: str
        """
        return self._year_type

    @year_type.setter
    def year_type(self, year_type):
        """Sets the year_type of this SettlementBalanceCalculator.


        :param year_type: The year_type of this SettlementBalanceCalculator.  # noqa: E501
        :type: str
        """
        allowed_values = ["FIRST_YEAR", "SECOND_YEAR", "THIRD_YEAR"]  # noqa: E501
        if (self._configuration.client_side_validation and
                year_type not in allowed_values):
            raise ValueError(
                "Invalid value for `year_type` ({0}), must be one of {1}"  # noqa: E501
                .format(year_type, allowed_values)
            )

        self._year_type = year_type

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
        if issubclass(SettlementBalanceCalculator, dict):
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
        if not isinstance(other, SettlementBalanceCalculator):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SettlementBalanceCalculator):
            return True

        return self.to_dict() != other.to_dict()
