from nltk.corpus import indian
from nltk.tag import tnt
from nltk.tokenize import sent_tokenize
import nltk
import json
import io
train_data = indian.tagged_sents('hindi.pos')
tnt_pos_tagger = tnt.TnT()
tnt_pos_tagger.train(train_data) 
test_data = ("भारतीय संस्कृति में नारी के सम्मान को बहुत महत्व दिया गया है। नारी शिक्षा कहा गया है जंहा स्त्रियों की पूजा होती है वंहा देवता निवास करते हैं । प्राचीन काल से ही नारी को ‘गृह देवी’ या ‘गृह लक्ष्मी’ कहा जाता है ।")
ts=test_data.split("।")
#s=sent_tokenize(test_data)

#a=tnt_pos_tagger.tag(nltk.word_tokenize(test_data))
with io.open('op.txt', 'w', encoding='utf8') as json_file:
    json.dump(ts, json_file, ensure_ascii=False)

