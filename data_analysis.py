"""
Script for analysing the data from the inauguration speeches
such as:
- most common words
- use of words over time
-
"""

import pandas as pd
import fetch_data

sample_text = fetch_data.get_text()

print (len(sample_text))


def lexical_diversity(text):
    return len(set(text))/len(text)

# def percentage(count,total):
#     return 100 * count/total

print (lexical_diversity(sample_text))
