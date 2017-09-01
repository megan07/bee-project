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
                "zip": []
              }

    # addresses are typically typed in a similar order
    pieces = request.form["my_address"].split()
    if len(pieces) > 1:
        # the zip code is typically last
        if re.match("\d{5}", pieces[-1]):
            address["zip"] = [pieces[-1]]

        # or they may have skipped the zip and just ended with a state
        elif re.match("\w{2}", pieces[-1]):
            address["state"] = [pieces[-1]]

    if "state" not in address or "zip" not in address:
        # if state or zip weren't provided before, we'll see if we can find it with geocode
        address_options = geocode.call_api( address=request.form["my_address"] )
        for geo_addr in address_options:
            for t in gedo_addr["address_components"]:
                if "administrative_area_level_1" in t["types"]:
                    address["state"].append( t["types"]["short_name"] )
                elif "postal_code" in t["types"]:
                    address["zip"].append( t["types"]["short_name"] )

    print (address, "\n\n")

    print (search.filter_locations(address))

    return request.form["my_address"]


if __name__ == '__main__':
    app.run()