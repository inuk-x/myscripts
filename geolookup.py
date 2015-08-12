#!/usr/bin/env python

"""

a super simple script that takes an IP address as input and returns 
GeoIP data such as city, country, region and autonominous system info

"""

# import libraries
import pygeoip
import sys

# usage error message
usage = (
"\nUsage: geolookup.py ip_address\n"
)

if len(sys.argv) < 2:
    print usage
    sys.exit(0)

# IP address input 
address = sys.argv[1]

# location of GeoIP database
gi = pygeoip.GeoIP('/opt/GeoIP/Geo.dat')
gi2 = pygeoip.GeoIP('/opt/GeoIP/GeoIPASNum.dat')

# parse IP address by city, country and region 
def printRecord(address):
    rec = gi.record_by_name(address)
    asn = gi2.asn_by_addr(address)
    city = rec['city']
    country = rec['country_name']
    region = rec['region_code']
    print '[*] IP Address: ' + address + ' is located in '+str(city)+', '+str(region)+', '+str(country)+', '+ asn

# print results of IP Geo lookup
printRecord(address)
