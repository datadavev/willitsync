# openapi-client
Provides various methods for retrieving, parsing, and validating the  various portions of a web harvesting workflow. 

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.1.1
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint


# Defining host is optional and default to https://localhost:8080/willitsync/1.1.1
configuration.host = "https://localhost:8080/willitsync/1.1.1"
# Create an instance of the API class
api_instance = openapi_client.DevelopersApi(openapi_client.ApiClient(configuration))
url = 'https://my.server/metadata/iso_metadata.xml' # str | URL referencing a science metadata XML document to retrieve  and validate. 
formatid = 'http://www.isotc211.org/2005/gmd' # str | The DataONE formatId of the XML to test for validity. 

try:
    # Retrieve and validate a science metadata XML document
    api_response = api_instance.get_validate_metadata(url, formatid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->get_validate_metadata: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://localhost:8080/willitsync/1.1.1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DevelopersApi* | [**get_validate_metadata**](docs/DevelopersApi.md#get_validate_metadata) | **GET** /scivalid | Retrieve and validate a science metadata XML document
*DevelopersApi* | [**get_validate_so**](docs/DevelopersApi.md#get_validate_so) | **GET** /sovalid | Retrieve and validate a schema.org JSON-LD document
*DevelopersApi* | [**parse_landingpage**](docs/DevelopersApi.md#parse_landingpage) | **GET** /so | Extract schema.org metadata from web page
*DevelopersApi* | [**parse_robots**](docs/DevelopersApi.md#parse_robots) | **GET** /robots | Retrieve sitemap references from a robots.txt file
*DevelopersApi* | [**parse_sitemap**](docs/DevelopersApi.md#parse_sitemap) | **GET** /sitemap | Get locatiosn from a sitemap.
*DevelopersApi* | [**validate_metadata**](docs/DevelopersApi.md#validate_metadata) | **POST** /scivalid | Validate provided science metadata XML document
*DevelopersApi* | [**validate_so**](docs/DevelopersApi.md#validate_so) | **POST** /sovalid | Validate provided schema.org JSON-LD document
*UsersApi* | [**get_validate_metadata**](docs/UsersApi.md#get_validate_metadata) | **GET** /scivalid | Retrieve and validate a science metadata XML document
*UsersApi* | [**get_validate_so**](docs/UsersApi.md#get_validate_so) | **GET** /sovalid | Retrieve and validate a schema.org JSON-LD document
*UsersApi* | [**parse_landingpage**](docs/UsersApi.md#parse_landingpage) | **GET** /so | Extract schema.org metadata from web page
*UsersApi* | [**parse_robots**](docs/UsersApi.md#parse_robots) | **GET** /robots | Retrieve sitemap references from a robots.txt file
*UsersApi* | [**parse_sitemap**](docs/UsersApi.md#parse_sitemap) | **GET** /sitemap | Get locatiosn from a sitemap.
*UsersApi* | [**validate_metadata**](docs/UsersApi.md#validate_metadata) | **POST** /scivalid | Validate provided science metadata XML document
*UsersApi* | [**validate_so**](docs/UsersApi.md#validate_so) | **POST** /sovalid | Validate provided schema.org JSON-LD document


## Documentation For Models

 - [LogEntry](docs/LogEntry.md)
 - [RobotsFile](docs/RobotsFile.md)
 - [SCIMetadata](docs/SCIMetadata.md)
 - [SOMetadata](docs/SOMetadata.md)
 - [Sitemap](docs/Sitemap.md)
 - [SitemapUrlset](docs/SitemapUrlset.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author

jevans97@utk.edu

