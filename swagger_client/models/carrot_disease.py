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


class CarrotDisease(object):
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
        'affected_area': 'str',
        'causes_of_occurrence': 'str',
        'control_measures': 'str',
        'culture': 'str',
        'diseases_ecology': 'str',
        'economic_threshold_of_harmfulness': 'str',
        'id': 'int',
        'leaves_signs': 'str',
        'name': 'str',
        'number': 'str',
        'pathogen': 'str',
        'pathogen_distribution_biology': 'str',
        'pathogen_morphology': 'str',
        'photo': 'str',
        'reproductive_organs_signs': 'str',
        'root_crop_signs': 'str',
        'root_system_signs': 'str',
        'seedlings_sings': 'str',
        'sickness': 'str',
        'stalks_signs': 'str',
        'sub_type': 'str',
        'type': 'str'
    }

    attribute_map = {
        'affected_area': 'affectedArea',
        'causes_of_occurrence': 'causesOfOccurrence',
        'control_measures': 'controlMeasures',
        'culture': 'culture',
        'diseases_ecology': 'diseasesEcology',
        'economic_threshold_of_harmfulness': 'economicThresholdOfHarmfulness',
        'id': 'id',
        'leaves_signs': 'leavesSigns',
        'name': 'name',
        'number': 'number',
        'pathogen': 'pathogen',
        'pathogen_distribution_biology': 'pathogenDistributionBiology',
        'pathogen_morphology': 'pathogenMorphology',
        'photo': 'photo',
        'reproductive_organs_signs': 'reproductiveOrgansSigns',
        'root_crop_signs': 'rootCropSigns',
        'root_system_signs': 'rootSystemSigns',
        'seedlings_sings': 'seedlingsSings',
        'sickness': 'sickness',
        'stalks_signs': 'stalksSigns',
        'sub_type': 'subType',
        'type': 'type'
    }

    def __init__(self, affected_area=None, causes_of_occurrence=None, control_measures=None, culture=None, diseases_ecology=None, economic_threshold_of_harmfulness=None, id=None, leaves_signs=None, name=None, number=None, pathogen=None, pathogen_distribution_biology=None, pathogen_morphology=None, photo=None, reproductive_organs_signs=None, root_crop_signs=None, root_system_signs=None, seedlings_sings=None, sickness=None, stalks_signs=None, sub_type=None, type=None, _configuration=None):  # noqa: E501
        """CarrotDisease - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._affected_area = None
        self._causes_of_occurrence = None
        self._control_measures = None
        self._culture = None
        self._diseases_ecology = None
        self._economic_threshold_of_harmfulness = None
        self._id = None
        self._leaves_signs = None
        self._name = None
        self._number = None
        self._pathogen = None
        self._pathogen_distribution_biology = None
        self._pathogen_morphology = None
        self._photo = None
        self._reproductive_organs_signs = None
        self._root_crop_signs = None
        self._root_system_signs = None
        self._seedlings_sings = None
        self._sickness = None
        self._stalks_signs = None
        self._sub_type = None
        self._type = None
        self.discriminator = None

        if affected_area is not None:
            self.affected_area = affected_area
        if causes_of_occurrence is not None:
            self.causes_of_occurrence = causes_of_occurrence
        if control_measures is not None:
            self.control_measures = control_measures
        if culture is not None:
            self.culture = culture
        if diseases_ecology is not None:
            self.diseases_ecology = diseases_ecology
        if economic_threshold_of_harmfulness is not None:
            self.economic_threshold_of_harmfulness = economic_threshold_of_harmfulness
        if id is not None:
            self.id = id
        if leaves_signs is not None:
            self.leaves_signs = leaves_signs
        if name is not None:
            self.name = name
        if number is not None:
            self.number = number
        if pathogen is not None:
            self.pathogen = pathogen
        if pathogen_distribution_biology is not None:
            self.pathogen_distribution_biology = pathogen_distribution_biology
        if pathogen_morphology is not None:
            self.pathogen_morphology = pathogen_morphology
        if photo is not None:
            self.photo = photo
        if reproductive_organs_signs is not None:
            self.reproductive_organs_signs = reproductive_organs_signs
        if root_crop_signs is not None:
            self.root_crop_signs = root_crop_signs
        if root_system_signs is not None:
            self.root_system_signs = root_system_signs
        if seedlings_sings is not None:
            self.seedlings_sings = seedlings_sings
        if sickness is not None:
            self.sickness = sickness
        if stalks_signs is not None:
            self.stalks_signs = stalks_signs
        if sub_type is not None:
            self.sub_type = sub_type
        if type is not None:
            self.type = type

    @property
    def affected_area(self):
        """Gets the affected_area of this CarrotDisease.  # noqa: E501


        :return: The affected_area of this CarrotDisease.  # noqa: E501
        :rtype: str
        """
        return self._affected_area

    @affected_area.setter
    def affected_area(self, affected_area):
        """Sets the affected_area of this CarrotDisease.


        :param affected_area: The affected_area of this CarrotDisease.  # noqa: E501
        :type: str
        """

        self._affected_area = affected_area

    @property
    def causes_of_occurrence(self):
        """Gets the causes_of_occurrence of this CarrotDisease.  # noqa: E501


        :return: The causes_of_occurrence of this CarrotDisease.  # noqa: E501
        :rtype: str
        """
        return self._causes_of_occurrence

    @causes_of_occurrence.setter
    def causes_of_occurrence(self, causes_of_occurrence):
        """Sets the causes_of_occurrence of this CarrotDisease.


        :param causes_of_occurrence: The causes_of_occurrence of this CarrotDisease.  # noqa: E501
        :type: str
        """

        self._causes_of_occurrence = causes_of_occurrence

    @property
    def control_measures(self):
        """Gets the control_measures of this CarrotDisease.  # noqa: E501


        :return: The control_measures of this CarrotDisease.  # noqa: E501
        :rtype: str
        """
        return self._control_measures

    @control_measures.setter
    def control_measures(self, control_measures):
        """Sets the control_measures of this CarrotDisease.


        :param control_measures: The control_measures of this CarrotDisease.  # noqa: E501
        :type: str
        """

        self._control_measures = control_measures

    @property
    def culture(self):
        """Gets the culture of this CarrotDisease.  # noqa: E501


        :return: The culture of this CarrotDisease.  # noqa: E501
        :rtype: str
        """
        return self._culture

    @culture.setter
    def culture(self, culture):
        """Sets the culture of this CarrotDisease.


        :param culture: The culture of this CarrotDisease.  # noqa: E501
        :type: str
        """

        self._culture = culture

    @property
    def diseases_ecology(self):
        """Gets the diseases_ecology of this CarrotDisease.  # noqa: E501


        :return: The diseases_ecology of this CarrotDisease.  # noqa: E501
        :rtype: str
        """
        return self._diseases_ecology

    @diseases_ecology.setter
    def diseases_ecology(self, diseases_ecology):
        """Sets the diseases_ecology of this CarrotDisease.


        :param diseases_ecology: The diseases_ecology of this CarrotDisease.  # noqa: E501
        :type: str
        """

        self._diseases_ecology = diseases_ecology

    @property
    def economic_threshold_of_harmfulness(self):
        """Gets the economic_threshold_of_harmfulness of this CarrotDisease.  # noqa: E501


        :return: The economic_threshold_of_harmfulness of this CarrotDisease.  # noqa: E501
        :rtype: str
        """
        return self._economic_threshold_of_harmfulness

    @economic_threshold_of_harmfulness.setter
    def economic_threshold_of_harmfulness(self, economic_threshold_of_harmfulness):
        """Sets the economic_threshold_of_harmfulness of this CarrotDisease.


        :param economic_threshold_of_harmfulness: The economic_threshold_of_harmfulness of this CarrotDisease.  # noqa: E501
        :type: str
        """

        self._economic_threshold_of_harmfulness = economic_threshold_of_harmfulness

    @property
    def id(self):
        """Gets the id of this CarrotDisease.  # noqa: E501


        :return: The id of this CarrotDisease.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CarrotDisease.


        :param id: The id of this CarrotDisease.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def leaves_signs(self):
        """Gets the leaves_signs of this CarrotDisease.  # noqa: E501


        :return: The leaves_signs of this CarrotDisease.  # noqa: E501
        :rtype: str
        """
        return self._leaves_signs

    @leaves_signs.setter
    def leaves_signs(self, leaves_signs):
        """Sets the leaves_signs of this CarrotDisease.


        :param leaves_signs: The leaves_signs of this CarrotDisease.  # noqa: E501
        :type: str
        """

        self._leaves_signs = leaves_signs

    @property
    def name(self):
        """Gets the name of this CarrotDisease.  # noqa: E501


        :return: The name of this CarrotDisease.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CarrotDisease.


        :param name: The name of this CarrotDisease.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def number(self):
        """Gets the number of this CarrotDisease.  # noqa: E501


        :return: The number of this CarrotDisease.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this CarrotDisease.


        :param number: The number of this CarrotDisease.  # noqa: E501
        :type: str
        """

        self._number = number

    @property
    def pathogen(self):
        """Gets the pathogen of this CarrotDisease.  # noqa: E501


        :return: The pathogen of this CarrotDisease.  # noqa: E501
        :rtype: str
        """
        return self._pathogen

    @pathogen.setter
    def pathogen(self, pathogen):
        """Sets the pathogen of this CarrotDisease.


        :param pathogen: The pathogen of this CarrotDisease.  # noqa: E501
        :type: str
        """

        self._pathogen = pathogen

    @property
    def pathogen_distribution_biology(self):
        """Gets the pathogen_distribution_biology of this CarrotDisease.  # noqa: E501


        :return: The pathogen_distribution_biology of this CarrotDisease.  # noqa: E501
        :rtype: str
        """
        return self._pathogen_distribution_biology

    @pathogen_distribution_biology.setter
    def pathogen_distribution_biology(self, pathogen_distribution_biology):
        """Sets the pathogen_distribution_biology of this CarrotDisease.


        :param pathogen_distribution_biology: The pathogen_distribution_biology of this CarrotDisease.  # noqa: E501
        :type: str
        """

        self._pathogen_distribution_biology = pathogen_distribution_biology

    @property
    def pathogen_morphology(self):
        """Gets the pathogen_morphology of this CarrotDisease.  # noqa: E501


        :return: The pathogen_morphology of this CarrotDisease.  # noqa: E501
        :rtype: str
        """
        return self._pathogen_morphology

    @pathogen_morphology.setter
    def pathogen_morphology(self, pathogen_morphology):
        """Sets the pathogen_morphology of this CarrotDisease.


        :param pathogen_morphology: The pathogen_morphology of this CarrotDisease.  # noqa: E501
        :type: str
        """

        self._pathogen_morphology = pathogen_morphology

    @property
    def photo(self):
        """Gets the photo of this CarrotDisease.  # noqa: E501


        :return: The photo of this CarrotDisease.  # noqa: E501
        :rtype: str
        """
        return self._photo

    @photo.setter
    def photo(self, photo):
        """Sets the photo of this CarrotDisease.


        :param photo: The photo of this CarrotDisease.  # noqa: E501
        :type: str
        """

        self._photo = photo

    @property
    def reproductive_organs_signs(self):
        """Gets the reproductive_organs_signs of this CarrotDisease.  # noqa: E501


        :return: The reproductive_organs_signs of this CarrotDisease.  # noqa: E501
        :rtype: str
        """
        return self._reproductive_organs_signs

    @reproductive_organs_signs.setter
    def reproductive_organs_signs(self, reproductive_organs_signs):
        """Sets the reproductive_organs_signs of this CarrotDisease.


        :param reproductive_organs_signs: The reproductive_organs_signs of this CarrotDisease.  # noqa: E501
        :type: str
        """

        self._reproductive_organs_signs = reproductive_organs_signs

    @property
    def root_crop_signs(self):
        """Gets the root_crop_signs of this CarrotDisease.  # noqa: E501


        :return: The root_crop_signs of this CarrotDisease.  # noqa: E501
        :rtype: str
        """
        return self._root_crop_signs

    @root_crop_signs.setter
    def root_crop_signs(self, root_crop_signs):
        """Sets the root_crop_signs of this CarrotDisease.


        :param root_crop_signs: The root_crop_signs of this CarrotDisease.  # noqa: E501
        :type: str
        """

        self._root_crop_signs = root_crop_signs

    @property
    def root_system_signs(self):
        """Gets the root_system_signs of this CarrotDisease.  # noqa: E501


        :return: The root_system_signs of this CarrotDisease.  # noqa: E501
        :rtype: str
        """
        return self._root_system_signs

    @root_system_signs.setter
    def root_system_signs(self, root_system_signs):
        """Sets the root_system_signs of this CarrotDisease.


        :param root_system_signs: The root_system_signs of this CarrotDisease.  # noqa: E501
        :type: str
        """

        self._root_system_signs = root_system_signs

    @property
    def seedlings_sings(self):
        """Gets the seedlings_sings of this CarrotDisease.  # noqa: E501


        :return: The seedlings_sings of this CarrotDisease.  # noqa: E501
        :rtype: str
        """
        return self._seedlings_sings

    @seedlings_sings.setter
    def seedlings_sings(self, seedlings_sings):
        """Sets the seedlings_sings of this CarrotDisease.


        :param seedlings_sings: The seedlings_sings of this CarrotDisease.  # noqa: E501
        :type: str
        """

        self._seedlings_sings = seedlings_sings

    @property
    def sickness(self):
        """Gets the sickness of this CarrotDisease.  # noqa: E501


        :return: The sickness of this CarrotDisease.  # noqa: E501
        :rtype: str
        """
        return self._sickness

    @sickness.setter
    def sickness(self, sickness):
        """Sets the sickness of this CarrotDisease.


        :param sickness: The sickness of this CarrotDisease.  # noqa: E501
        :type: str
        """

        self._sickness = sickness

    @property
    def stalks_signs(self):
        """Gets the stalks_signs of this CarrotDisease.  # noqa: E501


        :return: The stalks_signs of this CarrotDisease.  # noqa: E501
        :rtype: str
        """
        return self._stalks_signs

    @stalks_signs.setter
    def stalks_signs(self, stalks_signs):
        """Sets the stalks_signs of this CarrotDisease.


        :param stalks_signs: The stalks_signs of this CarrotDisease.  # noqa: E501
        :type: str
        """

        self._stalks_signs = stalks_signs

    @property
    def sub_type(self):
        """Gets the sub_type of this CarrotDisease.  # noqa: E501


        :return: The sub_type of this CarrotDisease.  # noqa: E501
        :rtype: str
        """
        return self._sub_type

    @sub_type.setter
    def sub_type(self, sub_type):
        """Sets the sub_type of this CarrotDisease.


        :param sub_type: The sub_type of this CarrotDisease.  # noqa: E501
        :type: str
        """

        self._sub_type = sub_type

    @property
    def type(self):
        """Gets the type of this CarrotDisease.  # noqa: E501


        :return: The type of this CarrotDisease.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CarrotDisease.


        :param type: The type of this CarrotDisease.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(CarrotDisease, dict):
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
        if not isinstance(other, CarrotDisease):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CarrotDisease):
            return True

        return self.to_dict() != other.to_dict()
