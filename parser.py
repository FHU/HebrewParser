from sys import argv


f = open(argv[1])

for verse in f:
    if (verse.find("xxxx") > -1):
        continue
    print(verse)
    