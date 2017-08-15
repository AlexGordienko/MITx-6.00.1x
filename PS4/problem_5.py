'''Problem 5 - Playing a Hand
10.0/10.0 points (graded)
In ps4a.py, note that in the function playHand, there is a bunch of pseudocode. This pseudocode is provided to help guide you in writing your function. Check out the Why Pseudocode? resource to learn more about the What and Why of Pseudocode before you start coding your solution.

Note: Do not assume that there will always be 7 letters in a hand! The parameter n represents the size of the hand.

Testing: Before testing your code in the answer box, try out your implementation as if you were playing the game. Here is some example output of playHand:
'''

def playHand(hand, wordList, n):
    score = 0
    while(True):
        print("Current Hand: ", end=" ")
        displayHand(hand)
        word = input('Enter word, or a "." to indicate that you are finished: ')
        if word == ".":
            print("Goodbye! ", end=" ")
            break
        else:
            if not isValidWord(word, hand, wordList):
                print("Invalid word, please try again.")
                print("")
            else:
                score += getWordScore(word, n)
                print('"' + word + '"' + " earned " + str(getWordScore(word, n)) + " points. Total: " + str(score) + " points.")
                print()
                hand = updateHand(hand, word)
            if all(value == 0 for value in hand.values()):
                print("Run out of letters. ", end="")
                break
    print("Total score: " + str(score) + " points.")



