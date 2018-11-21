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
IMDB_train_load = pd.read_csv()
IMDB_train_load['spaced'] = IMDB_train_load.text.apply(nlp)

IMDB_test_load = pd.read_csv()
IMDB_test_load['spaced'] = IMDB_test_load.text.apply(nlp)

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
  
IMDB_train_load['lemma'] = spacy_lemma_stop(IMDB_train_load)
IMDB_test_load['lemma'] = spacy_lemma_stop(IMDB_test_load)

IMDB_train_load = IMDB_train_load.drop(columns=['spaced', 'text'])
IMDB_train_load = IMDB_train_load.rename(index=str, columns={"lemma": "text"})
IMDB_train_load.to_csv(, index=False)

IMDB_test_load = IMDB_test_load.drop(columns=['spaced','text'])
IMDB_test_load = IMDB_test_load.rename(index=str, columns={"lemma": "text"})
IMDB_test_load.to_csv(, index=False)
