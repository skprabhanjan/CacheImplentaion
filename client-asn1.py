import requests
import json
import os
import random
import sys, getopt
import hashlib
serverName = ''
outputName = ''
try:
        opts, args = getopt.getopt(sys.argv[1:], "w:O:")
except getopt.GetoptError, err:
        print "Usage: ", sys.argv[0], " -w <url> -O <Output-File"
        sys.exit(2)
 
for opt, arg in opts:
        if opt=='-w':
            serverName=arg
        elif opt=='-O':
            outputName=arg
 
if outputName is None or serverName is None:
        print "Usage: ", sys.argv[0], "-w <url> -O <Output-File"
        sys.exit(2)
rand = random.getrandbits(32)
try:
    os.mkdir("cache")
except:
        dump = 1
os.chdir("cache")
path = os.getcwd()
open(path + '/' + 'map.txt', 'a').close()
fileCached = ''
found  = 0
fileName = path + '/' + "map.txt"
isImage = serverName[len(serverName)-3:len(serverName)]
with open(fileName) as f:
    for line in f:
        arr = line.split(",")
        if(arr[1] == (hashlib.sha1(serverName).hexdigest() + "\n")):
                found = 1
                fileCached = arr[0]
if found ==1:
        filePath = path + '/' + fileCached + '.txt'
        fo = open(filePath,"rw+")
        s = fo.read()
        str2 = "Last-Modified"
        value = s.find(str2)
        start = s[value+17]
        for i in range(1,29):
            start+=s[value+17+i]
        response = requests.get(serverName,headers={"If-Modified-Since":start})
        if(response.status_code == 304):
                cachedValue = s.split('$#prabpraj#$')
                outputFile = path + '/' + outputName 
                outFile = open(outputFile,"w")
                outFile.close()
                out = open(outputFile,"rw+")
                string = str(cachedValue[1])
                out.write(string)
                out.close()
        print response
        fo.close()
else:
        try:
                with open(fileName,"a") as myfile:
                        string = str(rand) + "," + str(hashlib.sha1(serverName).hexdigest())  +  '\n'
                        myfile.write(string)
                response = requests.get(serverName)
                outputFile = path + '/' + outputName
                outFile = open(outputFile,"w")
                outFile.close()
                out = open(outputFile,"rw+")
                data = ''
                if response.headers['Content-Type'][0:4] == "text":
                         data = response.text
                else:
                        data = response.url
                out.write(data)
                out.close()
                cacheFile = path + '/' + str(rand) +".txt" 
                f = open(cacheFile,'w')
                f.close()
                fo = open(cacheFile,"rw+")
                string = str(response.headers) + '\n' + "$#prabpraj#$" + '\n' + data
                fo.write(string)
                print response
        except:
                print "Error Occured"
                sys.exit(0)
