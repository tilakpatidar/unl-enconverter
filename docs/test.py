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
query="आगे खतरा है"
result=pos_tag(query)
with io.open('op.txt', 'w', encoding='utf8') as json_file:
    json.dump(result, json_file, ensure_ascii=False)
