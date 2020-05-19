from GifFinder import GifFinder

gif_finder = GifFinder(word_vector_datafile = '../WordVectors/word_vectors.vec', total_word_count = 10000)

test_phrase = 'party'
search_result_inds = gif_finder.FindGif(test_phrase)
print('Sample search query: ' + test_phrase)
for i in range(min(3, len(search_result_inds))):
    print('option ' + str(i + 1) + ': ' + gif_finder.gif_titles[search_result_inds[i]])

print('try another search query')
while True:
    phrase = input()
    search_result_inds = gif_finder.FindGif(phrase)
    for i in range(min(3, len(search_result_inds))):
        print('option ' + str(i + 1) + ': ' + gif_finder.gif_titles[search_result_inds[i]])
