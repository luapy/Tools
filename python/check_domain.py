# coding:utf-8
# 2018.11.7
import requests
import sys

headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; \
rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6', "Connection": "close"}


def readtxt(dirfile):
    with open(dirfile) as f:
        namelist = []
        for name in f.readlines():
            namelist.append(name.strip())
        return namelist


def check(namelist):
    or_url = "https://www.goldenpages"
    lists = []
    for add in namelist:
        fn_url = or_url + add
        lists.append(fn_url.strip())
    return lists


def send(url):
    try:
        re = requests.get(url, headers=headers)
        #print re.text
        if (re.status_code == 200):
            print " Aviliable: "+url
    except requests.RequestException as e:
            print " UnAviliable: " + url


if (len(sys.argv) != 2):
    print "Usage:python check.py listfiledir"
    sys.exit
else:
    dirfile = sys.argv[1]
    namelist = readtxt(dirfile)
    lists = check(namelist)
    for url in lists:
        send(url)
    print "\n\nCheck out!"
