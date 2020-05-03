import os
import sys

filedict = set()
dirdict = set()
blacklist = ['.jpg', '.JPG', '.PNG', '.png', '.HTML', '.html', '.svg', '.jpeg', '.ttf', '.css', '.pdf', '.woff', '.otf',
             '.eot', '.woff2']


def Get(source):
    for root, dirs, files in os.walk(source):
        for dirname in dirs:
            dirdict.add(dirname)
        for filename in files:
            files = os.path.splitext(filename)
            name, type = files
            if type not in blacklist:
                filedict.add(filename)


def remove():
    dirnamedict = open('dirnamedic.txt', 'a+')
    lines_temp = dirnamedict.readlines()
    with open('dirnamedic_temp.txt', 'r') as temp:
        for line in temp.readlines():
            if line.strip('\n') in lines_temp:
                continue
            else:
                dirnamedict.writelines(line)
    temp.close()
    dirnamedict.close()

    filenamedict = open('filenamedict.txt', 'a+')
    lines_temp = filenamedict.readlines()
    with open('filenamedic_temp.txt', 'r') as temp:
        for line in temp.readlines():
            if line.strip('\n') in lines_temp:
                continue
            else:
                filenamedict.writelines(line)
    temp.close()
    filenamedict.close()


def main():
    if len(sys.argv()) != 2:
        print("Usage: python dirs.py dir_path")
        exit()
    else:
        source = sys.argv[1]
        print(source)
        test = open('dirnamedic.txt', 'a+')
        test.seek(1)
        lines_temp = test.readlines()
        test.seek(length(line_temp) - 1)
        Get(source)
        dirnamedict = open('dirnamedic_temp.txt', 'w+')
        filenamedict = open('filenamedic_temp.txt', 'w+')
        for dic in dirdict:
            dirnamedict.writelines(dic + '\n')
        dirnamedict.close()
        for filename in filedict:
            filenamedict.writelines(filename + '\n')
        filenamedict.close()
        remove()


if __name__ == "__main__":
    main()
