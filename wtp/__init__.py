import time
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/petitions/")
def browse():
    args = { 'limit' : 10 }
    url = "https://api.whitehouse.gov/v1/petitions.json?limit=%(limit)s" % args

    if request.args.get('before'):
        url += '?createdBefore=%s' % int(request.args.get('before'))

    if request.args.get('after'):
        url += '?createdAfter=%s' % int(request.args.get('after'))

    print url

    contents = requests.get(url).json()
    results = contents['results']
    created = [ result['created'] for result in results ]
    oldest_new = min(created)
    newest_new = max(created)
    return render_template("browse.html", results = results, before = oldest_new, after = newest_new)

