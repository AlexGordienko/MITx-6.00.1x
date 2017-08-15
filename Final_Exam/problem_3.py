'''
!!!Problems 1 and 2 were MCQ!!!

Problem 3
10.0/10.0 points (graded)
Implement a function that meets the specifications below.

def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    # Your code here
For example, sum_digits("a;35d4") returns 12.
'''

def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    # Your code here
    nums = "0123456789"
    result = 0
    value = False
    for char in s:
        if char in nums:
            result += int(char)
            value = True
    if not value:
        raise ValueError()
    else:
        return result
