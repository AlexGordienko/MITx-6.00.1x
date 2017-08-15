#Problem 3
#15.0/15.0 points (graded)

#Assume s is a string of lower case characters.
#Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print
#Longest substring in alphabetical order is: beggh
#In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
#Longest substring in alphabetical order is: abc
#Note: This problem may be challenging. We encourage you to work smart. If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course. If you have time, come back to this problem after you've had a break and cleared your head.

s = 'abcbcd'

counter = 1
longest = 1
fin_str = s[0]
for c in range(0 , len(s)-1):
    if (s[c].lower() <= s[c + 1].lower()):
        counter += 1
        if counter > longest:
            longest = counter
            fin_str=s[c-longest+2:c+2]
    else:
        counter = 1
print('Longest substring in alphabetical order is: ', fin_str)
