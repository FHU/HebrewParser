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

def lookup_hebrew_word(word):
    word = word.replace('\u202b', "")
    word = word.replace('\u202c', "")
    #print("'" + word + "'")
    lookup_hebrew_definition(word)
    word = strip_rtl_characters(word)
    print("'" + word + "'")
#lookup_hebrew_definition(word)
    


def lookup_hebrew_definition(word):
    http = urllib3.PoolManager()
    urlPrefix = "http://scholarsgateway.com/parse/" 
    urlPrefix = urlPrefix.encode('utf-8')
    url = urlPrefix + word
    #print (url)
    request = http.request('GET', url)
    #print( request.status)
    #print( "HTML DATA\n" + request.data )
    
    found = False

    for line in request.data.splitlines():
        if "Word Parsed:" in line:
            found = True
            cleanedLine = re.sub('<[^>]*>', '\t', line)
            #print (cleanedLine)
            partOfSpeech = extractPartOfSpeech(cleanedLine)
            

            print partOfSpeech
            # if (partOfSpeech == "adjective"):
            #     parseAdjective(word, cleanedLine)
            # elif (partOfSpeech == "adverb"):
            #     parseAdverb(word, cleanedLine)
            # elif (partOfSpeech == "conjunction"):
            #     parseConjunction(word, cleanedLine)
            # elif (partOfSpeech == "demonstrative"):
            #     parseDemonstrative(word, cleanedLine)
            # elif (partOfSpeech == "determiner"):
            #     parseDeterminer(word, cleanedLine)
            # elif (partOfSpeech == "interjection"):
            #     parseInterjection(word, cleanedLine)
            # elif (partOfSpeech == "interrogative"):
            #     parseInterrogative(word, cleanedLine)
            # elif (partOfSpeech == "noun"):
            #     parseNoun(word, cleanedLine)
            # elif (partOfSpeech == "particle"):
            #     parseParticle(word, cleanedLine)
            # elif (partOfSpeech == "preposition"):
            #     parsePreposition(word, cleanedLine)
            # elif (partOfSpeech == "pronoun"):
            #     parsePronoun(word, cleanedLine)
            # elif (partOfSpeech == "verb"):
            #     parseVerb(word, cleanedLine)
           
    if found == False:
        print "No Data"
    return request.data    #return the html of the word


def extractPartOfSpeech(line):
    
    found = False
    pos = 'not found'

    for x in line.split('\t'):
        if x == '':
            f = 2
        elif True:
            if found == True:
                words = x.split(' ')
                pos = words[0]
                break
        if x == "Parts of Speech:":
            found = True

    pos = pos.lower()

    pos = re.sub(',', '', pos)
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
    
    if (verse_count == 5):
        print(words)
    
    for word in words:
        
        if (contains_digits(word) == False):
            if (verse_count == 5 and word != '\u202b' and len(word) > 1):
                lookup_hebrew_word(word.replace("׃", ""))
            if (verse_count == 5):
                 print("Word not containing numbers: " + word)
            continue
        word = strip_rtl_characters(word)
        if (verse_count == 5):
            print("word containing numbers: " + word + "~")
        
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


