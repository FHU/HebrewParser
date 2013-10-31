# -*- coding: utf-8 -*-

import re
from sys import argv

Nouns = {}


prepositions = {}

def parseData(filePath):

	partOfSpeechFile = open('partsOfSpeech.txt', 'w')



	rawDataFile = open(filePath)

	rawData = rawDataFile.readlines()

	for line in rawData:
		
		word = extractWord(line)

		# if word != 'not found':
		# 	print word

		partOfSpeech = extractPartOfSpeech(line)

		speechLine = word + '\t' + partOfSpeech + '\n'

		partOfSpeechFile.write(speechLine)
		

		# if partOfSpeech == 'adjective':
		# 	parseAdjective(line)
		# elif partOfSpeech == 'adverb':
		# 	parseAdverb(line)
		# elif partOfSpeech == 'conjunction':
		# 	parseConjunction(line)
		# elif partOfSpeech == 'demonstrative':
		# 	parseDemonstrative(line)
		# elif partOfSpeech == 'determiner':
		# 	parseDeterminer(line)
		# elif partOfSpeech == 'interjection':
		# 	parseInterjection(line)
		# elif partOfSpeech == 'interrogative':
		# 	parseInterrogative(line)
		if partOfSpeech == 'noun':
			parseNoun(line)
		# elif partOfSpeech == 'particle':
		# 	parseParticle(line)
		if partOfSpeech == 'preposition':
		 	parsePreoposition(line, word)
		# elif partOfSpeech == 'pronoun':
		# 	parsePronoun(line)
		# elif partOfSpeech == 'verb':
		# 	parseVerb(line)
		




def parseNoun(line):
	word = extractWord(line)
	found = False
	for x in line.split('\t'):
		if x == '':
			f = 2
		elif True:
			if found == True:
				words = x.split(' ')
				break
		if x == "Parts of Speech:":
			found = True

	words = [x for x in words if x != 'Noun' and x != '' ]

	firstLevel = {}

	firstLevel['Gender'] = words[0]
	firstLevel['Number'] = words[1]

	for x in line.split('\t'):
		if x == '':
			f = 2
		elif True:
			if found == True:
				words = x.split(' ')
				break
		if x == "Parts of Speech:":
			found = True

	

	found = False

	for x in line.split('\t'):
		if x == '':
			f = 2
		elif True:
			print x
			if found == True:
				words = x.split(' ')
				break
		if x == "Root:":
			found = True
			


	
	words = [x for x in words if x != 'Noun' and x != '' ]

	firstLevel['Root'] = words[0]


	found = False

	for x in line.split('\t'):
		if x == '':
			f = 2
		elif True:
			print x
			if found == True:
				words = x.split(' ')
				break
		if x == "Strong's Number:":
			found = True
			


	
	words = [x for x in words if x != 'Noun' and x != '' ]

	firstLevel['Strong\'s Number'] = words[0]


	Nouns[word] = firstLevel



def extractPartOfSpeech(line):
    
    found = False
    pos = 'not found'

    for x in line.split('\t'):
        if x == '':
            f = 2
        elif True:
            if found == True:
                words = x.split(' ')
                if 'Verb' in words:
                	pos = 'verb'
                elif 'Particle' in words:
                	pos = 'particle'
                else:
                	pos = words[0]
                break
        if x == "Parts of Speech:":
            found = True

    pos = pos.lower()

    pos = re.sub(',', '', pos)
    return pos


def extractWord(line):
	found = False
	pos = 'not found'

	for x in line.split('\t'):
		if x == '':
			f = 2
		else:
			if found == True:
				words = x.split(' ')
				pos = words[0]
				break
		if x == "Word Parsed:":
			found = True

	pos = re.sub(',', '', pos)
	return pos


def parsePreoposition(line, word):
    prepositions[word] = True


filePath = ''

if len(argv) < 2:
	print "Using Default File: raw_html_output_genesis.txt"
	filePath = 'raw_html_output_genesis.txt'
elif True:
	filePath = argv[1]

parseData(filePath)


print Nouns