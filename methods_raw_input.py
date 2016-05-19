#!/usr/bin/env python

import nltk
from random import shuffle

### Methods

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

#Read and print each line of filename
def read_filelines(filename):
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
            no_lines += 1
            raw_dataset.append(line_splitted)
            print line_splitted, '\n'
                       
        print "Number of lines: " + str(no_lines)
        train_data, test_data = split_traintest_data(raw_dataset,0.3,'normal')
        
    return 
                

def split_traintest_data(dataset, test_size, split_mode):

    size_raw_dataset = len(dataset)
    size_test_data = int(round(size_raw_dataset * test_size))
    size_train_data = abs(size_raw_dataset - size_test_data)

    if split_mode == 'normal':
        
        train_data = dataset[0:size_train_data - 1]
        test_data = dataset[size_train_data:]
        
    elif split_mode == 'shuffle':

        shuffle(dataset)
        train_data = dataset[0:size_train_data - 1]
        test_data = dataset[size_train_data:]

    print "Entries for test data: ", size_test_data
    print "Training data: ", size_train_data
    print "Testing data: ", size_test_data
    print "Test Samples: ", test_data[0:2]
    

    return train_data, test_data
    
    
        


    
