import csv 

output = "D:\\MyDownloads\\fakenews.csv"
out = open(output, 'w', newline='')
writer = csv.writer(out)
try:
	with open('D:\\MyDownloads\\fake.csv', encoding='utf8') as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		for row in readCSV:
			writer.writerow((row[4],row[5],'fake'))
except:
	print("Error")

out.close()