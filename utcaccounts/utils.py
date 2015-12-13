import urllib2
from settings import UTC_CAS_URL

class CASException(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return message


class CASTicket:

    def __init__(self, uri, ticket):
        self.uri = uri
        self.ticket = str(ticket)
        if self.ticket is None or self.ticket == '':
            raise CASException('Empty ticket')

    def get_server_information(self):
        response = urllib2.urlopen(UTC_CAS_URL + 'serviceValidate?service=' + self.uri + '&ticket=' + self.ticket)
        return response.read()

    def parse_information(self, xml_info):


    def get_information(self):
        xml_info = self.get_server_information()
        return self.parse_information(xml_info)