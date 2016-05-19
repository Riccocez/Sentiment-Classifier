#!/usr/bin/env python


import methods_raw_input


# Main code for sentiment classifier

#action = raw_input ("Introduce name of Raw Database  ")
action = "Tweets.csv"

#text = methods_raw_input.load_file(action)

methods_raw_input.read_filelines(action)
#methods_raw_input.split_fileline_0(action)
