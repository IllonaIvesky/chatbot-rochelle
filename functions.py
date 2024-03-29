
"""A collection of functions from Assignment 3"""


import string
import random
import nltk
        
def is_question(input_string):
    
    """check if the user input is a string"""
    
    if '?' in input_string:
        output = True
        
    else:
        output = False
        
    return output 


def remove_punctuation(input_string):
    
    """remove any punctuation from the user input"""
    
    out_string = ""
    
    for item in input_string:
        
        if item not in string.punctuation: 
            out_string = out_string + item
            
    return out_string


def prepare_text(input_string):
    
    """transform every word in the input into lower case, remove any puncuation, and then split the input into a invidual     strings of word"""
    
    temp_string = input_string.lower()
    temp_string = remove_punctuation(temp_string) 
    out_list = temp_string.split()
    
    return out_list


def respond_echo(input_string,number_of_echoes,spacer):
    
    """returns a string that has been repeated a specified number of times, with a given separator. """
    
    if input_string is not None:
        echo_output = (input_string + spacer)*number_of_echoes
        
    else:
        echo_output = None
        
    return echo_output  


def selector(input_list,check_list,return_list):
    
    """randomly chooses an output from a set of possible outputs, based on the input it got. """
    
    output = None
    
    for element in input_list:
        
        if element in check_list:
            output = random.choice(return_list)
            break
            
    return output


def string_concatenator(string1,string2,separator):
    
    """concatenates two strings them with a separator in between. """
    
    output = string1 + separator + string2
    
    return output


def list_to_string(input_list,separator):
    
    """makes a list of strings into one single concatenated string."""
    
    output = input_list[0]
    
    for item in input_list[1:]:
        output = string_concatenator(output,item,separator)  
        
    return output 


def end_chat(input_list):
    
    """ends chat chatbot"""
    
    if 'quit' in input_list:
        return True
    
    else:
        return False
    
    
def is_in_list(list_one, list_two):
    
    """check if any item in one list is included in another"""
    
    for element in list_one:
        
        if element in list_two:
            return True
        
    return False


def find_in_list(list_one, list_two):
    
    """ find any item in one list that is included in another"""
    
    for element in list_one:
        
        if element in list_two:
            return element
        
    return None


def choose_language(input_lang):
    
    """based on the input choice, return the desired language"""
    
    if 'eng' in input_lang.lower():
        language = 'english_response'
        
    elif 'ger' in input_lang.lower():
        language = 'german_response'
        
    else: raise ValueError
    print('enter a valid language')
        
    return language
