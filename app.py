# pip install flask
# pip install flask-cors
from flask import Flask
from flask_cors import CORS

import felix

app = Flask(__name__)
CORS(app)

@app.route("/")
def helloWorld():
  return "Hello, cross-origin-world!"

@app.route("/felix")
def methodefelix():
  return felix.methodevanfelix()

@app.route("/felix2")
def methodefelix2():
  return felix.tweedemethodevanfelix()

@app.route("/felix3/<variabele1>")
def methodefelix3(variabele1):
  return felix.derdemethodevanfelix(variabele1)