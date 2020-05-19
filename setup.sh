mkdir WordVectors
curl https://dl.fbaipublicfiles.com/fasttext/vectors-english/wiki-news-300d-1M.vec.zip -o ./WordVectors/word_vectors.zip
unzip ./WordVectors/word_vectors.zip -d ./WordVectors/
rm ./WordVectors/word_vectors.zip
mv ./WordVectors/wiki-news-300d-1M.vec ./WordVectors/word_vectors.vec
