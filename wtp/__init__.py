import time
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

LIMIT = 10

@app.route("/petitions/")
def browse():
    page = (request.args.get('p') or '1')
    try:
        page = int(page)
    except:
        page = 1

    offset = (page - 1) * LIMIT 

    args = { 'limit' : LIMIT, 'offset' : offset}
    url = "https://api.whitehouse.gov/v1/petitions.json?limit=%(limit)s&offset=%(offset)s" % args

    contents = requests.get(url).json()
    results = contents['results']

    return render_template("browse.html", results = results, page = page)

