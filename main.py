'''
    Blueprint:

    Pick a random word from the word list
    Ask the player to enter a letter
    Everytime the player enters a letter that is in the word, reveal that letter
    If the letter is not in the word, subtract 1 from the guess count
    Process continues until all letters are revealed or the player runs out of guesses

'''

import random #import random functionality
wordsFile = open('Words.txt','r') #open the words file
lstWords = wordsFile.readlines() #create a list of words
wordsFile.close() #close the file
validLetters = list('abcdefghijklmnopqrstuvwxyz')
deadGuyPicture = ['\nO O','\n[.]','\n---','\n | ','\n | ','\n/',' \\'] #create death picture into the deadGuyPicture list

#run the game indefinitely until the user does not want to play again
#while True: 

while True:

    word = lstWords[random.randint(0,len(lstWords)-1)] #pick a random word
    word = word[:-1] #remove the newline from the word

    #create the hidden word string
    displayWord = '_'*len(word)

    guessCount = 0

    #keep track of the letters the user already entered
    usedLetters = []

    #keep asking for input while the player has not uncovered the whole word and they have used less than 7 guesses
    while displayWord != word and guessCount < 7:

        print('Word: ',end='')

        #print the display word with spaces in between the characters 
        for letter in displayWord:
            print(letter+' ',end='')
        
        print()

        #ask the user for a letter
        while True:
            letter = input('Enter letter: ').lower()

            if letter in validLetters:
                if letter not in usedLetters:
                    usedLetters.append(letter)
                    break
                print('You arleady used that letter!\n')
            else:
                print('Not a valid letter\n')

        

        #if the letter is in word, edit the hidden word string to display the found letter
        if letter in word:
            for index in range(len(word)):
                if word[index]==letter:
                    displayWord = displayWord[:index]+letter+displayWord[index+1:]
        else: #otherwise, increase the guesscount, and display guessCount parts of the death picture
            guessCount += 1
            for index in range(guessCount):
                print(deadGuyPicture[index],end='')
            print()

        print()
            


    #if the guesscount is less than seven, say the player won, otherwise, say the player lossed
    if guessCount < 7:
        print('You win! The word is {}. You guessed incorrectly {} {}.'.format(word,guessCount,'time'+('','s')[guessCount!=1]))
    else:
        print('You lose! The word was '+word+'.')

    if input('Do you want to play again? Enter "no" to end, otherwise play again! ').lower()=='no':
        break
    print()
