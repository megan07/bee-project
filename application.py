from flask import render_template
from flask import request
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search_addresses():
    fp = open("data/us-addresses.tsv")

    headers = fp.readline().strip().split("\t")

    locations = []
    for line in fp.readlines():

        loc = dict( zip(headers, line.strip().split("\t")) )
        locations.append(loc)

    fp.close()

    return request.form["my_address"]


if __name__ == '__main__':
    app.run()