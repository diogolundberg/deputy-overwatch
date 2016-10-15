import urllib3
import xmltodict


def get_xml_parsed_data(url):
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    return xmltodict.parse(r.data)
