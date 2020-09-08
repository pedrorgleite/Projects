from tkinter import *
from Scrabble_GUI import *

root = Tk()
def DealNewHand():
    Button_repeat = Button(root, text = "Replay the last hand", command=ReplayGame )
    Button_repeat.pack()
    Play = Toplevel()
    hand = dealHand(HAND_SIZE)
    hand_copy = hand.copy() 
    Button_play = Button(Play, text="Play against the Computer", command=lambda: compPlayHand(hand,wordList, HAND_SIZE))
    Button_play.pack()  
    Button_uplay = Button(Play, text="Play against Yourself", command=lambda: playHand(hand,wordList, HAND_SIZE))
    Button_uplay.pack()  

def ReplayGame():
    pass

wordList = loadWords()
Button_exit = Button(root, text="Exit", command=root.quit)
Button_exit.pack()
Button_Deal = Button(root, text="Deal a new hand", command=DealNewHand)
Button_Deal.pack()
print(hand)

root.mainloop()