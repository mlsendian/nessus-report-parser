from collections import UserDict

from lxml import etree

from .report_host import ReportHost


class Report(UserDict):
    def __init__(self, properties):
        assert isinstance(properties, dict)
        self.data = properties

    @staticmethod
    def from_etree(elem):
        assert isinstance(elem, etree._Element)
        assert elem.tag == 'Report'

        properties = {
            'name': elem.attrib.get('name'),
            'hosts': [ReportHost.from_etree(el) for el in elem.findall('ReportHost')]
        }

        return Report(properties)
