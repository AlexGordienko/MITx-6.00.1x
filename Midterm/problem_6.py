'''
Problem 6
15.0/15.0 points (graded)
Write a function that satisfies the following docstring:

def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number
        of times in L. If no such element exists, returns None """
    # Your code here
For example, if

largest_odd_times([2,2,4,4]) returns None
largest_odd_times([3,9,5,3,5,3]) returns 9
Paste your entire function, including the definition, in the box below. Do not leave any debugging print statements.
'''

def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number
        of times in L. If no such element exists, returns None """
    # Your code here
    SecondNumOfOccurence = 0

    for x in L:
        largestNum = max(L)

        if len(L)>2:
            SecondLargest = max(n for n in L if n!=max(L))
            SecondNumOfOccurence = L.count(SecondLargest)
        NumOfOccurence = L.count(largestNum)
        if NumOfOccurence%2 != 0:
            return largestNum
        elif (SecondNumOfOccurence%2 != 0) and (len(L)>2):
            return SecondLargest
        else:
            return None



