from Game import Game
from time import sleep

def main():
    name = welcome()
    start(name)


# Welcome start
def welcome():
    print('Hello, player! Welcome to Choice Game v2.0 (new name pending...')
    print('Be careful with how you respond. Not all things are what they seem.')
    choice = input('Would you like to run through the tutorial? ').lower()
    if choice == 'y':
        tutorial()
    name = input('\nWhat is your name, player? ')
    return name


# Tutorial
def tutorial():
    print('\nThis is a game of choices')
    print('Every decision you make will impact your future.')
    sleep(2)
    print('For starters, let\'s throw you a practice question:')
    print('You are offered a blowjob (or whatever girls like) from a random man in a white van')
    sleep(2)
    choice  = input('Do you accept or decline? [a/d] ').lower()
    if choice == 'a':
        print('\nYou got the best head of your life and the man gave you ten bucks for a Big Mac!')
        print('You now have ten dollars in your pocket and an enlightened mood.')
    else:
        print('\nYou made the man mad... He was not happy with your decsision. He ran you over.')
        print('You suffer from multiple broken bones, but your not dead!')
        sleep(1)
        print('Wait...')
        sleep(1)
        print('He\'s coming back!')
        sleep(2)
        print('Ooop... Now you\'re dead!')
    sleep(1)
    print('\nSee! Fun right? There is much more intriguing questions to follow (:')
    print('Good luck! Tutorial done.')


# Main game loop
def start(name):
    player = Game(name)
    print('\nLet\'s get this party started!')
    print('Hello, ' + player.getName() + ' you are a mischevious young adolescent, constantly looking for trouble\nin the Austin area.')
    sleep(4)
    print('\nIn your pockets, you have a phone and a crinckled up ten dollar bill. Nothing more')
    sleep(3)
    print('It\'s a Tuesday night and you are looking for something to get into.')
    sleep(2)
    print('You start this adventure in your favorite place, DIRTY 6th!')
    print('You walk into a bar with the loud music and the many people turning it up.')
    sleep(3)
    print('\nYou approach the bartop and grab a seat')
    sleep(2)
    print('The bartender asks you what drink you would like.')
    print('You order your usual. A buttery nipple. FUCKING YUM.')
    sleep(3)
    print('\nA fine young specemin sees the open seat next to you and asks you if the seat is taken.')
    sleep(2)
    choice = input('Do you allow the specimen to take the seat next to you? [y/n] ').lower()
    sleep(1)
    if choice == 'y':
        print('\nYour new party friend grabs the open seat and places their buttocks upon the seat part of the chair.')
        print('They ask you if you would buy them a drink!')
        sleep(1)
        choice = input('Do you agree to purchase an alcoholic beverage for your new found friend? [y/n] ').lower()
        sleep(1)
        if choice == 'y':
            print('\nYou call out "OOOHHHHHHH BARRRTENDEEERRRR!!" and grab the young chap\'s attention.')
            sleep(3)
            print('The bartender comes thru with another sweet ass drank.')
            sleep(2)
            print('On the count of three, you two crazy folks shoot that drank down your wide throats.')
            print('They then ask you if you want to "Get outta here and do the freaky deek"')
            sleep(2)
            print('As the respectable asexual that you are you say "Fuck no" and walk away from the disgusting perv.')
    else:
        print('\nYou get offended by this question.')
        print('You scream at them "CORONA VIRUS BITCH SIX MOTHA FUCKIN FEET!"')
        sleep(4)
        print('They did not appreciate your attitude.')
        sleep(3)
        print('The person picked up your sacred Buttery Nipple and throws it on your nice sweater!')
        sleep(3)
        print('\ncunt\n')
        sleep(3)
        print('Lightly shaken up, you stand up from your chair.')
    sleep(1)
    print('\nAs you\'re heading for the exit, the bartender hands you your check')
    print('You reach into your pocket and find that you lack the necesary funds to pay for your drinks')
    sleep(2)
    chioce = input('Do you hand the man the money that you have and hope that he will let you go or run the fuck up outta there? [p/r] ').lower()
    sleep(1)
    print('\nThat was a trick question. Fuck that guy, you ran outta there faster than your dad did when he heard you were conceived.')
    sleep(2)
    print('\nBack on the streets you look for your next activity...')
    sleep(1)
    #
    #
    #
    print('\n\nStill in development! More to come (:')
    


def outro(player):
    print('Thank you for playing, ' + player.getName() + '!')
    print('That was a pitiful display of decision making. I hope you make better coices in your real life...')
    sleep(2)
    print('Final possesions: ' )
    print('-------------------')
    print(player.getBelt())
    print('$' +player.getMoney())
    sleep(5)
    print('PEACE!')
main()
