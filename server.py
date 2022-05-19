from flask import Flask
from flask import request, jsonify
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def initApp():
        if request.method == 'GET':
            return "<p>Hello, World!</p>"
        else:
            res = {'message': 'test POST'}
            return jsonify(res)
if __name__ == '__main__':
    app.run()