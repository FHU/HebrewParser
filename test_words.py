# -*- coding: utf-8 -*-
from sys import argv
import urllib3
import re

_digits = re.compile('\d')
def contains_digits(d):
    return bool(_digits.search(d))

def strip_rtl_characters(word):
    word = word.replace('\u202b', "")
    word = word.replace('\u202c', "")
    return word

f = open(argv[1])

verse_count = 0

words_lookup = {}
words_count = {}


def lookup_hebrew_word(word):
    word = strip_rtl_characters(word)
    print("'" + word + "'")
    if (not word in words_lookup):
        words_count[word] = 1
        wd = lookup_hebrew_definition(word)
        if ("Word Parsed" in wd):
            words_lookup[word] = True
        else:
            words_lookup[word] = False
        print "word requested"
    else:
        words_count[word] += 1
        print "word found in cache"


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
            partOfSpeech = extractPartOfSpeech(line)
            if (partOfSpeech == "adjective"):
                parseAdjective(word, cleanedLine)
            elif (partOfSpeech == "adverb"):
                parseAdverb(word, cleanedLine)
                #finish this! 



    return request.data    #return the html of the world


def extractPartOfSpeech(line):
    #fix this!
    pos = "adjective"

    return pos

def parseAdjective(word, html): 
    #fix this!
    wordFeatures = {}


    return wordFeatures


# Lee - Verbs
# Brendan - Pronouns
# Cory - Conjunctions and Demonstratives 
# Kaleb - Nouns 
# Joey - Adjectives 
# Andy - Prepositions 
# Jordan - Adverbs
# Camille - Interrogatives, Determiners 
# Austin - Particles, Interjections

for verse in f:
    if (verse.find("xxxx") > -1):
        continue
    verse_count += 1
    
    nverse = -1
    nchapter = -1
    
    words = verse.split()
    
    if (verse_count >  40):
        break
    
    for word in words:
        
        if (contains_digits(word) == False):
            if (word != '\u202b' and len(word) > 1):
                lookup_hebrew_word(word.replace("׃", ""))
            
                print("Word not containing numbers: " + word)
            continue
        word = strip_rtl_characters(word)
        
#print("word containing numbers: " + word + "~")
        
        colon_index = word.find(":")
    
#print("~" + str(word) + "~" + str(colon_index))
    
        if (colon_index == -1):
            nverse = word
        else:
            nchapter = word[colon_index:]
    
    
#print(str(nchapter) + " & " + str(nverse))
#    print(verse)


success = 0
success_weighted = 0
word_count = 0
for word in words_lookup:
    worked = words_lookup[word]
    instances = words_count[word]
    print word + ": " + str(instances) + " / " + str(worked)
    if (worked == True):
        success += 1
        success_weighted += words_count[word]
    word_count += instances

print str(success) + " / " + str(len(words_lookup))
print str(success_weighted) + " / " + str(word_count)

