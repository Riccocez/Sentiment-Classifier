#!/usr/bin/env python

import nltk
from random import shuffle
from petl import fromcsv, look, fieldnames, values, head, tail
import preprocessing

### Methods for preprocessing Raw Dataset

#Load a full file
def load_file(filename):
    
    file = open(filename)
    text = file.read()
    file.close()
    
    return text

#Print the content of filename
def print_file(filename):
    
    print filename
    
    return

#Get number of fields of the database
def split_fileline(line):
           
    line_splitted = line.split(',')
    no_fields = len(line_splitted)
    
    return no_fields, line_splitted


def really_read_filelines(filename, p_train_data, split_mode):
    
    #Load the table
    csvfile = fromcsv(filename)

    train_data, test_data = split_dataset(csvfile, p_train_data, split_mode)

    return train_data, test_data


#Split Dataset in training and testing data
def split_dataset(dataset, p_train_data, split_mode):

    fields = list(fieldnames(dataset))
    
    size_dataset = len(values(dataset, fields[0])) 
    size_train_data = int(round(size_dataset * p_train_data))
    size_test_data = abs(size_train_data - size_dataset)


    if split_mode == 'normal' :

        train_data = head(dataset, size_train_data - 1)
        
        if size_test_data == 0:
            
            test_data = []
            
        else:
            
            test_data = tail(dataset, size_test_data - 1)

    #################### Falta incluir Shuffle mode ###############

    return train_data, test_data



 
                
#Read and print each line of filename
def read_filelines(filename, p_train_data):
    
    no_lines = 0
    raw_dataset = []

    with open(filename,'r') as f:

        #Getting Header line
        header_line = f.readline()
        header_no_fields,header_splitted = split_fileline(header_line)
        
        #Getting each tweet
        next(f)        
        for line in f:
        
            no_fields,line_splitted = split_fileline(line)
            
            if no_fields == header_no_fields:
                
                raw_dataset.append(line_splitted)
                

    train_data, test_data = split_traintest_data(raw_dataset,p_train_data,'normal')

    return train_data, test_data


def split_traintest_data(dataset, p_train_data, split_mode):

    s_raw_dataset = len(dataset)
    size_train_data = int(round(s_raw_dataset * p_train_data))
    size_test_data = abs(size_train_data - s_raw_dataset)
    

    if split_mode == 'normal':
        
        train_data = dataset[0:size_train_data - 1]
        test_data = dataset[size_train_data:]
        
    elif split_mode == 'shuffle':

        shuffle(dataset)
        train_data = dataset[0:size_train_data - 1]
        test_data = dataset[size_train_data:]
    

    return train_data, test_data
    
    
        


    
