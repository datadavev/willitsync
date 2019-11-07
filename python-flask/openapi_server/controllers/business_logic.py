# standard library imports
import asyncio
import datetime as dt

# 3rd party library imports
import requests
from schema_org.so_core import SchemaDotOrgHarvester


def parse_sitemap(url):
    """
    Business logic for using schema_org to process sitemaps.

    Returns
    -------
    sitemaps
        list of all sitemap URLs on the web site
    date
        datetime of this request
    logs
        list of log entries for this operation
    urlset
        list of tuples consisting of a landing page URL and the last modified
        time of the landing page
    """
    date = dt.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

    kwargs = {
        'log_to_string': True,
        'log_to_stdout': False,
        'no_harvest': True,
        'ignore_harvest_time': True,
    }
    obj = SchemaDotOrgHarvester(**kwargs)
    obj.sitemap = url
    asyncio.run(obj.run())

    sitemaps = obj.get_sitemaps()
    urlset = obj.get_sitemaps_urlset()

    logs = obj.extract_log_messages()

    return sitemaps, date, logs, urlset

def parse_robots(url):
    """Parses robots.txt to find sitemap(s)

    Given a robots.txt file, parse, and retrieve referenced sitemap documents.

    :param url: URL pointing to a robots.txt file
    :type url: str
    """
    date = dt.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

    r = requests.get(url)
    r.raise_for_status()

    sitemaps = []
    for line in r.text.splitlines():
        if 'Sitemap:' in line:
            sitemaps.append(line.split(': ')[0])

    return date, sitemaps


def parse_landing_page(url):

    date = dt.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    jsonld, logs = extract_jsonld(url)
    return date, jsonld, logs


def extract_jsonld(url):
    """
    Given a URL of a landing page, extract an existing JSON-LD element if it
    exists.

    Returns
    -------
    jsonld : object
        deserialized JSON object
    logs
    """
    obj = SchemaDotOrgHarvester(log_to_string=True, log_to_stdout=False)
    doc = asyncio.run(obj.retrieve_landing_page_content(url))
    jsonld = obj.get_jsonld(doc)

    logs = obj.extract_log_messages()

    return jsonld, logs