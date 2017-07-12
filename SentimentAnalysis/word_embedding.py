#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：利用大语料生成词语的索引字典、词向量，然后保存为pkl文件
"""

import pickle
import logging


import numpy as np
np.random.seed(1337)  # For Reproducibility

from preprocess.TextSta import TextSta
from gensim.models.word2vec import Word2Vec
from gensim.corpora.dictionary import Dictionary

# 创建词语字典，并返回word2vec模型中词语的索引，词向量
def create_dictionaries(p_model):
    gensim_dict = Dictionary()
    gensim_dict.doc2bow(p_model.wv.vocab.keys(), allow_update=True)
    w2indx = {v: k + 1 for k, v in gensim_dict.items()}  # 词语的索引，从1开始编号
    w2vec = {word: model[word] for word in w2indx.keys()}  # 词语的词向量
    return w2indx, w2vec

# 主程序
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

print ("请选择大语料的分词文本...")
T = TextSta("data/pre_reviews.txt")
sentences = T.sen()    # 获取句子列表，每个句子又是词汇的列表


print ('训练Word2vec模型')
model = Word2Vec(sentences,
                 size=100,  # 词向量维度
                 min_count=5,  # 词频阈值
                 window=5)  # 窗口大小


model.save('word_embedding' + u'.model')  # 保存模型

# 索引字典、词向量字典
index_dict, word_vectors= create_dictionaries(model)

# 存储为pkl文件
output = open('dict_word2vec' + u".pkl", 'wb')
pickle.dump(index_dict, output)  # 索引字典
pickle.dump(word_vectors, output)  # 词向量字典
output.close()

if __name__ == "__main__":
    pass
