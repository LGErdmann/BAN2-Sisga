from connection import get_conn
from flask import Flask, request, jsonify

conn = get_conn()
app = Flask(__name__)

@app.route('/', methods=['GET'])
def test():
    return "test"


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)