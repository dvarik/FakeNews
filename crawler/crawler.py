import json
import csv 
import sys

file = "D:\MyDownloads\crawlednews.jsonl"
output = "D:\\MyDownloads\\real.csv"
out = open(output, 'w', newline='')
writer = csv.writer(out)
with open(file) as f:
	for line in f:
		try:
			j_content = json.loads(line)
			if j_content['source'].startswith('Reuters'):
				writer.writerow((j_content['title'], j_content['content'].replace('\n',''),'real'))
		except:
			print("Badly formed json, ignoring")
			
out.close();