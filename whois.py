import json
import urllib.request
import argparse
from bs4 import BeautifulSoup
import requests

class Parser(object):
    def __init__(self):
        self.parse = argparse.ArgumentParser()
        self.parse.add_argument('ip', help='The IP address you want to trace.')
        self.args = self.parse.parse_args()
    def ip(self):
        return self.args.ip

class IPTracer1(object):
    def __init__(self, ipaddress):
        self.endpoint1 = 'http://ip-api.com/json/'
        self.endpoint2 = 'https://whatismyipaddress.com/ip/'
        self.ipaddress = ipaddress
    def trace(self):
        #first source: ip-api.com
        data = urllib.request.urlopen(self.endpoint1 + self.ipaddress)
        data = json.load(data)
        newkeys = [
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
        keys = [
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

        #second source: whatismyipaddress.com

        header = {'user-Agent':'curl/7.21.3'}
        req = requests.get(self.endpoint2 + self.ipaddress, header).content
        soup = BeautifulSoup(req, 'html.parser')

        print('='*40)
        print('Tracing: ' + ip, end='\n\n')
        print('-'*40)
        print('Source #1: ip-api.com', end='\n\n')
        for index, key in enumerate(keys):
            print(newkeys[index] + ': ' + str(data[key]))
        print('-'*40)
        print('Source #2: whatismyipaddress.com', end='\n\n')
        for head, data in zip(soup.findAll('th'), soup.findAll('td')):
            print(head.text.strip() + " " + data.text.strip())
        print('='*40)

parser = Parser()
ip = parser.ip()
data = IPTracer1(ip).trace()
