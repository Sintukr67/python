import random

def choose():
    words = ['rainbow', 'computer', 'science', 'programming', 'mathematics', 'player', 'condition', 'reverse', 'water', 'board']
    pick = random.choice(words)
    return pick

def jumble(word):
    jumbled = "".join(random.sample(word, len(word)))
    return jumbled

def thank(pl1, pl2, pp1, pp2):
    print(pl1, 'your score is:', pp1)
    print(pl2, 'your score is:', pp2)
    print('Thanks for playing!')
    print('Have a nice day!')

def play():
    pl1 = input('Enter Player 1 name: ')
    pl2 = input('Enter Player 2 name: ')
    pp1 = 0
    pp2 = 0
    turn = 0

    while True:
        picked_word = choose()
        qn = jumble(picked_word)
        print("\nJumbled word is:", qn)

        if turn % 2 == 0:
            print(pl1, 'your turn')
            ans = input('What is your answer? ')
            if ans == picked_word:
                pp1 += 1
                print('Correct! Your score is:', pp1)
            else:
                print('Better luck next time! The word was:', picked_word)
        else:
            print(pl2, 'your turn')
            ans = input('What is your answer? ')
            if ans == picked_word:
                pp2 += 1
                print('Correct! Your score is:', pp2)
            else:
                print('Better luck next time! The word was:', picked_word)

        c = input('Press 1 to continue or 0 to quit: ')
        if c == '0':
            thank(pl1, pl2, pp1, pp2)
            break

        turn += 1

# Start the game
play()
