
import storer

import argparse
from flask import Flask, jsonify, request, Response
app = Flask(__name__)

db_path = storer.db_name

@app.route('/temperature/', methods=['GET'])
def temperature():
    args = request.args
    limit = args.get('limit')
    if limit is not None:
        limit = int(limit)

    s = storer.Sqlite3Storer(db_path)
    result = []
    for r in s.list_gen(limit):
        result.append({'timestamp': r.timestamp, 'value': r.value})
    return jsonify(result)

@app.route('/temperature/chart', methods=['GET'])
def chart():  # pragma: no cover
    content = open('chart.html')
    return Response(content, mimetype="text/html")

def process_command_line():
    parser = argparse.ArgumentParser(description='Web Service.')
    parser.add_argument('--db-path', dest='db_path', default=storer.db_name,
                        help='full path to db')
    parser.add_argument('--debug', dest='debug', action='store_true',
                        help='debug mode')
    return parser.parse_args()

if __name__ == '__main__':
    options = process_command_line()
    db_path = options.db_path
    app.run(host='0.0.0.0', debug=options.debug)
