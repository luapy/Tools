# coding:utf-8
import requests
import sys
#from bs4 import BeautifulSoup


def checkcode(dir):
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; \
    rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
        "Connection":
        "close"
    }
    Visablelist = []
    #Forbiddenlist = []
    #NotFoundlist = []
    #Elsedic = []
    lines = []
    f = open(dir, "r")
    for line in f.readlines():
        line = line.strip()
        line = 'http://' + line
        lines.append(line)
    for line in lines:      
        #print line
        try:
            re = requests.get(line, headers=headers)
            if re.status_code == 200:
                print "Aviliable: " + line
                Visablelist.append(line)
            #else:
             #   print "UnAviliable: " + line
            #Visablelist = (list.set(Visablelist))
        except requests.RequestException as e:
            pass
        continue
            #Visablelist = (list.set(Visablelist))
    #for url in Visablelist:
     #   print url + "    200"
        #print re.url
        #print re.content
        #soup = BeautifulSoup(re.content)
        #a = soup.find_all('title')[0].get_text()
        # print a
        #time.sleep(2)


if (len(sys.argv) != 2):
    print "Usage:python Domain_filter.py listfiledir"
    sys.exit
else:
    dirfile = sys.argv[1]
    checkcode(dirfile)
    print "Down!"