# OpenGif
This project provides a basic search tool to help find and share Animated Gifs.
The basic functionality is similar to exiting gif search engines like Tenor and Giphy. The hope is that messaging applications could use this tool as a secure, open source, alternative to existing commercial gif search engines.

## How to run it:
Run `./setup.sh` to download and install the necessary data. This will download a set of word vectors from
[Facebook's FastText Word Vectors](https://fasttext.cc/docs/en/english-vectors.html).

#### Python Version (WIP as of 2020-05-18):
Runs on Python 3.6, and requires numpy.
Run `python3 search_gif.py`
Enter a search query and a description of the gif will come back

## How it works:
This algorithm relies on a semantic space representation of english tokens. The dot product is used to quickly calculate the distance  to calculate the semantic similarity between a search phrase a database of gifs.

## Contributing:
This project is very new, and a lot needs to be done. Some things we need:

1. A website demonstrating the basic functionality.
2. Figure out how to host this and make it run well server side.
3. Improve the performance of the search algorithm runs (switch to C++)
4. Adding gifs we need more gifs to be added to the database.
