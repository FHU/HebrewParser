import pandas


hm = pandas.ExcelFile("human_evaluation_data.xlsx")
human_data = hm.parse("Sheet1")

hl = pandas.ExcelFile("hallelujah.xlsx")
computer_data = hl.parse("data")

new_data = {}

for key in human_data:
    new_data[key] = human_data[key]
    
for key in computer_data:
    new_data[key+"_computer"] = computer_data[key]
    
df = pandas.DataFrame(new_data)
writer = pandas.ExcelWriter('final_dataset.xlsx')
df.to_excel(writer,'data')
writer.save()

