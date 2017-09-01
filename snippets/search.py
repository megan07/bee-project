from fuzzywuzzy import process

def filter_locations(search_term):
    fp = open("data/us-addresses.tsv")

    headers = fp.readline().strip().split("\t")

    locations = []
    for line in fp.readlines():

        loc = dict( zip(headers, line.strip().split("\t")) )

        # try and narrow down the locations some
        search_state = search_term.get("state", None)
        search_zip = search_term.get("zip", None)

        if len(search_state) > 0 or len(search_zip) > 0:
            if loc["zip"] in search_zip:
                locations.append(loc)
            elif loc["state_abbrev"] in search_state:
                locations.append(loc)
        else:
            locations.append(loc)

    fp.close()

    print ("Locations length: ", len(locations))
    print (process.extract(search_term["original"], locations))