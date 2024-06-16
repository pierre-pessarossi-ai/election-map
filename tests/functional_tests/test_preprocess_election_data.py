# input a url to load raw data

import os

print(os.getcwd())

from election_map.src.preprocess_data import load_raw_data

raw_data = load_raw_data(
    "https://www.data.gouv.fr/fr/datasets/r/1996b2bc-e95a-4481-904f-28d16987fe61"
)

# save locally raw data

# get summary stats (first rows, col names, )

# load political party name mapping

# apply mapping to raw data of party name

# rearrange table in expected format

# save locally data
