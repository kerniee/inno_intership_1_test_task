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

class RosselkhozBankSetDeliveryMethodForAgrochemicalAnalysisRequestCommand(object):
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
        'delivery_method': 'str',
        'pickup_address': 'str'
    }

    attribute_map = {
        'delivery_method': 'delivery_method',
        'pickup_address': 'pickup_address'
    }

    def __init__(self, delivery_method=None, pickup_address=None):  # noqa: E501
        """RosselkhozBankSetDeliveryMethodForAgrochemicalAnalysisRequestCommand - a model defined in Swagger"""  # noqa: E501
        self._delivery_method = None
        self._pickup_address = None
        self.discriminator = None
        self.delivery_method = delivery_method
        self.pickup_address = pickup_address

    @property
    def delivery_method(self):
        """Gets the delivery_method of this RosselkhozBankSetDeliveryMethodForAgrochemicalAnalysisRequestCommand.  # noqa: E501


        :return: The delivery_method of this RosselkhozBankSetDeliveryMethodForAgrochemicalAnalysisRequestCommand.  # noqa: E501
        :rtype: str
        """
        return self._delivery_method

    @delivery_method.setter
    def delivery_method(self, delivery_method):
        """Sets the delivery_method of this RosselkhozBankSetDeliveryMethodForAgrochemicalAnalysisRequestCommand.


        :param delivery_method: The delivery_method of this RosselkhozBankSetDeliveryMethodForAgrochemicalAnalysisRequestCommand.  # noqa: E501
        :type: str
        """
        if delivery_method is None:
            raise ValueError("Invalid value for `delivery_method`, must not be `None`")  # noqa: E501
        allowed_values = ["self", "courier"]  # noqa: E501
        if delivery_method not in allowed_values:
            raise ValueError(
                "Invalid value for `delivery_method` ({0}), must be one of {1}"  # noqa: E501
                .format(delivery_method, allowed_values)
            )

        self._delivery_method = delivery_method

    @property
    def pickup_address(self):
        """Gets the pickup_address of this RosselkhozBankSetDeliveryMethodForAgrochemicalAnalysisRequestCommand.  # noqa: E501


        :return: The pickup_address of this RosselkhozBankSetDeliveryMethodForAgrochemicalAnalysisRequestCommand.  # noqa: E501
        :rtype: str
        """
        return self._pickup_address

    @pickup_address.setter
    def pickup_address(self, pickup_address):
        """Sets the pickup_address of this RosselkhozBankSetDeliveryMethodForAgrochemicalAnalysisRequestCommand.


        :param pickup_address: The pickup_address of this RosselkhozBankSetDeliveryMethodForAgrochemicalAnalysisRequestCommand.  # noqa: E501
        :type: str
        """
        if pickup_address is None:
            raise ValueError("Invalid value for `pickup_address`, must not be `None`")  # noqa: E501

        self._pickup_address = pickup_address

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
        if issubclass(RosselkhozBankSetDeliveryMethodForAgrochemicalAnalysisRequestCommand, dict):
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
        if not isinstance(other, RosselkhozBankSetDeliveryMethodForAgrochemicalAnalysisRequestCommand):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
