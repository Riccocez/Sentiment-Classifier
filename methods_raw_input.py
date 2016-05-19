#!/usr/bin/env python

import nltk

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

    with open(filename,'r') as f:

        #Getting Header line
        header_line = f.readline()
        header_no_fields,header_splitted = split_fileline(header_line)
        
        #Getting each tweet
        next(f)
        for line in f:
        
            no_fields,line_splitted = split_fileline(line)
            no_lines += 1
            print line_splitted, '\n'
                       
        print "Number of lines: " + str(no_lines)
        
    return
                




    
