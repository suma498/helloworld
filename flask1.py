from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({"about":'Hello World from Python Flask!'})

app.run(debug=True) 
