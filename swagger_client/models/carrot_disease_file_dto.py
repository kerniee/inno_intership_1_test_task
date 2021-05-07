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


class CarrotDiseaseFileDto(object):
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
        'content_type': 'str',
        'disease_id': 'int',
        'file_name': 'str',
        'id': 'int'
    }

    attribute_map = {
        'content_type': 'contentType',
        'disease_id': 'diseaseId',
        'file_name': 'fileName',
        'id': 'id'
    }

    def __init__(self, content_type=None, disease_id=None, file_name=None, id=None, _configuration=None):  # noqa: E501
        """CarrotDiseaseFileDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._content_type = None
        self._disease_id = None
        self._file_name = None
        self._id = None
        self.discriminator = None

        if content_type is not None:
            self.content_type = content_type
        if disease_id is not None:
            self.disease_id = disease_id
        if file_name is not None:
            self.file_name = file_name
        if id is not None:
            self.id = id

    @property
    def content_type(self):
        """Gets the content_type of this CarrotDiseaseFileDto.  # noqa: E501


        :return: The content_type of this CarrotDiseaseFileDto.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this CarrotDiseaseFileDto.


        :param content_type: The content_type of this CarrotDiseaseFileDto.  # noqa: E501
        :type: str
        """

        self._content_type = content_type

    @property
    def disease_id(self):
        """Gets the disease_id of this CarrotDiseaseFileDto.  # noqa: E501


        :return: The disease_id of this CarrotDiseaseFileDto.  # noqa: E501
        :rtype: int
        """
        return self._disease_id

    @disease_id.setter
    def disease_id(self, disease_id):
        """Sets the disease_id of this CarrotDiseaseFileDto.


        :param disease_id: The disease_id of this CarrotDiseaseFileDto.  # noqa: E501
        :type: int
        """

        self._disease_id = disease_id

    @property
    def file_name(self):
        """Gets the file_name of this CarrotDiseaseFileDto.  # noqa: E501


        :return: The file_name of this CarrotDiseaseFileDto.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this CarrotDiseaseFileDto.


        :param file_name: The file_name of this CarrotDiseaseFileDto.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def id(self):
        """Gets the id of this CarrotDiseaseFileDto.  # noqa: E501


        :return: The id of this CarrotDiseaseFileDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CarrotDiseaseFileDto.


        :param id: The id of this CarrotDiseaseFileDto.  # noqa: E501
        :type: int
        """

        self._id = id

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
        if issubclass(CarrotDiseaseFileDto, dict):
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
        if not isinstance(other, CarrotDiseaseFileDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CarrotDiseaseFileDto):
            return True

        return self.to_dict() != other.to_dict()
