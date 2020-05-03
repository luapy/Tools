#
import os
import sys
import time

if len(sys.argv) != 3:
    print('Usage:python dicts.py dic1.txt dic2.txt')
    exit()
else:
    new_dict = open(sys.argv[1], 'r')
    new_words = new_dict.readlines()
    new_dict.close()
    dicts = open(sys.argv[2], 'r')
    words = dicts.readlines()
    dicts.close()
    lists = new_words + words
    lists = set(lists)
    filename = str(time.time())+'.txt'
    finally_words = open(filename, "w+")
    for word in lists:
        finally_words.writelines(word.strip('\n') + '\n')
    finally_words.close()
    print(sys.argv[1]+":"+str(len(new_words)))
    print(sys.argv[2]+":"+str(len(words)))
    print("check " + filename + ": "+str(len(lists)))

