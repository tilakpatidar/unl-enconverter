import re,io,json
import pymongo
db=pymongo.MongoClient("192.168.101.5")
db=db["UNL"]
col=db.dic
regex_pattern="\[(.*?)\]\s*?\{(.*?)\}\s*?\"(.*?)\"\s*?\((.*?)\)\s*\<(.*?)\>\s*?;"

with io.open('UW-Hindi_Dict-20131003.txt', 'r', encoding='utf8') as f:
	for line in f:
		try:
			p=re.compile(regex_pattern)
			data=p.search(line)
			print (len(data.groups()))
			last=data.groups(2)[4].split(",")
			
			js={
			"line":line,
			"hw":data.groups(2)[0],
			"word_id":data.groups(2)[1],
			"uw":data.groups(2)[2],
			"attr":data.groups(2)[3].split(","),
			"lang_flg":last[0],
			"freq":int(last[1]),
			"priority":int(last[2])				
			}
			col.insert(js,w=0)
		except Exception as e:
			print (e)
		
