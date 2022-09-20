from random import *
from time import sleep


def main():
    play = 'yes'
    start()
    while play == 'yes':
        alive = 'yes'
        count = 0
        money = 0

        while alive == 'yes':
            alive = game(count)
            if alive == 'yes' and count == 0:
                count += 1
                money = 100
                print('You won $' + str(money) + ' that round.')
                print('Total winnings: $' + str(money))
                alive = input('Test your luck again or quit? [yes/quit]: ').lower()
                print('\n\n')
                ()


            elif alive == 'yes' and count > 0:
                print('You won $' + str(money) + ' that round.')
                money *= 2
                print('Total winnings: $' + str(money))
                alive = input('Test your luck again or quit? [yes/quit]: ').lower()
                print('\n\n')
                ()

        if alive == 'no':
            dead(money)
            money = 0
        else:
            win(money)
        highScore(money)
        play = input('\nPlay again? [yes/no]: ').lower()
        print('\n\n')


def start():
    print('Welcome to Alex\'s game of Russian Roulette!')
    print('In this game, you will earn money for every time you pull the trigger and survive.')
    input('You will earn $100 on your first shot and your total winnings will double each round. (Press enter)')
    print('\nYou have the choice to quit at any time, take your winnings, and get the heck out.')
    print('Though if you get the wrong end of the revolver barell hole thingy, you die and win nothing \
          \nmore than your premature death.')
    print('Alrighty then! Let\'s get spinning!')
    input('Ready??? (Press enter)')
    print('\n\n')


def game(count):
    print('Spinning...')
    barrel = randint(1, 6)
    sleep(1)
    if barrel == 6:
        return 'no'
    elif barrel != 6:
        if count < 1:
            print('\nClick Click')
            sleep(0.5)
            print('\nYou got lucky this time')
            return 'yes'
        else:
            print('\nClick Click')
            sleep(0.5)
            print('\nYou got lucky AGAIN!')
            return 'yes'
    sleep(1)


def win(money):
    print('Congrats on only being kinda stupid... You\'re still alive somehow.')
    print('You are walking away with $' + str(money))
    print('Now get out of here before I shoot you myself (:')
    #sleep(1.5)


def dead(money):
    print('\n\nBANG BANG \n')
    sleep(1)
    note = ['Boom Shakalocka, you dead son!', 'BANG BOOM BAM you is dead HOE!', 'Oooff brains EVERYWHERE! You dead.',
            'Someone call yo momma cause you not alive no mo!', 'Haha you died lol.', 'You probably should\'ve \
stopped while you were ahead cause now you dead!', 'You dead dead now BOY!', 'You\'re dead you greedy bastard haha.', \
            'BOOOOOMMM ! You dead and I don\'t even feel bad for you.']
    deathNote = randrange(len(note))
    print(note[deathNote])
    sleep(0.5)
    print('You could have won $' + str(money) + ' tsk tsk... Better luck next time!')


def highScore(money):
    score = open('rouletteHS.txt', 'r')
    hScore = score.readline()
    sleep(1.5)
    if money > int(hScore):
        score.close()
        score = open('rouletteHS.txt', 'w')
        sleep(.5)
        print('\n\nNEW HIGH SCORE!')
        name = input('Enter your name: ')
        score.write(str(money) + '\n')
        score.write(name + '\n')
        sleep(.5)
        print('\n\nHIGH SCORE:')
        print('\n_____________')
        print(name + ': $' + str(money))

    else:
        sleep(1.5)
        name = score.readline().rstrip()
        print('\n\nHIGH SCORE:')
        print('------------')
        print(name + ': $' + str(hScore))
    score.close()

    score.close()


main()
