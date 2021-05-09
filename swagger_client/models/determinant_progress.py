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

class DeterminantProgress(object):
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
        'disease': 'AllOfDeterminantProgressDisease',
        'determinant': 'int',
        'name': 'str',
        'created_date': 'datetime',
        'user': 'int'
    }

    attribute_map = {
        'id': 'id',
        'disease': 'disease',
        'determinant': 'determinant',
        'name': 'name',
        'created_date': 'created_date',
        'user': 'user'
    }

    def __init__(self, id=None, disease=None, determinant=None, name=None, created_date=None, user=None):  # noqa: E501
        """DeterminantProgress - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._disease = None
        self._determinant = None
        self._name = None
        self._created_date = None
        self._user = None
        self.discriminator = None
        self.id = id
        self.disease = disease
        self.determinant = determinant
        self.name = name
        self.created_date = created_date
        self.user = user

    @property
    def id(self):
        """Gets the id of this DeterminantProgress.  # noqa: E501


        :return: The id of this DeterminantProgress.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeterminantProgress.


        :param id: The id of this DeterminantProgress.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def disease(self):
        """Gets the disease of this DeterminantProgress.  # noqa: E501


        :return: The disease of this DeterminantProgress.  # noqa: E501
        :rtype: AllOfDeterminantProgressDisease
        """
        return self._disease

    @disease.setter
    def disease(self, disease):
        """Sets the disease of this DeterminantProgress.


        :param disease: The disease of this DeterminantProgress.  # noqa: E501
        :type: AllOfDeterminantProgressDisease
        """

        self._disease = disease

    @property
    def determinant(self):
        """Gets the determinant of this DeterminantProgress.  # noqa: E501


        :return: The determinant of this DeterminantProgress.  # noqa: E501
        :rtype: int
        """
        return self._determinant

    @determinant.setter
    def determinant(self, determinant):
        """Sets the determinant of this DeterminantProgress.


        :param determinant: The determinant of this DeterminantProgress.  # noqa: E501
        :type: int
        """

        self._determinant = determinant

    @property
    def name(self):
        """Gets the name of this DeterminantProgress.  # noqa: E501


        :return: The name of this DeterminantProgress.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeterminantProgress.


        :param name: The name of this DeterminantProgress.  # noqa: E501
        :type: str
        """
        self._name = name

    @property
    def created_date(self):
        """Gets the created_date of this DeterminantProgress.  # noqa: E501


        :return: The created_date of this DeterminantProgress.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this DeterminantProgress.


        :param created_date: The created_date of this DeterminantProgress.  # noqa: E501
        :type: datetime
        """
        self._created_date = created_date

    @property
    def user(self):
        """Gets the user of this DeterminantProgress.  # noqa: E501


        :return: The user of this DeterminantProgress.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this DeterminantProgress.


        :param user: The user of this DeterminantProgress.  # noqa: E501
        :type: int
        """
        self._user = user

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
        if issubclass(DeterminantProgress, dict):
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
        if not isinstance(other, DeterminantProgress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
