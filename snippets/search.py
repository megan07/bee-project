from fuzzywuzzy import process

# read the us addresses file right away,
# so that we don't have to keep opening it and closing it
fp = open("data/us-addresses.tsv")

headers = fp.readline().strip().split("\t")
AVAILABLE_ADDRESSES = []

# we'll make a set of states we can use for parsing the
# address in the application
STATES = set()

for line in fp.readlines():
    pieces = line.strip().split("\t")
    loc = dict( zip(headers, pieces) )
    loc["orig"] = " ".join(pieces)

    AVAILABLE_ADDRESSES.append(loc)
    STATES.add(loc["state_abbrev"])

# filter locations will go through our available locations
# from the file we read in.  it will then filter out which
# locations the search is likely looking for based on state
# and zip code.  we could potentially narrow down even more
# but for now this helps a lot
def filter_locations(search_term):
    locations = []
    for addr in AVAILABLE_ADDRESSES:

        # try and narrow down the locations some
        search_state = search_term.get("state", None)
        search_zip = search_term.get("zip", None)

        if len(search_zip) > 0:
            if addr["zip"] in search_zip:
                locations.append(addr["orig"])
        elif len(search_state) > 0:       
            if addr["state_abbrev"] in search_state:
                locations.append(addr["orig"])
        else:
            locations.append(addr["orig"])

    fp.close()

    # if the geo address we got earlier has enough information, lets use that one
    if search_term.get("geo", "") >= search_term["original"]:
        filtered =  process.extract(search_term["geo"], locations)
    else:
        filtered =  process.extract(search_term["original"], locations)

    # only return options that are more likely matches (80 or better)
    return ([options[0] for options in filtered if options[1] > 80])
