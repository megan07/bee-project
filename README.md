# bee-project
Backend Engineer Project

Ideally, this should take three hours.

## Scenario
Real estate data has a tendency to be very messy. In this project, we will ask you to take an incoming address and determine if it does or does not "approximately match" the result in the data set. The reason I use "approximate match", and the reason that the problem of finding matching addresses is difficult, is because a person who searches for the address `1 2 Avenue, Mason City IA` is probably looking for the same address as the person searching for `1 2nd Ave, Mason City` or the person searching for a house on `Anadale Street` and the person searching for a house on `Annadale Lane` may be looking for the same thing.

Since we deal primarily with address strings that have misspellings, strange abbreviations, or missing pieces, and since there is no way to "regex" our way through this, finding "approximate matches" is one of the things we do on a regular basis.

## Goals: Matching Queries in the Address Set
This task asks you to build a flask end-point that receives an unformatted address as a character string, searches the `us-addresses` data set for an approximate match, and, if such a match is found, returns the formatted address as a dictionary. 

Note: this is *not* a text cleaning exercise. The goal is not to convert "St." to "street" but instead to work within the messiness. Below are some possible approaches that follow the spirit this problem was designed to represent.

### Possible Approaches

Here are two possible ways to find "approximate matches" that we feel can be quickly implemented and don't require any special understanding that can't be pulled off of Stack Exchange, Wikipedia, or other sites. You are more than welcome to come up with your own, but we aren't looking for that.

#### Scoring algorithms to find best matches
There are many methods for measuring the distance between two strings. For instance, [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance) [(code)](https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Levenshtein_distance#Java) calculates the minimum number of single-character edits required to convert one string to another. This (or one of many other possible ways of describing the distance between two strings) could be used to compare either the incoming string to address strings from the loosely formatted address data set or you could attempt to do some parsing on the incoming string to compare it to the individual elements of the loosely formatted data set. The element with the highest score would be the best match. A well chosen cut-off for how high the score should be in order to report a match should be selected (for instance, if you store your scores in `match_score` you may choose to report a match only if `max(match_scores) > min_cutoff` where `min_cutoff` would be some value you choose based on the performance you see.

#### Fuzzy Matching
Fuzzy matching is a technique used to match elements in cases where a 100% match is not required. Python has a good fuzzy matching library 

## Resources
In this repository you will find a folder called data that contains a tab-delimited file, `us-addresses.tsv`. This file contains 50,000 addresses from around the United States. It is in the format used by one of our data sources. If you look over the data set, you may notice that some fields are only loosely standardized. For instance, sometimes `street_type` is reported as `Street` and other times it is reported as `St.`. You are also being provided with some code snippets which may or may not accomplish some of the parts for you. 
