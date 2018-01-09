import json
import urllib.request
import argparse

class Parser(object):
    def __init__(self):
        self.parse = argparse.ArgumentParser()
        self.parse.add_argument('ip', help='The IP address you want to trace.')
        self.args = self.parse.parse_args()
    def ip(self):
        return self.args.ip

class IPTracer(object):
    def __init__(self, ipaddress):
        self.endpoint = 'http://ip-api.com/json/'
        self.ipaddress = ipaddress
    def trace(self):
        data = urllib.request.urlopen(self.endpoint + self.ipaddress)
        data = json.load(data)
        return data

class PrettyPrint(object):
    def __init__(self, data):
        self.data = data
        self.newkeys = [
            'IP',
            'City',
            'State/Region',
            'Country',
            'ISP',
            'Timezone',
            'AS',
            'ZipCode',
            'Organization',
            'Latitude',
            'Longitude',
        ]
        self.keys = [
            'query',
            'city',
            'regionName',
            'country',
            'isp',
            'timezone',
            'as',
            'zip',
            'org',
            'lat',
            'lon'
        ]

        print('='*40)
        print('Tracing: ' + ip)
        print('-'*40)
        for index, key in enumerate(self.keys):
            print(self.newkeys[index] + ': ' + str(self.data[key]))
        print('='*40)

parser = Parser()
ip = parser.ip()
data = IPTracer(ip).trace()
PrettyPrint(data)
