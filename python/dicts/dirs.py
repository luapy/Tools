import os
import sys

filedict=set()
dirdict=set()
blacklist=['.jpg','.JPG','.PNG','.png','.HTML','.html','.svg','.jpeg','.ttf','.css','.pdf','.woff','.otf','.eot','.woff2']
def Get(source):
    for root,dirs,files in os.walk(source):
        for dirname in dirs:
            dirdict.add(dirname)
        for filename in files:
            files=os.path.splitext(filename)
            name,type=files
            if type not in blacklist:
                filedict.add(filename)

def main():
    source=sys.argv[1]
    print(source)
    Get(source)
    dirnamedict=open('dirnamedic.txt','w+')
    filenamedict=open('filenamedic.txt','w+')
    for dic in dirdict:
        dirnamedict.writelines(dic+'\n')
    dirnamedict.close()
    for filename in filedict:
        filenamedict.writelines(filename+'\n')
    filenamedict.close()

if __name__ == "__main__":
    main()

