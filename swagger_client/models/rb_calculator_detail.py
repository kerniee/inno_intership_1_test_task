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

class RbCalculatorDetail(object):
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
        'is_done': 'bool',
        'fertilizer_n': 'AllOfRbCalculatorDetailFertilizerN',
        'fertilizer_p': 'AllOfRbCalculatorDetailFertilizerP',
        'fertilizer_k': 'AllOfRbCalculatorDetailFertilizerK',
        'region': 'AllOfRbCalculatorDetailRegion',
        'culture': 'AllOfRbCalculatorDetailCulture',
        'degree_of_soil_moisture': 'AllOfRbCalculatorDetailDegreeOfSoilMoisture',
        'analysis_method': 'str',
        'soil_sampling_depth': 'int',
        'fertilizer_action_year': 'AllOfRbCalculatorDetailFertilizerActionYear',
        'depth_of_arable_layer': 'AllOfRbCalculatorDetailDepthOfArableLayer',
        'mechanical_composition': 'AllOfRbCalculatorDetailMechanicalComposition',
        'planned_yield': 'float',
        'agrochemical_calculator': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'user': 'user',
        'creation_date': 'creation_date',
        'is_done': 'is_done',
        'fertilizer_n': 'fertilizer_n',
        'fertilizer_p': 'fertilizer_p',
        'fertilizer_k': 'fertilizer_k',
        'region': 'region',
        'culture': 'culture',
        'degree_of_soil_moisture': 'degree_of_soil_moisture',
        'analysis_method': 'analysis_method',
        'soil_sampling_depth': 'soil_sampling_depth',
        'fertilizer_action_year': 'fertilizer_action_year',
        'depth_of_arable_layer': 'depth_of_arable_layer',
        'mechanical_composition': 'mechanical_composition',
        'planned_yield': 'planned_yield',
        'agrochemical_calculator': 'agrochemical_calculator'
    }

    def __init__(self, id=None, name=None, user=None, creation_date=None, is_done=None, fertilizer_n=None, fertilizer_p=None, fertilizer_k=None, region=None, culture=None, degree_of_soil_moisture=None, analysis_method=None, soil_sampling_depth=None, fertilizer_action_year=None, depth_of_arable_layer=None, mechanical_composition=None, planned_yield=None, agrochemical_calculator=None):  # noqa: E501
        """RbCalculatorDetail - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._user = None
        self._creation_date = None
        self._is_done = None
        self._fertilizer_n = None
        self._fertilizer_p = None
        self._fertilizer_k = None
        self._region = None
        self._culture = None
        self._degree_of_soil_moisture = None
        self._analysis_method = None
        self._soil_sampling_depth = None
        self._fertilizer_action_year = None
        self._depth_of_arable_layer = None
        self._mechanical_composition = None
        self._planned_yield = None
        self._agrochemical_calculator = None
        self.discriminator = None
        self.id = id
        self.name = name
        self.user = user
        self.creation_date = creation_date
        self.is_done = is_done
        self.fertilizer_n = fertilizer_n
        self.fertilizer_p = fertilizer_p
        self.fertilizer_k = fertilizer_k
        self.region = region
        self.culture = culture
        self.degree_of_soil_moisture = degree_of_soil_moisture
        self.analysis_method = analysis_method
        self.soil_sampling_depth = soil_sampling_depth
        self.fertilizer_action_year = fertilizer_action_year
        self.depth_of_arable_layer = depth_of_arable_layer
        self.mechanical_composition = mechanical_composition
        self.planned_yield = planned_yield
        self.agrochemical_calculator = agrochemical_calculator

    @property
    def id(self):
        """Gets the id of this RbCalculatorDetail.  # noqa: E501


        :return: The id of this RbCalculatorDetail.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RbCalculatorDetail.


        :param id: The id of this RbCalculatorDetail.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this RbCalculatorDetail.  # noqa: E501


        :return: The name of this RbCalculatorDetail.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RbCalculatorDetail.


        :param name: The name of this RbCalculatorDetail.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def user(self):
        """Gets the user of this RbCalculatorDetail.  # noqa: E501


        :return: The user of this RbCalculatorDetail.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this RbCalculatorDetail.


        :param user: The user of this RbCalculatorDetail.  # noqa: E501
        :type: int
        """
        if user is None:
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    @property
    def creation_date(self):
        """Gets the creation_date of this RbCalculatorDetail.  # noqa: E501


        :return: The creation_date of this RbCalculatorDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this RbCalculatorDetail.


        :param creation_date: The creation_date of this RbCalculatorDetail.  # noqa: E501
        :type: datetime
        """
        if creation_date is None:
            raise ValueError("Invalid value for `creation_date`, must not be `None`")  # noqa: E501

        self._creation_date = creation_date

    @property
    def is_done(self):
        """Gets the is_done of this RbCalculatorDetail.  # noqa: E501


        :return: The is_done of this RbCalculatorDetail.  # noqa: E501
        :rtype: bool
        """
        return self._is_done

    @is_done.setter
    def is_done(self, is_done):
        """Sets the is_done of this RbCalculatorDetail.


        :param is_done: The is_done of this RbCalculatorDetail.  # noqa: E501
        :type: bool
        """
        if is_done is None:
            raise ValueError("Invalid value for `is_done`, must not be `None`")  # noqa: E501

        self._is_done = is_done

    @property
    def fertilizer_n(self):
        """Gets the fertilizer_n of this RbCalculatorDetail.  # noqa: E501


        :return: The fertilizer_n of this RbCalculatorDetail.  # noqa: E501
        :rtype: AllOfRbCalculatorDetailFertilizerN
        """
        return self._fertilizer_n

    @fertilizer_n.setter
    def fertilizer_n(self, fertilizer_n):
        """Sets the fertilizer_n of this RbCalculatorDetail.


        :param fertilizer_n: The fertilizer_n of this RbCalculatorDetail.  # noqa: E501
        :type: AllOfRbCalculatorDetailFertilizerN
        """
        if fertilizer_n is None:
            raise ValueError("Invalid value for `fertilizer_n`, must not be `None`")  # noqa: E501

        self._fertilizer_n = fertilizer_n

    @property
    def fertilizer_p(self):
        """Gets the fertilizer_p of this RbCalculatorDetail.  # noqa: E501


        :return: The fertilizer_p of this RbCalculatorDetail.  # noqa: E501
        :rtype: AllOfRbCalculatorDetailFertilizerP
        """
        return self._fertilizer_p

    @fertilizer_p.setter
    def fertilizer_p(self, fertilizer_p):
        """Sets the fertilizer_p of this RbCalculatorDetail.


        :param fertilizer_p: The fertilizer_p of this RbCalculatorDetail.  # noqa: E501
        :type: AllOfRbCalculatorDetailFertilizerP
        """
        if fertilizer_p is None:
            raise ValueError("Invalid value for `fertilizer_p`, must not be `None`")  # noqa: E501

        self._fertilizer_p = fertilizer_p

    @property
    def fertilizer_k(self):
        """Gets the fertilizer_k of this RbCalculatorDetail.  # noqa: E501


        :return: The fertilizer_k of this RbCalculatorDetail.  # noqa: E501
        :rtype: AllOfRbCalculatorDetailFertilizerK
        """
        return self._fertilizer_k

    @fertilizer_k.setter
    def fertilizer_k(self, fertilizer_k):
        """Sets the fertilizer_k of this RbCalculatorDetail.


        :param fertilizer_k: The fertilizer_k of this RbCalculatorDetail.  # noqa: E501
        :type: AllOfRbCalculatorDetailFertilizerK
        """
        if fertilizer_k is None:
            raise ValueError("Invalid value for `fertilizer_k`, must not be `None`")  # noqa: E501

        self._fertilizer_k = fertilizer_k

    @property
    def region(self):
        """Gets the region of this RbCalculatorDetail.  # noqa: E501


        :return: The region of this RbCalculatorDetail.  # noqa: E501
        :rtype: AllOfRbCalculatorDetailRegion
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this RbCalculatorDetail.


        :param region: The region of this RbCalculatorDetail.  # noqa: E501
        :type: AllOfRbCalculatorDetailRegion
        """
        if region is None:
            raise ValueError("Invalid value for `region`, must not be `None`")  # noqa: E501

        self._region = region

    @property
    def culture(self):
        """Gets the culture of this RbCalculatorDetail.  # noqa: E501


        :return: The culture of this RbCalculatorDetail.  # noqa: E501
        :rtype: AllOfRbCalculatorDetailCulture
        """
        return self._culture

    @culture.setter
    def culture(self, culture):
        """Sets the culture of this RbCalculatorDetail.


        :param culture: The culture of this RbCalculatorDetail.  # noqa: E501
        :type: AllOfRbCalculatorDetailCulture
        """
        if culture is None:
            raise ValueError("Invalid value for `culture`, must not be `None`")  # noqa: E501

        self._culture = culture

    @property
    def degree_of_soil_moisture(self):
        """Gets the degree_of_soil_moisture of this RbCalculatorDetail.  # noqa: E501


        :return: The degree_of_soil_moisture of this RbCalculatorDetail.  # noqa: E501
        :rtype: AllOfRbCalculatorDetailDegreeOfSoilMoisture
        """
        return self._degree_of_soil_moisture

    @degree_of_soil_moisture.setter
    def degree_of_soil_moisture(self, degree_of_soil_moisture):
        """Sets the degree_of_soil_moisture of this RbCalculatorDetail.


        :param degree_of_soil_moisture: The degree_of_soil_moisture of this RbCalculatorDetail.  # noqa: E501
        :type: AllOfRbCalculatorDetailDegreeOfSoilMoisture
        """
        if degree_of_soil_moisture is None:
            raise ValueError("Invalid value for `degree_of_soil_moisture`, must not be `None`")  # noqa: E501

        self._degree_of_soil_moisture = degree_of_soil_moisture

    @property
    def analysis_method(self):
        """Gets the analysis_method of this RbCalculatorDetail.  # noqa: E501


        :return: The analysis_method of this RbCalculatorDetail.  # noqa: E501
        :rtype: str
        """
        return self._analysis_method

    @analysis_method.setter
    def analysis_method(self, analysis_method):
        """Sets the analysis_method of this RbCalculatorDetail.


        :param analysis_method: The analysis_method of this RbCalculatorDetail.  # noqa: E501
        :type: str
        """
        if analysis_method is None:
            raise ValueError("Invalid value for `analysis_method`, must not be `None`")  # noqa: E501
        allowed_values = ["kirsanov", "chirikov", "machigin"]  # noqa: E501
        if analysis_method not in allowed_values:
            raise ValueError(
                "Invalid value for `analysis_method` ({0}), must be one of {1}"  # noqa: E501
                .format(analysis_method, allowed_values)
            )

        self._analysis_method = analysis_method

    @property
    def soil_sampling_depth(self):
        """Gets the soil_sampling_depth of this RbCalculatorDetail.  # noqa: E501


        :return: The soil_sampling_depth of this RbCalculatorDetail.  # noqa: E501
        :rtype: int
        """
        return self._soil_sampling_depth

    @soil_sampling_depth.setter
    def soil_sampling_depth(self, soil_sampling_depth):
        """Sets the soil_sampling_depth of this RbCalculatorDetail.


        :param soil_sampling_depth: The soil_sampling_depth of this RbCalculatorDetail.  # noqa: E501
        :type: int
        """
        if soil_sampling_depth is None:
            raise ValueError("Invalid value for `soil_sampling_depth`, must not be `None`")  # noqa: E501

        self._soil_sampling_depth = soil_sampling_depth

    @property
    def fertilizer_action_year(self):
        """Gets the fertilizer_action_year of this RbCalculatorDetail.  # noqa: E501


        :return: The fertilizer_action_year of this RbCalculatorDetail.  # noqa: E501
        :rtype: AllOfRbCalculatorDetailFertilizerActionYear
        """
        return self._fertilizer_action_year

    @fertilizer_action_year.setter
    def fertilizer_action_year(self, fertilizer_action_year):
        """Sets the fertilizer_action_year of this RbCalculatorDetail.


        :param fertilizer_action_year: The fertilizer_action_year of this RbCalculatorDetail.  # noqa: E501
        :type: AllOfRbCalculatorDetailFertilizerActionYear
        """
        if fertilizer_action_year is None:
            raise ValueError("Invalid value for `fertilizer_action_year`, must not be `None`")  # noqa: E501

        self._fertilizer_action_year = fertilizer_action_year

    @property
    def depth_of_arable_layer(self):
        """Gets the depth_of_arable_layer of this RbCalculatorDetail.  # noqa: E501


        :return: The depth_of_arable_layer of this RbCalculatorDetail.  # noqa: E501
        :rtype: AllOfRbCalculatorDetailDepthOfArableLayer
        """
        return self._depth_of_arable_layer

    @depth_of_arable_layer.setter
    def depth_of_arable_layer(self, depth_of_arable_layer):
        """Sets the depth_of_arable_layer of this RbCalculatorDetail.


        :param depth_of_arable_layer: The depth_of_arable_layer of this RbCalculatorDetail.  # noqa: E501
        :type: AllOfRbCalculatorDetailDepthOfArableLayer
        """
        if depth_of_arable_layer is None:
            raise ValueError("Invalid value for `depth_of_arable_layer`, must not be `None`")  # noqa: E501

        self._depth_of_arable_layer = depth_of_arable_layer

    @property
    def mechanical_composition(self):
        """Gets the mechanical_composition of this RbCalculatorDetail.  # noqa: E501


        :return: The mechanical_composition of this RbCalculatorDetail.  # noqa: E501
        :rtype: AllOfRbCalculatorDetailMechanicalComposition
        """
        return self._mechanical_composition

    @mechanical_composition.setter
    def mechanical_composition(self, mechanical_composition):
        """Sets the mechanical_composition of this RbCalculatorDetail.


        :param mechanical_composition: The mechanical_composition of this RbCalculatorDetail.  # noqa: E501
        :type: AllOfRbCalculatorDetailMechanicalComposition
        """
        if mechanical_composition is None:
            raise ValueError("Invalid value for `mechanical_composition`, must not be `None`")  # noqa: E501

        self._mechanical_composition = mechanical_composition

    @property
    def planned_yield(self):
        """Gets the planned_yield of this RbCalculatorDetail.  # noqa: E501


        :return: The planned_yield of this RbCalculatorDetail.  # noqa: E501
        :rtype: float
        """
        return self._planned_yield

    @planned_yield.setter
    def planned_yield(self, planned_yield):
        """Sets the planned_yield of this RbCalculatorDetail.


        :param planned_yield: The planned_yield of this RbCalculatorDetail.  # noqa: E501
        :type: float
        """
        if planned_yield is None:
            raise ValueError("Invalid value for `planned_yield`, must not be `None`")  # noqa: E501

        self._planned_yield = planned_yield

    @property
    def agrochemical_calculator(self):
        """Gets the agrochemical_calculator of this RbCalculatorDetail.  # noqa: E501


        :return: The agrochemical_calculator of this RbCalculatorDetail.  # noqa: E501
        :rtype: int
        """
        return self._agrochemical_calculator

    @agrochemical_calculator.setter
    def agrochemical_calculator(self, agrochemical_calculator):
        """Sets the agrochemical_calculator of this RbCalculatorDetail.


        :param agrochemical_calculator: The agrochemical_calculator of this RbCalculatorDetail.  # noqa: E501
        :type: int
        """
        if agrochemical_calculator is None:
            raise ValueError("Invalid value for `agrochemical_calculator`, must not be `None`")  # noqa: E501

        self._agrochemical_calculator = agrochemical_calculator

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
        if issubclass(RbCalculatorDetail, dict):
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
        if not isinstance(other, RbCalculatorDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other