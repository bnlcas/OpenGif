# OpenGif
This project provides a basic search tool to help find and share Animated Gifs.
The basic functionality is similar to exiting gif search engines like Tenor and Giphy. The hope is that messaging applications could use this tool as a secure open source, alternative to existing commercial gif search engines. This project is at a very basic level, but any interest or feedback is appreciated.
A basic demo can be run at www.opengif.net.

## How to run it:
Run `./setup.sh` to download and install the necessary data. This will download a set of word vectors from
[Facebook's FastText Word Vectors](https://fasttext.cc/docs/en/english-vectors.html) and convert them into a dictionary. Other sources of word vectors could be used instead. The python script `prepare_data.py` can also be rerun to generate a larger or smaller dictionary of english words.

#### Python Version (WIP as of 2020-05-20):
Runs on Python 3.6, and requires Numpy & Flask.
In the terminal run:
```bash
cd python_prototype/
pip3 install -r requirements.txt
python3 demo.py
```
Enter a search query and a description of the gif will come back.
An preliminary Flask prototype for a server based solution can be found in `/python_prototype/main.py` and this will serve the site found in `/web_interface`.

## How it works:
This algorithm relies on a semantic space representation of english tokens. The dot product is used to quickly calculate the distance  to calculate the semantic similarity between a search phrase a database of gifs. A more sophisticated similarity ranking that can handle logical dis/conjunction is the next step.

## Contributing:
This project is very new, and a lot needs to be done. Some things we need:

1. An improved website for demonstrating the basic functionality.
2. Adding gifs. The current demo has a very limited set of gifs. More gifs are needed to cover a greater range of uses.
3. Design/build an API for 3rd party use.
4. Improve the logic of the search algorithm to handle more complex queries (AND/OR).
5. Improve the performance of the search algorithm runs (possible switch to C++)
