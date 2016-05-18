#!/usr/bin/env python


import methods_raw_input



#--------------------------------------

# Interaction with user

action = raw_input ("Introduce name of Raw Database  ")

text = methods_raw_input.load_file(action.lower())

methods_raw_input.print_file(text)
