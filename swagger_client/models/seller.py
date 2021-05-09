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

class Seller(object):
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
        'address': 'str',
        'contact_person': 'str',
        'site': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'address': 'address',
        'contact_person': 'contact_person',
        'site': 'site'
    }

    def __init__(self, id=None, name=None, address=None, contact_person=None, site=None):  # noqa: E501
        """Seller - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._address = None
        self._contact_person = None
        self._site = None
        self.discriminator = None
        self.id = id
        self.name = name
        if address is not None:
            self.address = address
        if contact_person is not None:
            self.contact_person = contact_person
        if site is not None:
            self.site = site

    @property
    def id(self):
        """Gets the id of this Seller.  # noqa: E501


        :return: The id of this Seller.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Seller.


        :param id: The id of this Seller.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this Seller.  # noqa: E501


        :return: The name of this Seller.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Seller.


        :param name: The name of this Seller.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def address(self):
        """Gets the address of this Seller.  # noqa: E501


        :return: The address of this Seller.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Seller.


        :param address: The address of this Seller.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def contact_person(self):
        """Gets the contact_person of this Seller.  # noqa: E501


        :return: The contact_person of this Seller.  # noqa: E501
        :rtype: str
        """
        return self._contact_person

    @contact_person.setter
    def contact_person(self, contact_person):
        """Sets the contact_person of this Seller.


        :param contact_person: The contact_person of this Seller.  # noqa: E501
        :type: str
        """

        self._contact_person = contact_person

    @property
    def site(self):
        """Gets the site of this Seller.  # noqa: E501


        :return: The site of this Seller.  # noqa: E501
        :rtype: str
        """
        return self._site

    @site.setter
    def site(self, site):
        """Sets the site of this Seller.


        :param site: The site of this Seller.  # noqa: E501
        :type: str
        """

        self._site = site

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
        if issubclass(Seller, dict):
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
        if not isinstance(other, Seller):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
