mkdir WordVectors
curl https://dl.fbaipublicfiles.com/fasttext/vectors-english/wiki-news-300d-1M.vec.zip -o ./WordVectors/word_vectors.zip
unzip ./WordVectors/word_vectors.zip -d ./Data/WordVectors/
rm ./Data/WordVectors/word_vectors.zip
mv ./Data/WordVectors/wiki-news-300d-1M.vec ./Data/WordVectors/word_vectors.vec
python3 prepare_data.py --word_count 10000
