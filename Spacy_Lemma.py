#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 09:40:19 2018

@author: slowking
"""

import pandas as pd
import spacy

nlp = spacy.load('en')
print(nlp.pipeline)

#Load Data
Texts_train_load = pd.read_csv()
Texts_train_load['spaced'] = Texts_train_load.text.apply(nlp)

Texts_test_load = pd.read_csv()
Texts_test_load['spaced'] = Texts_test_load.text.apply(nlp)

def spacy_lemma_stop(data):
    corpus = list()
    for each in data.spaced:
        lemma_stop = list()
        for token in each:
            if token.is_stop == False:  
                lemma_stop.append(token.lemma_) 
                words = ' '.join(lemma_stop)
        corpus.append(words)  
    return corpus
  
Texts_train_load['lemma'] = spacy_lemma_stop(Texts_train_load)
Texts_test_load['lemma'] = spacy_lemma_stop(Texts_test_load)

Texts_train_load = Texts_train_load.drop(columns=['spaced', 'text'])
Texts_train_load = Texts_train_load.rename(index=str, columns={"lemma": "text"})
Texts_train_load.to_csv(, index=False)

Texts_test_load = Texts_test_load.drop(columns=['spaced','text'])
Texts_test_load = Texts_test_load.rename(index=str, columns={"lemma": "text"})
Texts_test_load.to_csv(, index=False)
