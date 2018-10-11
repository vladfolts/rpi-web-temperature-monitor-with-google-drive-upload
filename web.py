
import storer

from flask import Flask, jsonify, request, Response
app = Flask(__name__)

@app.route('/temperature/', methods=['GET'])
def temperature():
    args = request.args
    limit = args.get('limit')
    if limit is not None:
        limit = int(limit)

    s = storer.Sqlite3Storer()
    result = []
    for r in s.list_gen(limit):
        result.append({'timestamp': r.timestamp, 'value': r.value})
    return jsonify(result)

@app.route('/temperature/chart', methods=['GET'])
def chart():  # pragma: no cover
    content = open('chart.html')
    return Response(content, mimetype="text/html")

if __name__ == '__main__':
    app.run(debug=True)