# The 6.00 Word Game

import random
import string
from tkinter import *

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
score = 0
hand = {}

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    count = 0
    #itterate over the letters of the word and adding to count the corresponding value
    for letter in word:
        count += SCRABBLE_LETTER_VALUES[letter]
    count = count*len(word)
    if len(word) == n:
        count += 50
    return count



#
# Problem #2: Make sure you understand how this function works and what it does!
#
def displayHand():
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    global hand
    element = ''
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")       # print all on the same line
             # Creating a Label Widget
             element = element + letter + " "
             
    print()                             # print an empty line
    return element

#
# Problem #2: Make sure you understand how this function works and what it does!
#
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    global hand
    numVowels = n // 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def updateHand(word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    global hand
    for letter in word:
        if letter in hand:
            hand[letter] -= 1

#
# Problem #3: Test word validity
#


def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    guess_dict = {}
    if word not in wordList:
        return False
    else:
        guess_dict = getFrequencyDict(word)
        for letter in word:
            if letter not in hand:
                return False
            elif hand[letter] < guess_dict.get(letter,0): 
                return False
    return True



#
# Problem #4: Playing a hand
#

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    count = 0
    for k in hand:
        count += hand[k]
    return count

def getword(e, wordList, n):
    word = e.get()
    print(word)
    global hand
    global score
#    if word == '.' : # If the input is a single period
#        flag = True
#    else: # Otherwise (the input is not a single period)
    if not isValidWord(word, hand, wordList): # If the word is not valid:
        print("Invalid word, please try again.")# Reject invalid word (print a message followed by a blank line)
    else: # Otherwise (the word is valid):
        score += getWordScore(word, n)
        # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
        print('''"''' + str(word) + '''"''' + " earned "+ str(getWordScore(word,n)) + " points. Total: " + str(score) + " points")
        # Update the hand 
        updateHand(word)

def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Keep track of the total score
    Playu = Toplevel()

#    while not all(value == 0 for value in hand.values()):# As long as there are still letters left in the hand
    print("Current Hand:  ", end = '')# Display the hand
    # Creating a Label Widget
    CurrentHand = Label(Playu, text="Current Hand:  ")
    # Shoving it onto the screen
    CurrentHand.pack()   
    DisplayHand = Label(Playu, text=displayHand())
    # Shoving it onto the screen
    DisplayHand.pack()
    e = Entry(Playu, width=30)
    e.pack()
    button_ok = Button(Playu, text = "OK", command = lambda: getword(e, wordList, n)) 
    print(hand)
    button_ok.pack()
    Playu.mainloop()


    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
#    if flag:
#        print("Goodbye! Total score: " + str(score) + " points. ")
#    else:
#        print("Run out of letters. Total score: " + str(score) + " points. ")


