# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.log_entry import LogEntry
from openapi_server import util

from openapi_server.models.log_entry import LogEntry  # noqa: E501

class SCIMetadata(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, url=None, evaluated_date=None, log=None, metadata=None):  # noqa: E501
        """SCIMetadata - a model defined in OpenAPI

        :param url: The url of this SCIMetadata.  # noqa: E501
        :type url: str
        :param evaluated_date: The evaluated_date of this SCIMetadata.  # noqa: E501
        :type evaluated_date: datetime
        :param log: The log of this SCIMetadata.  # noqa: E501
        :type log: List[LogEntry]
        :param metadata: The metadata of this SCIMetadata.  # noqa: E501
        :type metadata: str
        """
        self.openapi_types = {
            'url': str,
            'evaluated_date': datetime,
            'log': List[LogEntry],
            'metadata': str
        }

        self.attribute_map = {
            'url': 'url',
            'evaluated_date': 'evaluated_date',
            'log': 'log',
            'metadata': 'metadata'
        }

        self._url = url
        self._evaluated_date = evaluated_date
        self._log = log
        self._metadata = metadata

    @classmethod
    def from_dict(cls, dikt) -> 'SCIMetadata':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SCIMetadata of this SCIMetadata.  # noqa: E501
        :rtype: SCIMetadata
        """
        return util.deserialize_model(dikt, cls)

    @property
    def url(self):
        """Gets the url of this SCIMetadata.

        URL of the XML document that was retrieved and processed. If a  redirection occurs, then this is the final URL that was used to retrieve the document.   # noqa: E501

        :return: The url of this SCIMetadata.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this SCIMetadata.

        URL of the XML document that was retrieved and processed. If a  redirection occurs, then this is the final URL that was used to retrieve the document.   # noqa: E501

        :param url: The url of this SCIMetadata.
        :type url: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def evaluated_date(self):
        """Gets the evaluated_date of this SCIMetadata.

        The timestamp for when the evaluation the landing page was initiated.   # noqa: E501

        :return: The evaluated_date of this SCIMetadata.
        :rtype: datetime
        """
        return self._evaluated_date

    @evaluated_date.setter
    def evaluated_date(self, evaluated_date):
        """Sets the evaluated_date of this SCIMetadata.

        The timestamp for when the evaluation the landing page was initiated.   # noqa: E501

        :param evaluated_date: The evaluated_date of this SCIMetadata.
        :type evaluated_date: datetime
        """
        if evaluated_date is None:
            raise ValueError("Invalid value for `evaluated_date`, must not be `None`")  # noqa: E501

        self._evaluated_date = evaluated_date

    @property
    def log(self):
        """Gets the log of this SCIMetadata.


        :return: The log of this SCIMetadata.
        :rtype: List[LogEntry]
        """
        return self._log

    @log.setter
    def log(self, log):
        """Sets the log of this SCIMetadata.


        :param log: The log of this SCIMetadata.
        :type log: List[LogEntry]
        """
        if log is None:
            raise ValueError("Invalid value for `log`, must not be `None`")  # noqa: E501

        self._log = log

    @property
    def metadata(self):
        """Gets the metadata of this SCIMetadata.

        The XML metadata document that was validated.   # noqa: E501

        :return: The metadata of this SCIMetadata.
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this SCIMetadata.

        The XML metadata document that was validated.   # noqa: E501

        :param metadata: The metadata of this SCIMetadata.
        :type metadata: str
        """
        if metadata is None:
            raise ValueError("Invalid value for `metadata`, must not be `None`")  # noqa: E501

        self._metadata = metadata
