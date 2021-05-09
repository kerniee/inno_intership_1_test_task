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

class FluidCalculatorDetail(object):
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
        'consumption_rate_from_catalog': 'AllOfFluidCalculatorDetailConsumptionRateFromCatalog',
        'name': 'str',
        'creation_date': 'datetime',
        'is_done': 'bool',
        'fluid_consumption_rate_for_nozzle': 'float',
        'number_of_nozzles_on_the_rod': 'int',
        'rod_width': 'float',
        'actual_spraying_speed': 'float',
        'fluid_consumption_rate_for_rod': 'float',
        'rate_of_use': 'float',
        'fluid_consumption': 'float',
        'rate_of_use_of_plant_protection': 'float',
        'user': 'int',
        'plant_protection_product_application': 'int'
    }

    attribute_map = {
        'id': 'id',
        'consumption_rate_from_catalog': 'consumption_rate_from_catalog',
        'name': 'name',
        'creation_date': 'creation_date',
        'is_done': 'is_done',
        'fluid_consumption_rate_for_nozzle': 'fluid_consumption_rate_for_nozzle',
        'number_of_nozzles_on_the_rod': 'number_of_nozzles_on_the_rod',
        'rod_width': 'rod_width',
        'actual_spraying_speed': 'actual_spraying_speed',
        'fluid_consumption_rate_for_rod': 'fluid_consumption_rate_for_rod',
        'rate_of_use': 'rate_of_use',
        'fluid_consumption': 'fluid_consumption',
        'rate_of_use_of_plant_protection': 'rate_of_use_of_plant_protection',
        'user': 'user',
        'plant_protection_product_application': 'plant_protection_product_application'
    }

    def __init__(self, id=None, consumption_rate_from_catalog=None, name=None, creation_date=None, is_done=None, fluid_consumption_rate_for_nozzle=None, number_of_nozzles_on_the_rod=None, rod_width=None, actual_spraying_speed=None, fluid_consumption_rate_for_rod=None, rate_of_use=None, fluid_consumption=None, rate_of_use_of_plant_protection=None, user=None, plant_protection_product_application=None):  # noqa: E501
        """FluidCalculatorDetail - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._consumption_rate_from_catalog = None
        self._name = None
        self._creation_date = None
        self._is_done = None
        self._fluid_consumption_rate_for_nozzle = None
        self._number_of_nozzles_on_the_rod = None
        self._rod_width = None
        self._actual_spraying_speed = None
        self._fluid_consumption_rate_for_rod = None
        self._rate_of_use = None
        self._fluid_consumption = None
        self._rate_of_use_of_plant_protection = None
        self._user = None
        self._plant_protection_product_application = None
        self.discriminator = None
        self.id = id
        self.consumption_rate_from_catalog = consumption_rate_from_catalog
        self.name = name
        self.creation_date = creation_date
        self.is_done = is_done
        self.fluid_consumption_rate_for_nozzle = fluid_consumption_rate_for_nozzle
        self.number_of_nozzles_on_the_rod = number_of_nozzles_on_the_rod
        self.rod_width = rod_width
        self.actual_spraying_speed = actual_spraying_speed
        self.fluid_consumption_rate_for_rod = fluid_consumption_rate_for_rod
        self.rate_of_use = rate_of_use
        self.fluid_consumption = fluid_consumption
        self.rate_of_use_of_plant_protection = rate_of_use_of_plant_protection
        self.user = user
        self.plant_protection_product_application = plant_protection_product_application

    @property
    def id(self):
        """Gets the id of this FluidCalculatorDetail.  # noqa: E501


        :return: The id of this FluidCalculatorDetail.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FluidCalculatorDetail.


        :param id: The id of this FluidCalculatorDetail.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def consumption_rate_from_catalog(self):
        """Gets the consumption_rate_from_catalog of this FluidCalculatorDetail.  # noqa: E501


        :return: The consumption_rate_from_catalog of this FluidCalculatorDetail.  # noqa: E501
        :rtype: AllOfFluidCalculatorDetailConsumptionRateFromCatalog
        """
        return self._consumption_rate_from_catalog

    @consumption_rate_from_catalog.setter
    def consumption_rate_from_catalog(self, consumption_rate_from_catalog):
        """Sets the consumption_rate_from_catalog of this FluidCalculatorDetail.


        :param consumption_rate_from_catalog: The consumption_rate_from_catalog of this FluidCalculatorDetail.  # noqa: E501
        :type: AllOfFluidCalculatorDetailConsumptionRateFromCatalog
        """
        if consumption_rate_from_catalog is None:
            raise ValueError("Invalid value for `consumption_rate_from_catalog`, must not be `None`")  # noqa: E501

        self._consumption_rate_from_catalog = consumption_rate_from_catalog

    @property
    def name(self):
        """Gets the name of this FluidCalculatorDetail.  # noqa: E501


        :return: The name of this FluidCalculatorDetail.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FluidCalculatorDetail.


        :param name: The name of this FluidCalculatorDetail.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def creation_date(self):
        """Gets the creation_date of this FluidCalculatorDetail.  # noqa: E501


        :return: The creation_date of this FluidCalculatorDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this FluidCalculatorDetail.


        :param creation_date: The creation_date of this FluidCalculatorDetail.  # noqa: E501
        :type: datetime
        """
        if creation_date is None:
            raise ValueError("Invalid value for `creation_date`, must not be `None`")  # noqa: E501

        self._creation_date = creation_date

    @property
    def is_done(self):
        """Gets the is_done of this FluidCalculatorDetail.  # noqa: E501


        :return: The is_done of this FluidCalculatorDetail.  # noqa: E501
        :rtype: bool
        """
        return self._is_done

    @is_done.setter
    def is_done(self, is_done):
        """Sets the is_done of this FluidCalculatorDetail.


        :param is_done: The is_done of this FluidCalculatorDetail.  # noqa: E501
        :type: bool
        """
        if is_done is None:
            raise ValueError("Invalid value for `is_done`, must not be `None`")  # noqa: E501

        self._is_done = is_done

    @property
    def fluid_consumption_rate_for_nozzle(self):
        """Gets the fluid_consumption_rate_for_nozzle of this FluidCalculatorDetail.  # noqa: E501


        :return: The fluid_consumption_rate_for_nozzle of this FluidCalculatorDetail.  # noqa: E501
        :rtype: float
        """
        return self._fluid_consumption_rate_for_nozzle

    @fluid_consumption_rate_for_nozzle.setter
    def fluid_consumption_rate_for_nozzle(self, fluid_consumption_rate_for_nozzle):
        """Sets the fluid_consumption_rate_for_nozzle of this FluidCalculatorDetail.


        :param fluid_consumption_rate_for_nozzle: The fluid_consumption_rate_for_nozzle of this FluidCalculatorDetail.  # noqa: E501
        :type: float
        """
        if fluid_consumption_rate_for_nozzle is None:
            raise ValueError("Invalid value for `fluid_consumption_rate_for_nozzle`, must not be `None`")  # noqa: E501

        self._fluid_consumption_rate_for_nozzle = fluid_consumption_rate_for_nozzle

    @property
    def number_of_nozzles_on_the_rod(self):
        """Gets the number_of_nozzles_on_the_rod of this FluidCalculatorDetail.  # noqa: E501


        :return: The number_of_nozzles_on_the_rod of this FluidCalculatorDetail.  # noqa: E501
        :rtype: int
        """
        return self._number_of_nozzles_on_the_rod

    @number_of_nozzles_on_the_rod.setter
    def number_of_nozzles_on_the_rod(self, number_of_nozzles_on_the_rod):
        """Sets the number_of_nozzles_on_the_rod of this FluidCalculatorDetail.


        :param number_of_nozzles_on_the_rod: The number_of_nozzles_on_the_rod of this FluidCalculatorDetail.  # noqa: E501
        :type: int
        """
        if number_of_nozzles_on_the_rod is None:
            raise ValueError("Invalid value for `number_of_nozzles_on_the_rod`, must not be `None`")  # noqa: E501

        self._number_of_nozzles_on_the_rod = number_of_nozzles_on_the_rod

    @property
    def rod_width(self):
        """Gets the rod_width of this FluidCalculatorDetail.  # noqa: E501


        :return: The rod_width of this FluidCalculatorDetail.  # noqa: E501
        :rtype: float
        """
        return self._rod_width

    @rod_width.setter
    def rod_width(self, rod_width):
        """Sets the rod_width of this FluidCalculatorDetail.


        :param rod_width: The rod_width of this FluidCalculatorDetail.  # noqa: E501
        :type: float
        """
        if rod_width is None:
            raise ValueError("Invalid value for `rod_width`, must not be `None`")  # noqa: E501

        self._rod_width = rod_width

    @property
    def actual_spraying_speed(self):
        """Gets the actual_spraying_speed of this FluidCalculatorDetail.  # noqa: E501


        :return: The actual_spraying_speed of this FluidCalculatorDetail.  # noqa: E501
        :rtype: float
        """
        return self._actual_spraying_speed

    @actual_spraying_speed.setter
    def actual_spraying_speed(self, actual_spraying_speed):
        """Sets the actual_spraying_speed of this FluidCalculatorDetail.


        :param actual_spraying_speed: The actual_spraying_speed of this FluidCalculatorDetail.  # noqa: E501
        :type: float
        """
        if actual_spraying_speed is None:
            raise ValueError("Invalid value for `actual_spraying_speed`, must not be `None`")  # noqa: E501

        self._actual_spraying_speed = actual_spraying_speed

    @property
    def fluid_consumption_rate_for_rod(self):
        """Gets the fluid_consumption_rate_for_rod of this FluidCalculatorDetail.  # noqa: E501


        :return: The fluid_consumption_rate_for_rod of this FluidCalculatorDetail.  # noqa: E501
        :rtype: float
        """
        return self._fluid_consumption_rate_for_rod

    @fluid_consumption_rate_for_rod.setter
    def fluid_consumption_rate_for_rod(self, fluid_consumption_rate_for_rod):
        """Sets the fluid_consumption_rate_for_rod of this FluidCalculatorDetail.


        :param fluid_consumption_rate_for_rod: The fluid_consumption_rate_for_rod of this FluidCalculatorDetail.  # noqa: E501
        :type: float
        """
        if fluid_consumption_rate_for_rod is None:
            raise ValueError("Invalid value for `fluid_consumption_rate_for_rod`, must not be `None`")  # noqa: E501

        self._fluid_consumption_rate_for_rod = fluid_consumption_rate_for_rod

    @property
    def rate_of_use(self):
        """Gets the rate_of_use of this FluidCalculatorDetail.  # noqa: E501


        :return: The rate_of_use of this FluidCalculatorDetail.  # noqa: E501
        :rtype: float
        """
        return self._rate_of_use

    @rate_of_use.setter
    def rate_of_use(self, rate_of_use):
        """Sets the rate_of_use of this FluidCalculatorDetail.


        :param rate_of_use: The rate_of_use of this FluidCalculatorDetail.  # noqa: E501
        :type: float
        """
        if rate_of_use is None:
            raise ValueError("Invalid value for `rate_of_use`, must not be `None`")  # noqa: E501

        self._rate_of_use = rate_of_use

    @property
    def fluid_consumption(self):
        """Gets the fluid_consumption of this FluidCalculatorDetail.  # noqa: E501


        :return: The fluid_consumption of this FluidCalculatorDetail.  # noqa: E501
        :rtype: float
        """
        return self._fluid_consumption

    @fluid_consumption.setter
    def fluid_consumption(self, fluid_consumption):
        """Sets the fluid_consumption of this FluidCalculatorDetail.


        :param fluid_consumption: The fluid_consumption of this FluidCalculatorDetail.  # noqa: E501
        :type: float
        """
        if fluid_consumption is None:
            raise ValueError("Invalid value for `fluid_consumption`, must not be `None`")  # noqa: E501

        self._fluid_consumption = fluid_consumption

    @property
    def rate_of_use_of_plant_protection(self):
        """Gets the rate_of_use_of_plant_protection of this FluidCalculatorDetail.  # noqa: E501


        :return: The rate_of_use_of_plant_protection of this FluidCalculatorDetail.  # noqa: E501
        :rtype: float
        """
        return self._rate_of_use_of_plant_protection

    @rate_of_use_of_plant_protection.setter
    def rate_of_use_of_plant_protection(self, rate_of_use_of_plant_protection):
        """Sets the rate_of_use_of_plant_protection of this FluidCalculatorDetail.


        :param rate_of_use_of_plant_protection: The rate_of_use_of_plant_protection of this FluidCalculatorDetail.  # noqa: E501
        :type: float
        """
        if rate_of_use_of_plant_protection is None:
            raise ValueError("Invalid value for `rate_of_use_of_plant_protection`, must not be `None`")  # noqa: E501

        self._rate_of_use_of_plant_protection = rate_of_use_of_plant_protection

    @property
    def user(self):
        """Gets the user of this FluidCalculatorDetail.  # noqa: E501


        :return: The user of this FluidCalculatorDetail.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this FluidCalculatorDetail.


        :param user: The user of this FluidCalculatorDetail.  # noqa: E501
        :type: int
        """
        if user is None:
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    @property
    def plant_protection_product_application(self):
        """Gets the plant_protection_product_application of this FluidCalculatorDetail.  # noqa: E501


        :return: The plant_protection_product_application of this FluidCalculatorDetail.  # noqa: E501
        :rtype: int
        """
        return self._plant_protection_product_application

    @plant_protection_product_application.setter
    def plant_protection_product_application(self, plant_protection_product_application):
        """Sets the plant_protection_product_application of this FluidCalculatorDetail.


        :param plant_protection_product_application: The plant_protection_product_application of this FluidCalculatorDetail.  # noqa: E501
        :type: int
        """
        if plant_protection_product_application is None:
            raise ValueError("Invalid value for `plant_protection_product_application`, must not be `None`")  # noqa: E501

        self._plant_protection_product_application = plant_protection_product_application

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
        if issubclass(FluidCalculatorDetail, dict):
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
        if not isinstance(other, FluidCalculatorDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
