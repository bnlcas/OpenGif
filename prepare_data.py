import argparse
import io
import json
import pickle

def LoadWordVectors(word_vector_datafile, n_words):
    f = io.open(word_vector_datafile, 'r', encoding='utf-8', newline='\n', errors='ignore')
    n, d = map(int, f.readline().split())
    word_vector_dimension = d
    word_dict = {}
    if(n_words <= 0):
        n_words = n
    else:
        n_words = min(n, n_words)
    for i in range(n_words):
        line = f.readline()
        tokens = line.rstrip().split(' ')
        word_dict[tokens[0]] = [float(x) for x in tokens[1:]]
    return word_dict

parser = argparse.ArgumentParser(
    description='Prepare Dictionary for word vectors')
parser.add_argument('--word_count', dest='total_word_count', default=20000, type=int)
args = parser.parse_args()

total_word_count = args.total_word_count
word_vector_datafile = './Data/WordVectors/word_vectors.vec'
word_dict = LoadWordVectors(word_vector_datafile, total_word_count)

with open('./Data/WordVectors/word_dict.pkl', 'wb') as f:
    pickle.dump(word_dict, f)
