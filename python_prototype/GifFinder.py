#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 13:11:32 2018

@author: benjaminlucas
"""
import numpy as np
import io

class GifFinder():
    def __init__(self, total_word_count = 20000, word_vector_datafile = '../WordVectors/word_vectors.txt'):
        self.word_vector_dimension = 200
        self.total_word_count = 20000
        self.LoadWordVecs(total_word_count, total_word_count, word_vector_datafile)
        self.LoadGifData()
        self.GenerateGifMatrix()

    def LoadWordVecs(self, n_words, word_vector_datafile):
        data = self.LoadWordVecRaw(n_words)
        word_mat = np.zeros([len(data), self.word_vector_dimension])
        word_dict = {}
        row_ind = 0
        for row in data:
            entries = row.split(' ')
            word_dict[entries[0]] = row_ind
            vec = [float(entries[i]) for i in range(1,self.word_vector_dimension + 1)]
            word_mat[row_ind,:] = vec
            row_ind += 1
        self.word_dict = word_dict
        self.word_matrix = word_mat

    def LoadWordVecRaw(self, n_tokens, word_vector_datafile):
        f = open(word_vector_datafile,'r')
        f.readline()
        f.readline() # Remove first two lines of header data
        data = []
        for i in range(n_tokens):
            data.append(f.readline())
            f.close()
        return data

    def LoadGifData(self):
        with open('../GIF_Data/gif_description.txt', 'r') as f:
            raw_txt_data = f.readlines()
        raw_gif_data = [x for x in raw_txt_data if(x[0] != '\n' and x[0] != '#')]
        #TODO: parse gif_data:
        gif_ids = [gif_data[0] for gif_data in raw_gif_data]
        gif_description = [gif_data[1] for gif_data in raw_gif_data]
        self.gif_ids = gif_ids
        self.gif_description = gif_description

    def GenerateGifMatrix(self):
        gif_matrix = np.zeros([len(self.gif_description), self.word_vector_dimension])
        for i, gif in enumerate(self.gif_description):
            vec = MakePhraseVec(gif)
            gif_matrix[i,:] = vec
        self.gif_matrix = gif_matrix

    def MakePhraseVec(self, phrase):
        stop_chars = [':', ';', '-',',']
        for c in stop_chars:
            phrase = phrase.replace(c,' ')
        words = phrase.lower().split(' ')
        words = [w for w in words if len(w) > 1]
        word_inds = []
        for w in words:
            try:
                word_inds.append(self.word_dict[w])
            except:
                print('word not found in dictionary')
        if(len(word_inds) > 0):
            phrase_mat = self.word_matrix[word_inds,:]
            phrase_vec = np.sum(phrase_mat, axis=0)
            phrase_vec_norm = phrase_vec/(np.linalg.norm(phrase_vec))
            return phrase_vec_norm
        else:
            print('no words recognized in phrase')
            return np.zeros([1,self.word_vector_dimension])

    def FindGif(self, search_phrase, n_results = 5):
        search_phrase_vector = MakePhraseVec(search_phrase)
        similarity = np.matmul(self.gif_matrix, np.transpose(search_phrase_vector))
        sort_inds = np.flipud(np.argsort(similarity))
        return list(sort_inds[0:n_results])
