from flask import Flask, request
import json
import sys
import os
sys.path.insert(1, os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    os.pardir,
))

from api import process_docs
import search

app = Flask(__name__)


@app.route('/process_raw', methods=['GET', 'POST'])
def process_raw():
    if request.method == 'POST':
        doc = request.form.get('doc')
        source = request.form.get('source')
        doc_id = request.form.get('doc_id')
        filetype = request.form.get('filetype')
    else:
        doc = request.args.get('doc')
        source = request.args.get('source')
        doc_id = request.args.get('doc_id')
        filetype = request.args.get('filetype')

    return Response(process_docs.process_raw(doc, source, doc_id, filetype))


@app.route('/process', methods=['GET', 'POST'])
def process():
    doc = json.loads(request.args.get('doc'))
    timestamp = request.args.get('timestamp')
    doc = process_docs.process(doc, timestamp)
    search.update('scrapi', doc, 'article')
    return doc


@app.route('/search', methods=['GET'])
def search_search():
    query = request.args.get('doc')
    start = request.args.get('from')
    to = request.args.get('to')
    return json.dumps(search.search(query, start, to))


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=1337,
        debug=True
    )
