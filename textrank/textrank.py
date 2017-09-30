#-*- encoding:utf-8 -*-
from  textrank4zh import TextRank4Keyword,TextRank4Sentence
import codecs

file = r"E:\GrgBanking_task\关键词提取\textrank\test_text.txt"
text = codecs.open(file,'r','utf-8').read()

print ('提取关键词:')
word = TextRank4Keyword()
word.analyze(text, window = 7, lower = True)
w_list = word.get_keywords(num = 3, word_min_len = 1)
for w in w_list:
  print (w.word, w.weight)

print ('提取关键词组:')
phrase = word.get_keyphrases(keywords_num = 5, min_occur_num=2)
for p in phrase:
  print (p)

print ('提取关键句:')
sentence = TextRank4Sentence()
sentence.analyze(text, lower = True)
s_list = sentence.get_key_sentences(num = 1, sentence_min_len = 5)
for s in s_list:
  print (s.sentence,s.weight)



