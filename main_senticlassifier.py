#!/usr/bin/env python


import methods_raw_input
import preprocessing
from petl import tocsv


# Main code for sentiment classifier

#Setting Parameters
data_filename = "Tweets.csv"
p_train_data = 0.7
split_mode = 'normal'



train_data, test_data = methods_raw_input.really_read_filelines(data_filename, p_train_data, split_mode)

train_data = preprocessing.tokenise_data(train_data)

train_data = preprocessing.word_frequency(train_data, 'tweet_tokenized')


tocsv(train_data,'New_table.csv')
