#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

def print_words(filename):

    #creat a dict call words dict to store words(keys) and int(values)
    wordsDict = readin_file(filename)

    #Sort the dict by its keys and print
    for key in sorted(wordsDict.keys()):
        print key, wordsDict[key]

 
    
def print_top(filename):
    
    #creat a dict call words dict to store words(keys) and int(values)
    wordsDict = readin_file(filename)    
    
    #orrigonal Solution
    #count = 0
    ##Sort the dict by its values and print
    #for key, value in sorted(wordsDict.iteritems(), key=lambda (k,v): (v,k),reverse=True):
        #if count < 20:
            #print "%s: %s" % (key, value)
            #count += 1

    #another option to make loop neater 
    items = sorted(wordsDict.items(), key=lambda (k,v): (v,k), reverse=True)

    # Print the first 20
    for item in items[:20]:
        print item[0], item[1]
###

def readin_file(filename):
    #creat a dict call words dict to store words(keys) and int(values)
    wordsDict = {}
    
    #open file
    f = open(filename, 'r')
        
    #iterate through file line by line    
    for line in f:
        #create list called words
        words = []
        #convert line to lowercase break on space add to words
        words = line.lower().split()
            
        #for every word in my list words
        for word in words:
            #if the word is in wordsDict
            if wordsDict.has_key(word):
                #increment it
                wordsDict[word] += 1
            #otherwise    
            else:
                #add it and set value to 1
                wordsDict[word] = 1
    
    f.close()
    
    return wordsDict


# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
    if len(sys.argv) != 3:
        print 'usage: ./wordcount.py {--count | --topcount} file'
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
  
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print 'unknown option: ' + option
        sys.exit(1)

if __name__ == '__main__':
    main()