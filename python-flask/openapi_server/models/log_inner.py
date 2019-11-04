# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class LogInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, level=None, timestamp=None, msg=None):  # noqa: E501
        """LogInner - a model defined in OpenAPI

        :param level: The level of this LogInner.  # noqa: E501
        :type level: int
        :param timestamp: The timestamp of this LogInner.  # noqa: E501
        :type timestamp: datetime
        :param msg: The msg of this LogInner.  # noqa: E501
        :type msg: str
        """
        self.openapi_types = {
            'level': int,
            'timestamp': datetime,
            'msg': str
        }

        self.attribute_map = {
            'level': 'level',
            'timestamp': 'timestamp',
            'msg': 'msg'
        }

        self._level = level
        self._timestamp = timestamp
        self._msg = msg

    @classmethod
    def from_dict(cls, dikt) -> 'LogInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Log_inner of this LogInner.  # noqa: E501
        :rtype: LogInner
        """
        return util.deserialize_model(dikt, cls)

    @property
    def level(self):
        """Gets the level of this LogInner.

        Logging level for entry. DEBUG=10, INFO=20, WARNING=30, ERROR=40, FATAL=50   # noqa: E501

        :return: The level of this LogInner.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this LogInner.

        Logging level for entry. DEBUG=10, INFO=20, WARNING=30, ERROR=40, FATAL=50   # noqa: E501

        :param level: The level of this LogInner.
        :type level: int
        """
        if level is None:
            raise ValueError("Invalid value for `level`, must not be `None`")  # noqa: E501

        self._level = level

    @property
    def timestamp(self):
        """Gets the timestamp of this LogInner.

        Timestamp for log entry  # noqa: E501

        :return: The timestamp of this LogInner.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this LogInner.

        Timestamp for log entry  # noqa: E501

        :param timestamp: The timestamp of this LogInner.
        :type timestamp: datetime
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def msg(self):
        """Gets the msg of this LogInner.

        The logged message.  # noqa: E501

        :return: The msg of this LogInner.
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg):
        """Sets the msg of this LogInner.

        The logged message.  # noqa: E501

        :param msg: The msg of this LogInner.
        :type msg: str
        """
        if msg is None:
            raise ValueError("Invalid value for `msg`, must not be `None`")  # noqa: E501

        self._msg = msg