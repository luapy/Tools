# coding:utf-8
import requests 
import sys
import re
#date;2018.4.10

def Start():
    if(len(sys.argv)!=2):
        print "****************"
        print " ************* "
        print "Useage:python Webscan.py 111.111.111.111"
        print " ************* "
        print "****************"
        sys.exit()
def Scan():
    y=0

    url="http://www.webscan.cc/"
    iparg=sys.argv[1]
    payload={'action':'query','ip':iparg,'type':'xml'}
    res=requests.get(url,params=payload)
    domain=re.findall(".*domain>(.*)</domain.*",res.text)
    title=re.findall(".*title>(.*)</title.*",res.text)
    for x in domain:
            print ">>  domain:"+x+"  <<"
            if(title[y]!=""):
                print ">>  title:"+title[y]+"  <<" 
                y+=1
            else:
                print ">>  title:None  <<"
                y+=1
            print 
if __name__ == '__main__':
    print "                  Site search"    
    Start()
    Scan()