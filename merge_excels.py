import pandas


hm = pandas.ExcelFile("human_evaluation_data.xlsx")
human_data = hm.parse("Sheet1")

hl = pandas.ExcelFile("hallelujah.xlsx")
computer_data = hl.parse("data")

new_data = {}

for key in human_data:
    if not key == "Verse Content":
        new_data[key] = human_data[key]
    
for key in computer_data:
    new_data[key+"_computer"] = computer_data[key]

df = pandas.DataFrame(new_data)
writer = pandas.ExcelWriter('final_dataset.xlsx')
df.to_excel(writer,'data')
writer.save()

# Produce ARFF

f = open("genesis.arff", "w+")
f.write("% Title: Reallywritter\n%\n@RELATION text\n")

for key in new_data:
    f.write("@ATTRIBUTE\t"+key+"\t")
    if key == "Genre":
        f.write("{Genealogy, Narrative, Blessing, Law, Covenant}")
    elif key == "hasElohim" or key == "hasYHWH":
        f.write("{Y, N}")
    elif key == "Classification":
        f.write("{J, E, P, D}")
    else:
        f.write("NUMERIC")
    f.write("\n")


f.write("\n@DATA\n")

verses = new_data["Verse"]

for i in xrange(0, len(verses)):
    first = True
    for key in new_data:
        if not first:
            f.write(",")
        arr = new_data[key]
        f.write(str(arr[i]))
        first = False
    f.write("\n")
f.close()

