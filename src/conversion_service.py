import sys

from flask import Flask
from flask import jsonify
from flask import abort
from flask import request

sys.path.insert(1, "../../parsey-mcparseface-service/src/")
from parse_tree_parser import parse_ascii_tree
from parse_tree_to_displacy import parse_tree_to_displacy_tree
from run_parsey import run_parsey

app = Flask(__name__)

@app.route('/parsey-to-displacy', methods=['POST'])
def convert():
    print "Request.get_json():\n%s" % str(request.get_json(force=True))
    sentence = request.get_json()['text']
    print "Sentence is: %s" % sentence
    ascii_tree = run_parsey(sentence)
    print("\nAscii tree is:\n%s\n" % ascii_tree)
    response = jsonify(parse_tree_to_displacy_tree(parse_ascii_tree(ascii_tree)))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True, debug=True)