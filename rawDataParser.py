# -*- coding: utf-8 -*-

import re
from sys import argv
import pandas

interjection = {}
particle = {}
Nouns = {}
conjunctions = {}
adjectives = {}
prepositions = {}
interrogatives = {}
adverbs = {}
pronouns = {}

def parseData(filePath):
	partOfSpeechFile = open('partsOfSpeech.txt', 'w')

	rawDataFile = open(filePath)

	rawData = rawDataFile.readlines()

	for line in rawData:
		word = extractWord(line)
		partsOfSpeech = extractPartOfSpeech(line)
        
		for partOfSpeech in partsOfSpeech:
			speechLine = word + '\t' + partOfSpeech + '\n'
			partOfSpeechFile.write(speechLine)
			
			if partOfSpeech == 'Interjection':
				parseInterjection(line, word)
			if partOfSpeech == 'Particle':
				parseParticle(line, word)
			if partOfSpeech == 'Noun':
				parseNoun(line)
			if partOfSpeech == 'Preposition':
				parsePreoposition(line, word)
			if partOfSpeech == 'Conjunction':
				parseConjunction(line)
			if partOfSpeech == 'Adjective':
				parseAdjective(line)
			if partOfSpeech == 'Pronoun':
				relative = False
				parsePronoun(line, word, relative)
			if partOfSpeech == 'Relative':
				relative = True;
				parsePronoun(line, word, relative)
			if partOfSpeech == 'Interrogative':
				parseInterrogative(line, word)
			

def parseConjunction(line):
	word = '';
	root = '';
	strongsNumber = '';
	#parse line
	lineArray =  line.split('\t')
	while(True):
		try:
			lineArray.remove('')
		except:
			break
	for x in lineArray:
		if x == "Word Parsed:":
			word = lineArray[lineArray.index(x) + 1]
		if x == "Root:":
			root = lineArray[lineArray.index(x) + 1]
		if x == "Strong's Number:":
			strongsNumber = lineArray[lineArray.index(x) + 1]
	#add to dictionary
	conjunctions[word] = {'root': root, 'strongsNumber': strongsNumber}

def parseNoun(line):
	firstLevel = {}


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



	words = [x for x in words if x != 'Noun' and x != '']

	if "Proper" in words:
		firstLevel['Gender'] = "null"
		firstLevel['Number'] = "null"
		firstLevel['isProperNoun'] = "True"
	
	else:
		firstLevel['isProperNoun'] = "False"
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
			#print x
			if found == True:
				words = x.split(' ')
				break
		if x == "Root:":
			found = True
			


	
	words = [x for x in words if x != 'Noun' and x != ''  and x != "Proper"]

	firstLevel['Root'] = words[0]


	found = False

	for x in line.split('\t'):
		if x == '':
			f = 2
		elif True:
			if found == True:
				words = x.split(' ')
				break
		if x == "Strong's Number:":
			found = True
			


	
	words = [x for x in words if x != 'Noun' and x != '' ]

	firstLevel['Strong\'s Number'] = words[0]


	Nouns[word] = firstLevel
	
def parsePronoun(line,word, relative):
	word = '';
	root = '';
	strongsNumber = '';
	#parse line
	lineArray =  line.split('\t')
	while(True):
		try:
			lineArray.remove('')
		except:
			break
	for x in lineArray:
		if x == "Word Parsed:":
			word = lineArray[lineArray.index(x) + 1]
		if x == "Root:":
			root = lineArray[lineArray.index(x) + 1]
		if x == "Strong's Number:":
			strongsNumber = lineArray[lineArray.index(x) + 1]
		#add to dictionary
	pronouns[word] = {'Root': root, 'Strongs Number': strongsNumber, 'Relative': relative}	



def extractPartOfSpeech(line):
	found = False
    
	word_list = []

	for x in line.split('\t'):
		if x == '':
			f = 2
		elif True:
			if found == True:
				words = x.split(' ')
				for word in words:
				    word = word.replace(",", "")
				    if len(word) > 0:
				        word_list.append(word)
                    
				if 'Verb' in words:
					pos = 'verb'
				elif 'Particle' in words:
					pos = 'particle'
				else:
					pos = words[0]
				break
		if x == "Parts of Speech:":
			found = True

	return word_list
	
def parseAdjective(line):	
	word = ''
	root = ''
	gender = ''
	plurality = ''
	otherThing = ''
	strongsNumber = ''
	#parse line
	lineArray =  line.split('\t')
	while(True):
		try:
			lineArray.remove('')
		except:
			break
	for x in lineArray:
		if x == "Word Parsed:":
			word = lineArray[lineArray.index(x) + 1]
		if x == "Root:":
			root = lineArray[lineArray.index(x) + 1]
		if x == "Parts of Speech:":
			#print lineArray[lineArray.index(x) + 1]
			gender = lineArray[lineArray.index(x) + 1][17:20]
			plurality = lineArray[lineArray.index(x) + 1][22:26]
			plurality = plurality.strip()
			#print lineArray[lineArray.index(x) + 1][26:37]
		if x == "Strong's Number:":
			strongsNumber = lineArray[lineArray.index(x) + 1]
	#add to dictionary
	adjectives[word] = {'root': root, 'strongsNumber': strongsNumber, 'gender' : gender, 'plurality' : plurality}


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



def parseInterjection(line, word):
	interjection[word] = True
	
def parseParticle(line, word):
	particle[word] = True

def parsePreoposition(line, word):
	prepositions[word] = {}
	prepositions[word]["isPreposition"] = True
	prepositions[word]["isVerb"] = ("Verb" in line)
	prepositions[word]["isPronoun"] = ("Pronoun" in line)
	
def parseInterrogative():
	InterrogativeDict = dict()
	defList = []
	
	for line in hebFile:
		wordDef = []
		placeholder = line.split("\t")
		for e in placeholder:
			if(e != ''):
				if(e != ' '):
					wordDef.append(e)
		defList.append(wordDef);

	count = 0
	for e in defList:
		count += 1

def parseInterrogative(line, word):
	defList = []
	strongNum = ''

	placeholder = line.split("\t")
	for e in placeholder:
		if(e != ''):
			if(e != ' '):
				defList.append(e)
	for e in defList:
		if e == "Strong's Number:":
			strongNum = defList[(defList.index(e) + 1)]
		hebWord = word
		subLine = line
			
		poS = ''
		#Parts of Speech
		if "Noun" in subLine:
			poS += "Noun"
		elif "Adjective" in subLine:
			poS += "Adjective"
		elif "Adverb" in subLine:
			poS += "Adverb"
		elif "Conjunction" in subLine:
			poS += "Conjunction"
		elif "Pronoun" in subLine:
			poS += "Pronoun"
		elif "Preposition" in subLine:
			poS += "Preposition"
		elif "Verb" and "Qal" in subLine:
			poS += "Verb Qal"
		elif "Verb" and "Hiphil" in subLine:
			poS += "Verb Hiphil"
		elif "Verb" and "Niphal" in subLine:
			poS += "Verb Niphal"
		if "Negative" and "Particle" in subLine:
			poS += "Negative Particle"
			
			#Tenses
		if "Participle" in subLine:
			tense = "Participle"
		elif "Perfect" and "3" in subLine:
			tense = "Perfect 3rd"
		elif "Perfect" and "2" in subLine:
			tense = "Perfect 2nd"
		elif "Imperfect" and "2" in subLine:
			tense = "Imperfect 2nd"
		elif "Infinitive" and "Absolute" in subLine:
			tense = "Infinitive Absolute"
		else:
			tense = "None"
				
			#Gender
		if "Mas." in subLine:
			gender = "Mas."
		if "Fem." in subLine:
			gender = "Fem."
		if "Com." in subLine:
			gender = "Com."
		else:
			gender = "None"
				
			#Number
		if "Sing." and "Absolute" in subLine:
			number = "Singular Absolute"
		if "Sing." in subLine:
				number = "Sing."
		elif "Pl." in subLine:
			number = "Pl."
		else:
			number = "None"
		
		if not poS:
			poS = "None"
		wordDefTypes = ["pOS", "Gender", "Tense", "Number", "Strong's Number"]
		wordDefInfo = [poS, gender, tense, number, strongNum]
		attributeDict = dict(zip(wordDefTypes, wordDefInfo))
			
		interrogatives[hebWord] = attributeDict

# comment from my phone.
		#for w in interrogatives:
		#	print w
		#	for k in interrogatives[w]:
		#		print k + ": " + interrogatives[w][k]

def parseAdverb(line):        
	word = ''
	root = ''
	gender = ''
	plurality = ''
	strongsNumber = ''
	
	#parse line
	
	lineArray =  line.split('\t')
	while(True):
		try:
			lineArray.remove('')
		except:
			break
	
	for x in lineArray:
		if x == "Word Parsed:":
			word = lineArray[lineArray.index(x) + 1]
		
		if x == "Root:":
			root = lineArray[lineArray.index(x) + 1]
		
		if x == "Parts of Speech:":
			gender = lineArray[lineArray.index(x) + 1][17:20]
			plurality = lineArray[lineArray.index(x) + 1][22:26]
		
		if x == "Strong's Number:":
			strongsNumber = lineArray[lineArray.index(x) + 1]
	
	#add to dictionary
	adverbs[word] = {'root': root, 'strongsNumber': strongsNumber, 'gender' : gender, 'plurality' : plurality}


	#for w in interrogatives:
	#	print w
	#	for k in interrogatives[w]:
	#		print k + ": " + interrogatives[w][k]




def computeStatsForVerse(verse, partOfSpeech, key, value):
	#computeStatsForVerse(string verse, dictionary partOfSpeech, string key, string value)
	wordCount = 0
	foundWords = []
	for word in verse.split(" "):
		wordCount = wordCount + 1
		temp = ''
		if word in partOfSpeech:
			temp = partOfSpeech[word]
			if (temp[key] == value):
				foundWords.append(word)
	print str(len(foundWords)) + "/" + str (wordCount)
	return (len(foundWords) * 1.0) / (wordCount * 1.0)

def projectGenesisToVerses(filename):
    f = open(filename)
    dataset = []
    for line in f:
        if (line.find("xxxx") > -1):
            continue
        unsorted_parts = line.split("\xc2\xa0")
        parts = []
        for part in unsorted_parts:
            if len(part) > 0:
                parts.append(part)
        verse = (parts[3]).replace("\xd7\x83", "").replace('\u202b', "").replace('\u202c', "")
        cn = parts[2].replace("\xd7\x83", "")
        vn = parts[1]
       
        print cn + ":" + vn
        row = calculateDataForVerse(verse, cn, vn)
        
        dataset.append(row)
    return dataset
    
columns = [
    [prepositions, "isPreposition", True],
    [prepositions, "isVerb", True],
    [prepositions, "isPronoun", True]
    ]
    
def calculateDataForVerse(text, chapter, verse):
    words = text.split()
    data = [chapter, verse]
    # Calculate the values somehow?
    for column in columns:
        data.append(computeStatsForVerse(text, column[0], column[1], column[2]))
    return data
    
    

filePath = ''

if len(argv) < 2:
	print "Using Default File: raw_html_output_genesis.txt"
	filePath = 'raw_html_output_genesis.txt'
elif True:
	filePath = argv[1]

parseData(filePath)

df = pandas.DataFrame(projectGenesisToVerses("genesis.txt"))
writer = pandas.ExcelWriter('hallelujah.xlsx')
df.to_excel(writer,'data')
writer.save()


#print Nouns
