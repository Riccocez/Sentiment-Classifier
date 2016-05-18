#!/usr/bin/env python

### Methods


def load_file(filename):
    file = open(filename)
    text = file.read()
    file.close()
    return text

def print_file(filename):
    print filename
    return
