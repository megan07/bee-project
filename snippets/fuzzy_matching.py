#!/usr/bin/env python

"""
Provides example code snippets for fuzzy matching using Levenshtein Distance.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from fuzzywuzzy import process


if __name__ == '__main__':
    print(process.extract("main st", ["ballard st", "main street", "howard drive"]))
