from GifFinder import GifFinder

gif_finder = GifFinder(total_word_count = 20000, word_vector_datafile = '../WordVectors/word_vectors.txt')
gif_finder.FindGif()

test_phrase = 'party'
search_result_inds = gif_finder.FindGif(test_phrase)
gif_finder.gif_ids[search_result_inds[0]]
print('Search phrase: "' + test_phrase + '"\n' + 'option 1: ' + emoji_description[emoji_inds[0]] + '\noption 2:' + emoji_description[emoji_inds[1]] + '\noption 3:' + emoji_description[emoji_inds[2]])
