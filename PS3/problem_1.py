#Problem 1 - Is the Word Guessed
#10.0/10.0 points (graded)
#Please read the Hangman Introduction before starting this problem. We'll start by writing 3 simple functions that will help us easily code the Hangman problem. First, implement the function isWordGuessed that takes in two parameters - a string, secretWord, and a list of letters, lettersGuessed. This function returns a boolean - True if secretWord has been guessed (ie, all the letters of secretWord are in lettersGuessed) and False otherwise.

#Example Usage:

#>>> secretWord = 'apple'
#>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#>>> print(isWordGuessed(secretWord, lettersGuessed))
#False
#For this function, you may assume that all the letters in secretWord and lettersGuessed are lowercase.

secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

def isWordGuessed(secretWord, lettersGuessed):
    counter = 0
    checker = False
    for char in secretWord:
        for i in lettersGuessed:
            if char == i:
                counter += 1
            if counter == len(secretWord):
                checker = True
    return checker

print(isWordGuessed(secretWord, lettersGuessed))

