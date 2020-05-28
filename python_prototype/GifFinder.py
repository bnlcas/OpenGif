#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 13:11:32 2018

@author: benjaminlucas
"""
import numpy as np
import pickle
import json

class GifFinder():
    def __init__(self, word_vector_datafile = '../Data/WordVectors/word_dict.pkl'):
        self.word_vector_dimension = 0
        self.total_word_count = 0
        self.LoadGifData()
        print('loading word vectors')
        self.word_dict = self.LoadWordVectors(word_vector_datafile)
        self.gif_matrix = self.GenerateGifMatrix()
        print('ready')

    def LoadGifData(self):
        f = open('../Data/GIF_Data/gif_data.json', 'r')
        json_data = json.load(f)
        gif_data = json_data['gifs']
        self.gif_filenames = [gif['filename']  for gif in gif_data]
        self.gif_titles = [gif['title']  for gif in gif_data]
        self.gif_descriptions = [gif['description']  for gif in gif_data]

    def LoadWordVectors(self, word_vector_datafile):
        with open(word_vector_datafile, 'rb') as f:
            word_dict = pickle.load(f)
        self.total_word_count = len(word_dict.keys())
        self.word_vector_dimension = len(next(iter(word_dict.values())))
        return word_dict

    def GenerateGifMatrix(self):
        gif_matrix = np.zeros([len(self.gif_descriptions), self.word_vector_dimension])
        for i, gif in enumerate(self.gif_descriptions):
            vec = self.MakePhraseVector(gif)
            gif_matrix[i,:] = vec
        return gif_matrix

    def MakePhraseVector(self, phrase):
        phrase = phrase.lower()
        stop_chars = [':', ';', '-',',']
        for c in stop_chars:
            phrase = phrase.replace(c,' ')
        words = phrase.lower().split(' ')
        words = [w for w in words if len(w) > 1 and w in self.word_dict]
        phrase_vec = []
        for w in words:
            if(len(phrase_vec) == 0):
                phrase_vec = self.word_dict[w]
            else:
                phrase_vec = np.add(phrase_vec, self.word_dict[w])
        if(len(words) > 0):
            phrase_vec_norm = phrase_vec/(np.linalg.norm(phrase_vec))
            return phrase_vec_norm
        else:
            print('no words recognized in phrase')
            phrase_vec = self.word_dict['question']
            phrase_vec_norm = phrase_vec/(np.linalg.norm(phrase_vec))
            return phrase_vec_norm

    def FindGif(self, search_phrase, n_results = 5):
        search_phrase_vector = self.MakePhraseVector(search_phrase)
        similarity = np.matmul(self.gif_matrix, np.transpose(search_phrase_vector))
        sort_inds = np.flipud(np.argsort(similarity))
        return list(sort_inds[0:n_results])
