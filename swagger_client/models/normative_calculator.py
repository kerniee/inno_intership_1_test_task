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

class NormativeCalculator(object):
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
        'fertilizer_n': 'int',
        'fertilizer_p': 'int',
        'fertilizer_k': 'int',
        'culture': 'int',
        'region': 'int',
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
        'culture': 'culture',
        'region': 'region',
        'agrochemical_calculator': 'agrochemical_calculator'
    }

    def __init__(self, id=None, name=None, user=None, creation_date=None, is_done=None, fertilizer_n=None, fertilizer_p=None, fertilizer_k=None, culture=None, region=None, agrochemical_calculator=None):  # noqa: E501
        """NormativeCalculator - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._user = None
        self._creation_date = None
        self._is_done = None
        self._fertilizer_n = None
        self._fertilizer_p = None
        self._fertilizer_k = None
        self._culture = None
        self._region = None
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
        self.culture = culture
        self.region = region
        self.agrochemical_calculator = agrochemical_calculator

    @property
    def id(self):
        """Gets the id of this NormativeCalculator.  # noqa: E501


        :return: The id of this NormativeCalculator.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NormativeCalculator.


        :param id: The id of this NormativeCalculator.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this NormativeCalculator.  # noqa: E501


        :return: The name of this NormativeCalculator.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NormativeCalculator.


        :param name: The name of this NormativeCalculator.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def user(self):
        """Gets the user of this NormativeCalculator.  # noqa: E501


        :return: The user of this NormativeCalculator.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this NormativeCalculator.


        :param user: The user of this NormativeCalculator.  # noqa: E501
        :type: int
        """
        if user is None:
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    @property
    def creation_date(self):
        """Gets the creation_date of this NormativeCalculator.  # noqa: E501


        :return: The creation_date of this NormativeCalculator.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this NormativeCalculator.


        :param creation_date: The creation_date of this NormativeCalculator.  # noqa: E501
        :type: datetime
        """
        if creation_date is None:
            raise ValueError("Invalid value for `creation_date`, must not be `None`")  # noqa: E501

        self._creation_date = creation_date

    @property
    def is_done(self):
        """Gets the is_done of this NormativeCalculator.  # noqa: E501


        :return: The is_done of this NormativeCalculator.  # noqa: E501
        :rtype: bool
        """
        return self._is_done

    @is_done.setter
    def is_done(self, is_done):
        """Sets the is_done of this NormativeCalculator.


        :param is_done: The is_done of this NormativeCalculator.  # noqa: E501
        :type: bool
        """
        if is_done is None:
            raise ValueError("Invalid value for `is_done`, must not be `None`")  # noqa: E501

        self._is_done = is_done

    @property
    def fertilizer_n(self):
        """Gets the fertilizer_n of this NormativeCalculator.  # noqa: E501


        :return: The fertilizer_n of this NormativeCalculator.  # noqa: E501
        :rtype: int
        """
        return self._fertilizer_n

    @fertilizer_n.setter
    def fertilizer_n(self, fertilizer_n):
        """Sets the fertilizer_n of this NormativeCalculator.


        :param fertilizer_n: The fertilizer_n of this NormativeCalculator.  # noqa: E501
        :type: int
        """
        if fertilizer_n is None:
            raise ValueError("Invalid value for `fertilizer_n`, must not be `None`")  # noqa: E501

        self._fertilizer_n = fertilizer_n

    @property
    def fertilizer_p(self):
        """Gets the fertilizer_p of this NormativeCalculator.  # noqa: E501


        :return: The fertilizer_p of this NormativeCalculator.  # noqa: E501
        :rtype: int
        """
        return self._fertilizer_p

    @fertilizer_p.setter
    def fertilizer_p(self, fertilizer_p):
        """Sets the fertilizer_p of this NormativeCalculator.


        :param fertilizer_p: The fertilizer_p of this NormativeCalculator.  # noqa: E501
        :type: int
        """
        if fertilizer_p is None:
            raise ValueError("Invalid value for `fertilizer_p`, must not be `None`")  # noqa: E501

        self._fertilizer_p = fertilizer_p

    @property
    def fertilizer_k(self):
        """Gets the fertilizer_k of this NormativeCalculator.  # noqa: E501


        :return: The fertilizer_k of this NormativeCalculator.  # noqa: E501
        :rtype: int
        """
        return self._fertilizer_k

    @fertilizer_k.setter
    def fertilizer_k(self, fertilizer_k):
        """Sets the fertilizer_k of this NormativeCalculator.


        :param fertilizer_k: The fertilizer_k of this NormativeCalculator.  # noqa: E501
        :type: int
        """
        if fertilizer_k is None:
            raise ValueError("Invalid value for `fertilizer_k`, must not be `None`")  # noqa: E501

        self._fertilizer_k = fertilizer_k

    @property
    def culture(self):
        """Gets the culture of this NormativeCalculator.  # noqa: E501


        :return: The culture of this NormativeCalculator.  # noqa: E501
        :rtype: int
        """
        return self._culture

    @culture.setter
    def culture(self, culture):
        """Sets the culture of this NormativeCalculator.


        :param culture: The culture of this NormativeCalculator.  # noqa: E501
        :type: int
        """
        if culture is None:
            raise ValueError("Invalid value for `culture`, must not be `None`")  # noqa: E501

        self._culture = culture

    @property
    def region(self):
        """Gets the region of this NormativeCalculator.  # noqa: E501


        :return: The region of this NormativeCalculator.  # noqa: E501
        :rtype: int
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this NormativeCalculator.


        :param region: The region of this NormativeCalculator.  # noqa: E501
        :type: int
        """
        if region is None:
            raise ValueError("Invalid value for `region`, must not be `None`")  # noqa: E501

        self._region = region

    @property
    def agrochemical_calculator(self):
        """Gets the agrochemical_calculator of this NormativeCalculator.  # noqa: E501


        :return: The agrochemical_calculator of this NormativeCalculator.  # noqa: E501
        :rtype: int
        """
        return self._agrochemical_calculator

    @agrochemical_calculator.setter
    def agrochemical_calculator(self, agrochemical_calculator):
        """Sets the agrochemical_calculator of this NormativeCalculator.


        :param agrochemical_calculator: The agrochemical_calculator of this NormativeCalculator.  # noqa: E501
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
        if issubclass(NormativeCalculator, dict):
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
        if not isinstance(other, NormativeCalculator):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other