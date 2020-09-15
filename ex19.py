#In this example, we will be practicing how to import the file in python
#and pulling the functions from this script to run in another.

#in other words, creating a library

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sort the words."""
    return sorted(words)
    
def printfirstword(words):
    """Print the first word after popping it off."""
    words = words.pop(0)
    print(words)

def printlastword(words):
    """Print the last word after popping it off."""
    words = words.pop(-1)
    print(words)
    
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints first and last word in sentence"""
    words = break_words(sentence)
    printfirstword(words)
    printlastword(words)
    
def print_first_and_last_sorted(sentence):
    """Print first and last in a sorted sentence"""
    words = sort_sentence(sentence)
    printfirstword(words)
    printlastword(words)
