# -*- coding: utf-8 -*-

import re
from sys import argv


def parseData(filePath):

	partOfSpeechFile = open('partsOfSpeech.txt', 'w')



	rawDataFile = open(filePath)

	rawData = rawDataFile.readlines()

	for line in rawData:
		
		word = extractWord(line)

		if word != 'not found':
			print word

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
		# elif partOfSpeech == 'noun':
		# 	parseNoun(line)
		# elif partOfSpeech == 'particle':
		# 	parseParticle(line)
		# elif partOfSpeech == 'preposition':
		# 	parsePreoposition(line)
		# elif partOfSpeech == 'pronoun':
		# 	parsePronoun(line)
		# elif partOfSpeech == 'verb':
		# 	parseVerb(line)
		







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


def extractWord(line):
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
		if x == "Word Parsed:":
			found = True

	pos = re.sub(',', '', pos)
	return pos



filePath = ''

if len(argv) < 2:
	print "Using Default File: raw_html_output_genesis.txt"
	filePath = 'raw_html_output_genesis.txt'
elif True:
	filePath = argv[1]

parseData(filePath)


