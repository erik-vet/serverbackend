# pip install flask
# pip install flask-cors
from flask import Flask
from flask_cors import CORS

import erik
import felix
import dominique

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

@app.route("/dominique")
def methodedominique():
    return dominique.open_youtube_link('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

@app.route("/erik1/<eenword>/<tweeword>")
def methodeerik(eenword, tweeword):
  return erik.methodeerik(eenword, tweeword)