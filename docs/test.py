from nltk.corpus import indian
from nltk.tag import tnt
import nltk
import json
import io


def pos_tag(query):
	train_data = indian.tagged_sents('hindi.pos')
	tnt_pos_tagger = tnt.TnT()
	tnt_pos_tagger.train(train_data) 
	#test_data = ("भारतीय संस्कृति में नारी के सम्मान को बहुत महत्व दिया गया है।")
	a=tnt_pos_tagger.tag(nltk.word_tokenize(query))
	return a

li={}
with io.open('t', 'r', encoding='utf8') as f:
	for line in f:
		li[line]=pos_tag(line)
	with io.open('ans', 'a', encoding='utf8') as json_file:
    		json.dump(li, json_file, ensure_ascii=False,indent=2)
