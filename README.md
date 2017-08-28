# Backend Engineer Project

If you have any questions about these instructions, don't hesitate to [submit an issue on GitHub](https://github.com/structurely/bee-project/issues/new) - that is the fastest way to get a response from the appropriate person.

## Scenario
Real estate data has a tendency to be very messy. In this project, we will ask you to take an incoming address and determine if it does or does not "approximately match" an item in an existing data set. The reason I use "approximate match", and the reason that the problem of finding matching addresses is difficult, is because a person who searches for the address `1 2 Avenue, Mason City IA` is probably looking for the same address as the person searching for `1 2nd Ave, Mason City` or the person searching for a house on `Anadale Street` and the person searching for a house on `Annadale Lane` may be looking for the same thing.

Since we frequently deal with address strings that have misspellings, strange abbreviations, or missing pieces, and since there is no way to "regex" our way through this, finding "approximate matches" is one of the things we do on a regular basis.

## Task: Approximate Matching for Addresses
In this repository you will find a folder called `data/` that contains a tab-delimited file, `us-addresses.tsv`. This file contains 50,000 addresses from around the United States. It is in the format used by one of our data sources. 

This task asks you to build a flask end-point that receives an unformatted address as a character string, searches the `us-addresses` data set for an approximate match, and, if such a match is found, returns the matching address from the data set as a dictionary. 

Note: this is *not* a text cleaning exercise. The goal is not to convert "St." to "street" but instead to work within "the spirit of messiness". Below are some possible approaches that follow the spirit this problem was designed to present.

### Possible Approaches
Here are some possible ways steps you may find useful as you attempt to find "approximate matches" that we feel can be quickly implemented and don't require any special understanding that can't be pulled off of Stack Exchange, Wikipedia, or other sites. You are more than welcome to come up with your own, but we aren't looking for that.

#### Geocoding
The incoming string can be edited, chopped, etc. You may find that sending the incoming string through Google's Geocoding API could help to clean up and standardize your inputs.

#### Fuzzy matching
Fuzzy matching is a technique that compares different strings in order to find matches in cases where a 100% match is not required. 
There are many methods for measuring how "different" two strings are. For instance, [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance) [(code)](https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Levenshtein_distance) calculates the minimum number of single-character edits required to convert one string to another. This (or one of many other possible ways of describing the distance between two strings) could be used to compare the incoming address to the addresses in the data set. Notice that all the fields may not equally important when searching for matches - for instance the strings `12th street` and `15th street` may be closer together than the strings `15th St` and `15th street`. You may be able to do better by parsing before you make comparisons. In particular, we could improve our match accuracy by using a tool like the Geocoding API in order to perform fuzzy matching on the components of the addresses (street name, street number, and so on) instead of the entire strings.

You can find some useful code for geocoding and fuzzy matching in the `snippets/` directory.

## Resources
- The set of addresses to be searched through for matches is stored in `data/`.
- The code in `snippets/` may be of use in your project. Feel free to edit/incorporate them.

## What we are looking for
Ideally, this should take three hours.
- This project should demonstrate a proficiency in python. 
- The result should include a python file called `application.py` which when ran from the command line as `python application.py` starts a http server running flask. 
- There should be a usage on multiple methods and modules to reuse code and to provide structure to the program. 
- All python requirements should be committed to the repo so that a program like pip could be used to install all necessary modules in the environment. 
- Use of built in and popular python libraries is encouraged.
- Efficiency of the program should be a concern. Include comments about how one could optimize the program further or how it is being optimized already. Optimizations could mean things like sorting a list to search through it faster and not making requests to resources more than necessary.
