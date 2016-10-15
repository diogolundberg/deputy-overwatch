from urllib2 import urlopen
import xmltodict


def get_xml_parsed_data(url):
    response = urlopen(url)
    data = response.read()
    return xmltodict.parse(data)
