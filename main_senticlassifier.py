#!/usr/bin/env python


import methods_raw_input
import preprocessing


# Main code for sentiment classifier

#Setting Parameters
data_filename = "Tweets.csv"
p_train_data = 0.7
split_mode = 'normal'



train_data, test_data = methods_raw_input.really_read_filelines(data_filename, p_train_data, split_mode)

preprocessing.tokenise_data(train_data)




