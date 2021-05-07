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


class RequestDto(object):
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
        'annotation': 'str',
        'create_date': 'datetime',
        'files': 'list[TaskFileDto]',
        'id': 'int',
        'status': 'str',
        'tasks': 'list[TaskDto]',
        'title': 'str',
        'update_date': 'datetime',
        'user_id': 'int'
    }

    attribute_map = {
        'annotation': 'annotation',
        'create_date': 'createDate',
        'files': 'files',
        'id': 'id',
        'status': 'status',
        'tasks': 'tasks',
        'title': 'title',
        'update_date': 'updateDate',
        'user_id': 'userId'
    }

    def __init__(self, annotation=None, create_date=None, files=None, id=None, status=None, tasks=None, title=None, update_date=None, user_id=None, _configuration=None):  # noqa: E501
        """RequestDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._annotation = None
        self._create_date = None
        self._files = None
        self._id = None
        self._status = None
        self._tasks = None
        self._title = None
        self._update_date = None
        self._user_id = None
        self.discriminator = None

        if annotation is not None:
            self.annotation = annotation
        if create_date is not None:
            self.create_date = create_date
        if files is not None:
            self.files = files
        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if tasks is not None:
            self.tasks = tasks
        if title is not None:
            self.title = title
        if update_date is not None:
            self.update_date = update_date
        if user_id is not None:
            self.user_id = user_id

    @property
    def annotation(self):
        """Gets the annotation of this RequestDto.  # noqa: E501


        :return: The annotation of this RequestDto.  # noqa: E501
        :rtype: str
        """
        return self._annotation

    @annotation.setter
    def annotation(self, annotation):
        """Sets the annotation of this RequestDto.


        :param annotation: The annotation of this RequestDto.  # noqa: E501
        :type: str
        """

        self._annotation = annotation

    @property
    def create_date(self):
        """Gets the create_date of this RequestDto.  # noqa: E501


        :return: The create_date of this RequestDto.  # noqa: E501
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this RequestDto.


        :param create_date: The create_date of this RequestDto.  # noqa: E501
        :type: datetime
        """

        self._create_date = create_date

    @property
    def files(self):
        """Gets the files of this RequestDto.  # noqa: E501


        :return: The files of this RequestDto.  # noqa: E501
        :rtype: list[TaskFileDto]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this RequestDto.


        :param files: The files of this RequestDto.  # noqa: E501
        :type: list[TaskFileDto]
        """

        self._files = files

    @property
    def id(self):
        """Gets the id of this RequestDto.  # noqa: E501


        :return: The id of this RequestDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RequestDto.


        :param id: The id of this RequestDto.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def status(self):
        """Gets the status of this RequestDto.  # noqa: E501


        :return: The status of this RequestDto.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this RequestDto.


        :param status: The status of this RequestDto.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def tasks(self):
        """Gets the tasks of this RequestDto.  # noqa: E501


        :return: The tasks of this RequestDto.  # noqa: E501
        :rtype: list[TaskDto]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """Sets the tasks of this RequestDto.


        :param tasks: The tasks of this RequestDto.  # noqa: E501
        :type: list[TaskDto]
        """

        self._tasks = tasks

    @property
    def title(self):
        """Gets the title of this RequestDto.  # noqa: E501


        :return: The title of this RequestDto.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this RequestDto.


        :param title: The title of this RequestDto.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def update_date(self):
        """Gets the update_date of this RequestDto.  # noqa: E501


        :return: The update_date of this RequestDto.  # noqa: E501
        :rtype: datetime
        """
        return self._update_date

    @update_date.setter
    def update_date(self, update_date):
        """Sets the update_date of this RequestDto.


        :param update_date: The update_date of this RequestDto.  # noqa: E501
        :type: datetime
        """

        self._update_date = update_date

    @property
    def user_id(self):
        """Gets the user_id of this RequestDto.  # noqa: E501


        :return: The user_id of this RequestDto.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this RequestDto.


        :param user_id: The user_id of this RequestDto.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

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
        if issubclass(RequestDto, dict):
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
        if not isinstance(other, RequestDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RequestDto):
            return True

        return self.to_dict() != other.to_dict()
