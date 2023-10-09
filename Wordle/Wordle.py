import random

#-----------------------------------------
# File Importing for First Time Word Bank
#-----------------------------------------

with open('/Users/devpatel/Desktop/Personal Codes/Wordle Project/10000_words.txt', 'r') as file:
    lines = file.readlines()
    
word_list = [line.strip() for line in lines]

wordle5 = []

for word in word_list:
    if len(word) == 5 and word.isalpha():
        wordle5.append(word)
        
#-----------------------------------------

wordleAnswer = random.choice(wordle5)

#print(wordleAnswer)

#-----------------------------------------
    
with open('five_letter_words.txt', 'w') as output_file:
    for word in wordle5:
        output_file.write(word + '\n')

#-----------------------------------------

def createBoard(gameBoard):
    print()
    for row in gameBoard:
        print(' '.join(row))
    print()
    print('-' * 10)


def updateBoard(gameBoard, guess, wordleAnswer, chance):
    
    guess = list(guess)
    
    for i in range(5):
       
        if guess[i] == wordleAnswer[i]:
            gameBoard[chance][i] = wordleAnswer[i]
        
        elif guess[i] in wordleAnswer:
            gameBoard[chance][i] = '!'
        
        elif guess[i] not in wordleAnswer:
            gameBoard[chance][i] == 'X'
                

    createBoard(gameBoard)
    
    
def main():
    
    notFound = True
    chance = 0
    
    gameBoard = [
    ['?', '?', '?', '?', '?'],
    ['?', '?', '?', '?', '?'],
    ['?', '?', '?', '?', '?'],
    ['?', '?', '?', '?', '?'],
    ['?', '?', '?', '?', '?'],
    
    ]

    list(wordleAnswer)
    
    print('')
    print('Welcome to Python Wordle!')
    print('')
    init= int(input('Would you like to play? (0 = No thanks!), (1 = Yes!): '))
    
    if init == 1:
        print('')
        createBoard(gameBoard)
       
        print(str(wordleAnswer)) #FOR TEST PURPOSES ONLY. COMMENT OUT WHEN ACTUALLY PLAYING!
        
    
        while notFound:
            
            
            if chance < 5:
                
                guess = input('Enter guess: ')
                
                if len(guess) == 5:
                    
                    updateBoard(gameBoard, guess, wordleAnswer, chance)
                    chance += 1
                    
                else:
                    print('Make sure to enter a word that is 5 characters long!')
                    
                if str(guess) == str(wordleAnswer):
                    notFound = False
            
        
            if chance == 5:
                break
                
    
            
        if notFound == True:
            print('You\'ve ran out of guesses! The correct guess was: ', wordleAnswer)
        
        if notFound == False:
            print('You\'ve got it!')
    else:
        print('')
        print('Have a good day!')
    
    
if __name__ == '__main__':
    main()

