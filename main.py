from flask import Flask
from flask.json import jsonify
from flask import request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    current_time = datetime.now().strftime("%H:%M:%S")
    name = request.args.get('name', 'No name')
    return jsonify({
        "name": name,
        "current_time": current_time
    })

if __name__ == "__main__":
    app.run(port=8000, host="0.0.0.0")
