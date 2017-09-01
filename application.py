import re

from snippets import geocode
from snippets import search

from flask import render_template
from flask import request
from flask import Flask
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search_addresses():
    # save the original address
    address = {
                "original": request.form["my_address"],
                "state": [],
                "zip": [],
              }

    # addresses are typically typed in a similar order
    # there could potentially be more string parsing here
    # for street name etc, but i think it's common for people
    # to search by city, state at the very least
    # state should filter it enough, but there could definitely be more
    pieces = request.form["my_address"].split()
    if len(pieces) > 1:
        # the zip code is typically last
        if re.match("\d{5}", pieces[-1]):
            address["zip"] = [pieces[-1]]

        # or they may have skipped the zip and just ended with a state
        elif pieces[-1] in search.STATES:
            address["state"] = [pieces[-1]]

    # see how much we can narrow down with the geo code
    address_options = geocode.call_api( address=address["original"] )
    for geo_addr in address_options:
        state = ""
        zip_code = ""

        for t in geo_addr["address_components"]:
            if "postal_code" in t["types"]:
                address["zip"].append( t["short_name"] )
                zip_code = t["short_name"]
            
            if "administrative_area_level_1" in t["types"]:
                address["state"].append( t["short_name"] )
                state = t["short_name"]

            # this should correct any address errors, hopefully
            if "route" in t["types"]:
                address["geo"] = " ".join( [t["long_name"], state, zip_code] )

    # print out a template that lists the addresses that matched
    return render_template("found.html", addresses=search.filter_locations(address))


if __name__ == '__main__':
    app.run()