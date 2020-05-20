from flask import Flask
from flask import request
from flask import render_template
from GifFinder import GifFinder
import json

gif_finder = GifFinder(word_vector_datafile = '../WordVectors/word_vectors.vec', total_word_count = 10000)
app = Flask(__name__,  template_folder='../web_interface', static_folder='../web_interface/static')
#static_folder='web/static',
#template_folder='web/templates'

@app.before_request
def before_request():
    # When you import jinja2 macros, they get cached which is annoying for local
    # development, so wipe the cache every request.
    if 'localhost' in request.host_url or '0.0.0.0' in request.host_url:
        app.jinja_env.cache = {}


@app.route('/query', methods = ['POST'])
def query():
    data = request.get_data()
    data_json = json.loads(data)
    search_phrase = data_json['search']
    print(search_phrase)
    search_result_inds = gif_finder.FindGif(search_phrase)
    result = {'result1': gif_finder.gif_titles[search_result_inds[0]]}
    return json.dumps(result)

@app.route("/")
def index():
    return render_template('opengif.html')

if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['TESTING'] = True
    app.run(debug=True)
