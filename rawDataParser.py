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
verbs = {}

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
				relative = True
				parsePronoun(line, word, relative)
			if partOfSpeech == 'Interrogative':
				parseInterrogative(line, word)
			if partOfSpeech == 'Verb':
				parseVerb(line)
			
	print adjectives
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
	tense = ''
	POS = ''
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
			if lineArray[lineArray.index(x) + 1][0] == "P":
				POS = "Pronoun"
				gender = lineArray[lineArray.index(x) + 1][26:30]
				if lineArray[lineArray.index(x) + 1][31] == "S":
					plurality = "Sing."
				elif lineArray[lineArray.index(x) + 1][31] == "P":
					plurality = "Pl."
				
				if lineArray[lineArray.index(x) + 1][35:45] == ". Absolute" or lineArray[lineArray.index(x) + 1][35:45] == "Absolute":
					tense = "Absolute"
				elif lineArray[lineArray.index(x) + 1][35:45] == ". Construct" or lineArray[lineArray.index(x) + 1][35:45] == "Construct":
					tense = "Construct"
				else:
					tense = "Unknown Tense"
			elif lineArray[lineArray.index(x) + 1][0] == "N":
				POS = "Noun"
				gender = lineArray[lineArray.index(x) + 1][23:27]
				if lineArray[lineArray.index(x) + 1][28] == "S":
					plurality = "Sing."
				elif lineArray[lineArray.index(x) + 1][28] == "P":
					plurality = "Pl."
								
				if lineArray[lineArray.index(x) + 1][32:42] == ". Absolute" or lineArray[lineArray.index(x) + 1][32:42] == "Absolute":
					tense = "Absolute"
				elif lineArray[lineArray.index(x) + 1][32:42] == ". Construct" or lineArray[lineArray.index(x) + 1][32:42] == "Construct":
					tense = "Construct"
				else:
					tense = "Unknown Tense"
			elif lineArray[lineArray.index(x) + 1][0:15] == "Adjective, Noun":
				POS = "Noun"
				gender = lineArray[lineArray.index(x) + 1][23:27]
				if lineArray[lineArray.index(x) + 1][28] == "S":
					plurality = "Sing."
				elif lineArray[lineArray.index(x) + 1][28] == "P":
					plurality = "Pl."
												
				if lineArray[lineArray.index(x) + 1][32:42] == ". Absolute" or lineArray[lineArray.index(x) + 1][32:42] == "Absolute":
					tense = "Absolute"
				elif lineArray[lineArray.index(x) + 1][32:42] == ". Construct" or lineArray[lineArray.index(x) + 1][32:42] == "Construct":
					tense = "Construct"
				else:
					tense = "Unknown Tense"
			elif lineArray[lineArray.index(x) + 1][0] == "I":
				POS = "Interrogative"
				gender = lineArray[lineArray.index(x) + 1][32:36]
				if lineArray[lineArray.index(x) + 1][37] == "S":
					plurality = "Sing."
				elif lineArray[lineArray.index(x) + 1][37] == "P":
					plurality = "Pl."
							
				if lineArray[lineArray.index(x) + 1][41:51] == ". Absolute" or lineArray[lineArray.index(x) + 1][41:51] == "Absolute":
					tense = "Absolute"
				elif lineArray[lineArray.index(x) + 1][41:51] == ". Construct" or lineArray[lineArray.index(x) + 1][41:51] == "Construct":
					tense = "Construct"
				else:
					tense = "Unknown Tense"
			elif lineArray[lineArray.index(x) + 1][0] == "D":
				POS = "Direct, Object"
				gender = lineArray[lineArray.index(x) + 1][45:49]
				if lineArray[lineArray.index(x) + 1][50] == "S":
					plurality = "Sing."
				elif lineArray[lineArray.index(x) + 1][50] == "P":
					plurality = "Pl."
											
				if lineArray[lineArray.index(x) + 1][54:64] == ". Absolute" or lineArray[lineArray.index(x) + 1][54:64] == "Absolute":
					tense = "Absolute"
				elif lineArray[lineArray.index(x) + 1][54:64] == ". Construct" or lineArray[lineArray.index(x) + 1][54:64] == "Construct":
					tense = "Construct"
				else:
					tense = "Unknown Tense"
			elif lineArray[lineArray.index(x) + 1][0:17] == "Adverb, Adjective":
				POS = "Adverb"
				gender = lineArray[lineArray.index(x) + 1][25:29]
				if lineArray[lineArray.index(x) + 1][30] == "S":
					plurality = "Sing."
				elif lineArray[lineArray.index(x) + 1][30] == "P":
					plurality = "Pl."
														
				if lineArray[lineArray.index(x) + 1][34:44] == ". Absolute" or lineArray[lineArray.index(x) + 1][34:44] == "Absolute":
					tense = "Absolute"
				elif lineArray[lineArray.index(x) + 1][34:44] == ". Construct" or lineArray[lineArray.index(x) + 1][34:44] == "Construct":
					tense = "Construct"
				else:
					tense = "Unknown Tense"
			elif lineArray[lineArray.index(x) + 1][0:12] == "Interjection":
				POS = "Interjection"
				gender = lineArray[lineArray.index(x) + 1][31:35]
				if lineArray[lineArray.index(x) + 1][36] == "S":
					plurality = "Sing."
				elif lineArray[lineArray.index(x) + 1][36] == "P":
					plurality = "Pl."
										
				if lineArray[lineArray.index(x) + 1][40:50] == ". Absolute" or lineArray[lineArray.index(x) + 1][40:50] == "Absolute":
					tense = "Absolute"
				elif lineArray[lineArray.index(x) + 1][40:50] == ". Construct" or lineArray[lineArray.index(x) + 1][40:50] == "Construct":
					tense = "Construct"
				else:
					tense = "Unknown Tense"
			else:
				POS = "Adjective"
				gender = lineArray[lineArray.index(x) + 1][17:21].strip()
				if lineArray[lineArray.index(x) + 1][22] == "S" or lineArray[lineArray.index(x) + 1][21] == "S":
					plurality = "Sing."
				elif lineArray[lineArray.index(x) + 1][22] == "P" or lineArray[lineArray.index(x) + 1][21] == "P":
					plurality = "Pl."
			
				if lineArray[lineArray.index(x) + 1][26:36] == ". Absolute" or lineArray[lineArray.index(x) + 1][26:36] == "Absolute":
					tense = "Absolute"
				elif lineArray[lineArray.index(x) + 1][26:36] == ". Construct" or lineArray[lineArray.index(x) + 1][26:36] == "Construct":
					tense = "Construct"
				else:
					tense = "Unknown Tense"
		if x == "Strong's Number:":
			strongsNumber = lineArray[lineArray.index(x) + 1]
	#add to dictionary
	adjectives[word] = {'POS' : POS, 'root': root, 'strongsNumber': strongsNumber, 'Gender' : gender, 'Number' : plurality, 'Tense': tense }
	


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
	interjection[word] = {}
	interjection[word]["isInterjection"] = True
	
def parseParticle(line, word):
	particle[word] = {}
	particle[word]["isParticle"] = True

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
		wordDefTypes = ["isInterrogative","pOS", "Gender", "Tense", "Number", "Strong's Number"]
		wordDefInfo = [True, poS, gender, tense, number, strongNum]
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



def parseVerb(line):
	word = 'Not Found'
	root = 'Not Found'
	gender = 'Not Found'
	number = 'Not Found'
	tense = 'Not Found'
	stem = 'Not Found'
	line = re.sub(',', '', line)
	s1 = []
	for x in line.split('\t'):
		i = -1
		u = x.split(' ')
		if x!='':
			for y in x.split(' '):
				if y!='':
					s1.append(y)
	for z in s1:
		if z == 'Parsed:':
			word = s1[s1.index(z) + 1]
		if z == 'Root:':
			root = s1[s1.index(z) + 1]
		if z == 'Verb':
			stem = s1[s1.index(z) + 1]
			tense = s1[s1.index(z) + 2]
			if tense == 'Participle':
				gender = 'Not Found'
				number = 'Not Found'
			elif tense == 'Imperative':
				gender = 'Not Found'
				number = 'Not Found'
			elif tense == 'Infinitive':
				tense += (' ' + s1[s1.index(z) + 3])
				gender = 'Not Found'
				number = 'Not Found'
			else:
				gender = s1[s1.index(z) + 5]
				number = s1[s1.index(z) + 6]
	#print gender
	verbs[word] = {'root': root, 'gender': gender ,'number': number ,'tense': tense, 'stem': stem}





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
	#print str(len(foundWords)) + "/" + str (wordCount)
	if wordCount == 0:
	    return 0
	return (len(foundWords) * 1.0) / (wordCount * 1.0)

def projectGenesisToVerses(filename):
    f = open(filename)
    dataset = {}
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
       
        #print cn + ":" + vn
        row = calculateDataForVerse(verse, cn, vn)
        
        for column in row:
        	if not column in dataset:
        		dataset[column] = []
        	dataset[column].append(row[column])
    return dataset
    
columns = [
    ["Prepositions",prepositions, "isPreposition", True],
    ["Prepositions_verb", prepositions, "isVerb", True],
    ["Prepositions_pronoun",prepositions, "isPronoun", True],

    ["Particle",particle, "isParticle", True],
    
    ["Propernouns",Nouns, "isProperNoun", "True"],
    
    ["Interjection",interjection, "isInterjection", True],

	["Verb_Mas", verbs, "gender", "Mas."],
	["Verb_Fem", verbs, "gender", "Fem."],
	["Verb_Com", verbs, "gender", "Com."],
	
	["Interrogative",interrogatives, "isInterrogative", True],
	
    ["Interrogative_negativeParticle",interrogatives, "pOS", "Negative Particle"],
    ["Interrogative_adverb",interrogatives, "pOS", "Adverb"],
    ["Interrogative_adjective",interrogatives, "pOS", "Adjective"],
    ["Interrogative_qal",interrogatives, "pOS", "Verb Qal"],
    ["Interrogative_hiphil",interrogatives, "pOS", "Verb Hiphil"],
    ["Interrogative_niphal",interrogatives, "pOS", "Verb Niphal"],
    ["Interrogative_Noun",interrogatives, "pOS", "Noun"],
    ["Interrogative_conjunction",interrogatives, "pOS", "Conjunction"],
    ["Interrogative_verb",interrogatives, "pOS", "Verb"],

    ["Interrogative_tense_participle",interrogatives, "Tense", "Participle"], 
    ["Interrogative_p3rd",interrogatives, "Tense", "Perfect 3rd"],
    ["Interrogative_p2nd",interrogatives, "Tense", "Perfect 2nd"],   
    ["Interrogative_infinitiveAbsolute", interrogatives, "Tense", "Infinitive Absolute"],

    ["Interrogative_pl",interrogatives, "Number", "Pl."],
    ["Interrogative_sing",interrogatives, "Number", "Sing."],

    ["Interrogative_mas",interrogatives, "Gender", "Mas."],
    ["Interrogative_fem",interrogatives, "Gender", "Fem."],
	
	["Adjective_pl", adjectives, "Number", "Pl."],
	["Adjective_sing", adjectives, "Number", "Sing."],
		
	["Adjective_mas", adjectives, "Gender", "Mas."],
	["Adjective_fem", adjectives, "Gender", "Fem."],
	["Adjective_absolute", adjectives, "Tense", "Absolute"],
	["Adjective_construct", adjectives, "Tense", "Construct"],
	
	["Adjective_noun", adjectives, "POS", "Noun"],
	["Adjective_pronoun", adjectives, "POS", "Pronoun"],
	["Adjective_directObject", adjectives, "POS", "Direct, Object"],
	["Adjective_interrogative", adjectives, "POS", "Interrogative"],
	["Adjective_interjection", adjectives, "POS", "Interjection"],
	["Adjective_adjective", adjectives, "POS", "Adjective"],
	["Adjective_adverb", adjectives, "POS", "Adverb"]
	
    ]
    
def calculateDataForVerse(text, chapter, verse):
    words = text.split()
    data = {}
    data["chapter"] = chapter
    data["verse"] = verse
    # Calculate the values somehow?
    for column in columns:
    	val = computeStatsForVerse(text, column[1], column[2], column[3])
        data[column[0]] = val
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
