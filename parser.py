# -*- coding: utf-8 -*-
from sys import argv
import urllib3
import re

_digits = re.compile('\d')
def contains_digits(d):
    return bool(_digits.search(d))

f = open(argv[1])

verse_count = 0

def lookup_hebrew_word(word):
    word = word.replace('\u202b', "")
    word = word.replace('\u202c', "")
    print("'" + word + "'")
    lookup_hebrew_definition(word)
    


def lookup_hebrew_definition(word):
    http = urllib3.PoolManager()
    urlPrefix = u"http://scholarsgateway.com/parse/" 
    urlPrefix = urlPrefix.encode('utf-8')
    url = urlPrefix + word
    print (url)
    request = http.request('GET', url)
    #print( request.status)
    #print( "HTML DATA\n" + request.data )
    
    for line in request.data.splitlines():
        if "Word Parsed:" in line:
            cleanedLine = re.sub('<[^>]*>', ' ', line)
            print (cleanedLine)
    
    
    return request.data    #return the html of the world


for verse in f:
    if (verse.find("xxxx") > -1):
        continue
    verse_count += 1
    
    nverse = -1
    nchapter = -1
    
    words = verse.split()
    
    if (verse_count == 5):
        print(words)
    
    for word in words:
        
        if (contains_digits(word) == False):
            if (verse_count == 5 and word != '\u202b' and len(word) > 1):
                lookup_hebrew_word(word.replace("׃", ""))
            continue
        
        colon_index = word.find(":")
    
        if (verse_count == 5):
            
            print("~" + str(word) + "~" + str(colon_index))
    
        if (colon_index == -1):
            nverse = word
        else:
            nchapter = word[colon_index:]
    
    
    if (verse_count == 5):
        print(str(nchapter) + " & " + str(nverse))
#    print(verse)


