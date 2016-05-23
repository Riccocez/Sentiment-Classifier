#!/usr/bin/env python

#Text Preprocessing Module
from petl import values, fieldnames, look, addcolumn

import nltk
#from nltk.tokenize import TweetTokenizer

def tokenise_data(dataset):

    tweets_tokenized = []
    # Text of tweet is on field 10
    tweets = extract_values(dataset, 10)

    for tweet in tweets:
        t_tokenised = nltk.word_tokenize(tweet)
        tweets_tokenized.append(t_tokenised)

    token_dataset = add_columns(dataset, 'tweet_tokenized', tweets_tokenized)
    return token_dataset

def word_frequency(dataset,text_field):

    tweets = extract_values(dataset,text_field)

    bag_words = {}
    word_frequency = []

    for tweet in tweets:
        for word in tweet:
            if word in bag_words:
                bag_words[word] += 1
            else:
                bag_words[word] = 1
        word_frequency.append(bag_words)
        bag_words = {}
        
        
    wfreq_dataset = add_columns(dataset, 'word_frequency', word_frequency)

    return wfreq_dataset
           
       
        

def add_columns(dataset, column_name, column_data):

    new_dataset = addcolumn(dataset, column_name, column_data)

    return new_dataset


def extract_values(dataset, field_position):

    fields = list(fieldnames(dataset))
    field_values = values(dataset, field_position)
    
    return field_values
