import random

"""

    Pick a random word from the word list
    
    Ask player to enter a letter

    Everytime the player enters a letter that is in the word, reveal that letter

    Process continues until all letters are revealed or the player ran out of guesses

"""

wordsFile = open("Words.txt","r") #open the words file
lstWords = wordsFile.readlines() #create a list of words
wordsFile.close() #close the file
word = lstWords[random.randint(0,len(lstWords)-1)] #pick a random word
word = word[:-1] #remove the newline from the word

#create the hidden word string
displayWord = ""
for letter in word:
    displayWord+="_"

deadGuyPicture = ["\nO O","\n[.]","\n---","\n | ","\n | ","\n/"," \\"] #load each part of the death picture into the deadGuyPicture list
guessCount = 0

#Keep track of the letters the user already entered
usedLetters = []

#keep asking for input while the player has not uncovered the whole word and they have used less than 7 guesses
while displayWord != word and guessCount < 7:
    displayWordText = "Word: "

    #attach the hidden word string to the hidden word display 
    for letter in displayWord:
        displayWordText+=letter+" "

    #print the hidden word display
    print(displayWordText)

    #ask the user for a letter
    while True:
        letter = input("Enter letter: ").lower()
        if letter not in usedLetters:
            usedLetters.append(letter)
            break
        print('You arleady used that letter!')

    #if the letter is in word, edit the hidden word string to display the found letter
    if letter in word:
        for index in range(len(word)):
            if word[index]==letter:
                displayWord = displayWord[:index]+letter+displayWord[index+1:]
    else: #otherwise, increase the guesscount, and display guessCount (the amount of incorrect guesses the player used) parts of the death picture
        guessCount += 1
        for index in range(guessCount):
            print(deadGuyPicture[index],end="")
        print()

    print()

#if the guesscount is less than seven, say the player won, otherwise, say the player lossed
if guessCount < 7:
    print("You win! The word is {}. You guessed incorrectly {} {}.".format(displayWord,guessCount,'time'+('s','')[guessCount!=1]))
else:
    print("You lose! The word was "+word+".")
