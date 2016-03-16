from nltk.corpus import indian
from nltk.tag import tnt
import nltk
import json
import io
from pymongo import MongoClient as mc
db=mc("192.168.101.5")
db=db["UNL"]
col=db["dic"]
def fetchUW(wrd):
	a=col.find_one({"hw":wrd})
	print(a)
	if a is None:
		return "UNK"
	else:
		return a["uw"]

def replacer(line):
	line=line.split(" ")
	a=[]
	for l in line:
		a.append(fetchUW(l))
	return "|".join(a)

li={}
with io.open('t', 'r', encoding='utf8') as f:
	for line in f:
		li[line]=replacer(line)
		with io.open('ans', 'w', encoding='utf8') as json_file:
    			json.dump(li, json_file, ensure_ascii=False,indent=4, sort_keys=True)
