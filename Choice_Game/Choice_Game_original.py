def game(name):

    print("\nWelcome, " +name+ " let's test your decision skills")
    print("This is a game of choices; you decide your fate. Every choice you make will lead you down a different path and impact your future. \nLet's see if you can survive")
    jump=input("\nHere comes your first choice: Your friends decide to go jump off a bridge, will you join them? [y/n] ")
    if jump==("y"):
        print("\nYou went with your friends and jumped off a bridge into the lake and had a great time!")
        ice_cream = input("Now they invite you to go get ice cream, do you go with them? [y/n] ")
        if ice_cream==("y"):
            print("\nYou went to get ice cream with your friends! Upon walking in the front door though, you slip on an ice cream cone a child dropped a few moments before.")
            print("You broke your neck and died on the spot.")
            gameOver(name)
        else:
            print("\nYou went back home to tell your mother about your cliff jumping")
            print("Your mom gets really angry at your poor decision. She starts yelling at you, calling you names.")
            yell = input("Do you yell back? [y/n] ")
            if yell==("y"):
                print("\nYour mom gets more angry at your disrespectful attitude and hits you in the head with a frying pan.")
                gameOver(name)
            else:
                print("\nYou take the hurtful words from your mother and then go to your bedroom.")
                room=input("In your room you are deciding if you want to sleep (s) or play video games (g). Which activity do you choose? [s/g] ")
                if room==("s"):
                    print("\nYou sleep peacefully into the night.")
                    noise=input("While sleeping, you hear a loud noise outside of your bedroom door. Do you go inspect where the noise comes from? [y/n] ")
                    if noise==("y"):
                        print("\nYou realize the noise is an intruder!")
                        intruder=input("Do you run back to your room (r) or stay and fight (f)? [r/f] ")
                        if intruder == 'f':
                            print("\nYou grabbed the frying pan and beat that intruder back to his momma's house")
                            print("After the incident, your mother asks you what happened.")
                            hero = input("Do you tell your mother you whooped ass (y) or lie and say he ran off (n)? [y/n] ")
                            if hero == 'y':
                                print("\nYour mother gets upset for using her good frying pan and kicks you out of the house")
                                print("You are now out on the streets, cold and tired.")
                                go = input("Do you go to your friends house (f) or try to go back home (h)? [f/h] ")
                                if go == 'f':
                                    print("\nYour friends all get together with some mixers so y'all can get litty")
                                    mix = input("Do you choose to drink the lemonade or sprite [l/s]" )
                                    if mix == 'l':
                                        print("\nYour friends forgot to mention that the lemonade had been spiked with L$D.")
                                        print("You start trippin balls and hallucinating. You see a human sized spider chilling on your couch.")
                                        spider = input("Do you go sit (s) with the spider on the couch or grab a knife and kill (k) it? [s/k] ")
                                        if spider == 'k':
                                            print('\nYou grab the knife and stab the spider 17 times until it stops saying "bro wtf."')
                                            print("The spider turned out to actually just be your buddy, innocently watching Bandersnatch.")
                                            print("You and your other buddies laugh at the fact you thought he was a spider.")
                                            hide = input("Do you hide (h) the body or call (c) the police? [h/c]" )
                                            if hide == 'h':
                                                print("\nYou and your friends throw the body in the back of the truck and drive over to the 360 bridge.")
                                                print("Getting out of the truck you see a cute puppy")
                                                pup = input("Do you go pet (p) the puppy or leave (l) it alone [p/l] ")
                                                if pup == 'p':
                                                    print("\nThe cute puppy was actually a wolf.")
                                                    print("The wolf mauls your whole face off")
                                                    gameOver(name)
                                                else:
                                                    print("\nThe puppy wonders off into the trees while you tend to your important business.")
                                                    print("You throw the dead body over the bidge into the water. Hooray!")
                                                    print("A few seconds later, you see something emerge from the water. It's your friend coming back as a zombie.")
                                                    ohNo = input("Do you get back in the truck and run (r) away or alert (a) the authorities that there's a zombie on the loose? [r/a] ")
                                                    if ohNo == "r":
                                                        print("\nYou and your remaining friends attempt to run away from the zombie and crash the truck into a tree.")
                                                        print("There were no survivors.")
                                                        gameOver(name)
                                                    else:
                                                        print("\nThe authorities arive on the scene and discovers the dead body floating in the water and you tripping out on drugs.")
                                                        print("You were arrested and charged with homicide and drug abuse. You will now be serving a sentence of 25 years to life.")
                                                        gameOver(name)
                                            else:
                                                print("\nThe police arive on scene only to find you holding a knife covered in blood and your friend dead on the couch.")
                                                print("The police immediately fire their weapons on you, mistaking your black hoodie for dark skin. You're dead.")
                                                gameOver(name)     
                                        else: 
                                            print("\nYou take a seat next to the spider.")
                                            print("The spider turned out to be a really cool dude. He even made you a blanket from it's web.")
                                            print("The blanket is so comfortable it put you to sleep.")
                                            print("Though, you wake up 15 minutes later to the spider eating your face off.")
                                            run = input("Do you run to the bathroom (b) to check the mirror or run out of the house (h)? [b/h] ")
                                            if run == 'b':
                                                print("\nYou check your face in the mirror and it's gone!")
                                                print("All gone... nothing left.")
                                                shoot = input("Do you put (p) yourself out of your missery or allow (a) yourself to live the rest of your life with no face? [p/a] ")
                                                if shoot == 'p':
                                                    print("\nYou find a gun in your friend's parents room, put it to your head, and release yourself from a faceless life.")
                                                    print("Too bad you failed to realize that your face was just fine, you were only tripping on drugs.")
                                                    gameOver(name)
                                                else:
                                                    print("\nYou make the brave decision to live without a face.")
                                                    print('You walk out of the bathroom and scream "I\'m ugly and I\'m proud!"')
                                                    print("Your hideousness spooked one of your friend and he shot you in your nonexistent face.")
                                                    gameOver(name)
                                            else:
                                                print("\nYou frantically run out of the house and into the street where a car mistakes you for a hideous monster and runs you over.")
                                                gameOver(name)
                                                                 
                                    else:
                                        print("\nThe Sprite tasted a little funny. You come to find out that the Sprite was spiked with Codeine. You were drinking lean.")
                                        print("You begin to feel light headed so you go sit down on the couch to watch Netflix.")
                                        print("In your daze, you fail to realize that your friend tripping on acid has mistaken you for a very large spider.")
                                        print('Your friend begins to stab you with a knife while all you can mutter is "wtf bro."')
                                        print("You died on the couch.")
                                        gameOver(name)
                                else:
                                    print("\nYou find that your window was left unlocked so you go inside.")
                                    print("Your mom thinks that the intruder came back and unintentionally blammies you with a shotgun.")
                                    gameOver(name)
                            else:
                                print("\nYour mother calls you a pussy for not protecting the house")
                                print("You get upset with your mother for not caring for your safety and call her a bitch")
                                print("Oh no you didn't... I'm going to spare you the details but your mother killed you for disrespecting her")
                                gameOver(name)
                        else:
                            print("\nYou spooked the intruder. He followed you to your room and shoots you cold.")
                            gameOver(name)
                    else:
                        print("\nYou ignore the noise and try to pretend it didn't happen. The noise came from a home intruder though, he found his way into your bedroom and shoots you cold.")
                        gameOver(name)
                else:
                    print("\nWhile playing your game, you realize that during your cliff jumping adventure you developed brain damage. The flashing lights of the game causes you to have a seizure.")
                    gameOver(name)
    if jump==("n"):
        print("\nYou decided to stay home while your friends jump off a bridge")
        homework=input("Since you decided to stay home, will you do your homework now? [y/n] ")
        if homework==("n"):
            print("\nYou didn't do your homework. You failed your computer science class. You got kicked out of the university and decided to sell drugs to make money.")
            sell=input("A man walks up to you at your regular spot and asks if he can try a sample. Do you give him a sample? [y/n] ")
            print("\nIt was a setup, the cops are on you now!")
            run=input("Are you going to run? [y/n] ")
            if run==("y"):
                print("\nYou attempted to run. You ran off a cliff")
                gameOver(name)
            else:
                print("\nThe police took you into custody, you are now serving 25 years to life")
                print("You ended up in prison. Better luck next time!")
                gameOver(name)
        else:
            print("\nYou study hard and complete all of your assignments.")
            nap=input("Now that you are done with your homework, will you get something to eat (e) or take a nap (n)? [e/n] ")
            if nap==("n"):
                print("\nYour long nap takes you into the night.")
                noise = input("While sleeping, you hear a loud noise outside of your bedroom door. Do you go inspect where the noise comes from? [y/n] ")
                if noise==("y"):
                        print("\nYou realize the noise is an intruder!")
                        intruder=input("Do you run back to your room (r) or stay and fight (f)? [r/f] ")
                        if intruder == 'f':
                            print("\nYou grabbed the frying pan and beat that intruder back to his momma's house")
                            print("After the incident, your mother asks you what happened.")
                            hero = input("Do you tell your mother you whooped ass (y) or lie and say he ran off (n)? [y/n] ")
                            if hero == 'y':
                                print("\nYour mother gets upset for using her good frying pan and kicks you out of the house")
                                print("You are now out on the streets, cold and tired.")
                                go = input("Do you go to your friends house (f) or try to go back home (h)? [f/h] ")
                                if go == 'f':
                                    print("\nYour friends all get together with some mixers so y'all can get litty")
                                    mix = input("Do you choose to drink the lemonade or sprite [l/s]" )
                                    if mix == 'l':
                                        print("\nYour friends forgot to mention that the lemonade had been spiked with L$D.")
                                        print("You start trippin balls and hallucinating. You see a human sized spider chilling on your couch.")
                                        spider = input("Do you go sit (s) with the spider on the couch or grab a knife and kill (k) it? [s/k] ")
                                        if spider == 'k':
                                            print('\nYou grab the knife and stab the spider 17 times until it stops saying "bro wtf."')
                                            print("The spider turned out to actually just be your buddy, innocently watching Bandersnatch.")
                                            print("You and your other buddies laugh at the fact you thought he was a spider.")
                                            hide = input("Do you hide (h) the body or call (c) the police? [h/c]" )
                                            if hide == 'h':
                                                print("\nYou and your friends throw the body in the back of the truck and drive over to the 360 bridge.")
                                                print("Getting out of the truck you see a cute puppy")
                                                pup = input("Do you go pet (p) the puppy or leave (l) it alone [p/l] ")
                                                if pup == 'p':
                                                    print("\nThe cute puppy was actually a wolf.")
                                                    print("The wolf mauls your whole face off")
                                                    gameOver(name)
                                                else:
                                                    print("\nThe puppy wonders off into the trees while you tend to your important business.")
                                                    print("You throw the dead body over the bidge into the water. Hooray!")
                                                    print("A few seconds later, you see something emerge from the water. It's your friend coming back as a zombie.")
                                                    ohNo = input("Do you get back in the truck and run (r) away or alert (a) the authorities that there's a zombie on the loose? [r/a] ")
                                                    if ohNo == "r":
                                                        print("\nYou and your remaining friends attempt to run away from the zombie and crash the truck into a tree.")
                                                        print("There were no survivors.")
                                                        gameOver(name)
                                                    else:
                                                        print("\nThe authorities arive on the scene and discovers the dead body floating in the water and you tripping out on drugs.")
                                                        print("You were arrested and charged with homicide and drug abuse. You will now be serving a sentence of 25 years to life.")
                                                        gameOver(name)
                                            else:
                                                print("\nThe police arive on scene only to find you holding a knife covered in blood and your friend dead on the couch.")
                                                print("The police immediately fire their weapons on you, mistaking your black hoodie for dark skin. You're dead.")
                                                gameOver(name)
                                        else:
                                            print("\nYou take a seat next to the spider.")
                                            print("The spider turned out to be a really cool dude. He even made you a blanket from it's web.")
                                            print("The blanket is so comfortable it put you to sleep.")
                                            print("Though, you wake up 15 minutes later to the spider eating your face off.")
                                            run = input("Do you run to the bathroom (b) to check the mirror or run out of the house (h)? [b/h] ")
                                            if run == 'b':
                                                print("\nYou check your face in the mirror and it's gone!")
                                                print("All gone... nothing left.")
                                                shoot = input("Do you put (p) yourself out of your missery or allow (a) yourself to live the rest of your life with no face? [p/a] ")
                                                if shoot == 'p':
                                                    print("\nYou find a gun in your friend's parents room, put it to your head, and release yourself from a faceless life.")
                                                    print("Too bad you failed to realize that your face was just fine, you were only tripping on drugs.")
                                                    gameOver(name)
                                                else:
                                                    print("\nYou make the brave decision to live without a face.")
                                                    print('You walk out of the bathroom and scream "I\'m ugly and I\'m proud!"')
                                                    print("Your hideousness spooked one of your friend and he shot you in your nonexistent face.")
                                                    gameOver(name)
                                            else:
                                                print("\nYou frantically run out of the house and into the street where a car mistakes you for a hideous monster and runs you over.")
                                                gameOver(name)
                                    else:
                                        print("\nThe Sprite tasted a little funny. You come to find out that the Sprite was spiked with Codeine. You were drinking lean.")
                                        print("You begin to feel light headed so you go sit down on the couch to watch Netflix.")
                                        print("In your daze, you fail to realize that your friend tripping on acid has mistaken you for a very large spider.")
                                        print('Your friend begins to stab you with a knife while all you can mutter is "wtf bro."')
                                        print("You died on the couch.")
                                        gameOver(name)
                                else:
                                    print("\nYou find that your window was left unlocked so you go inside.")
                                    print("Your mom thinks that the intruder came back and unintentionally blammies you with a shotgun.")
                                    gameOver(name)
                            else:
                                print("\nYour mother calls you a pussy for not protecting the house")
                                print("You get upset with your mother for not caring for your safety and call her a bitch")
                                print("Oh no you didn't... I'm going to spare you the details but your mother killed you for disrespecting her")
                                gameOver(name)
                        else:
                            print("\nYou spooked  the intruder. He followed you to your room and shoots you cold.")
                            gameOver(name)
                else:
                    print("\nYou ignore the noise and try to pretend it didn't happen. The noise came from a home intruder though, he found his way into your bedroom and shoots you cold.")
                    gameOver(name)
            else:
                print("\nYou eat some bangers and mash. You have now satisfied your cravings")
                print("Your friends come over to da crib with some mixers so y'all can get litty")
                mix = input("Do you choose to drink the lemonade or sprite [l/s]" )
                if mix == 'l':
                    print("\nYour friends forgot to mention that the lemonade had been spiked with L$D.")
                    print("You start trippin balls and hallucinating. You see a human sized spider chilling on your couch.")
                    spider = input("Do you go sit (s) with the spider on the couch or grab a knife and kill (k) it? [s/k] ")
                    if spider == 'k':
                        print('\nYou grab the knife and stab the spider 17 times until it stops saying "bro wtf."')
                        print("The spider turned out to actually just be your buddy, innocently watching Bandersnatch.")
                        print("You and your other buddies laugh at the fact you thought he was a spider.")
                        hide = input("Do you hide (h) the body or call (c) the police? [h/c]" )
                        if hide == 'h':
                            print("\nYou and your friends throw the body in the back of the truck and drive over to the 360 bridge.")
                            print("Getting out of the truck you see a cute puppy")
                            pup = input("Do you go pet (p) the puppy or leave (l) it alone [p/l] ")
                            if pup == 'p':
                                print("\nThe cute puppy was actually a wolf.")
                                print("The wolf mauls your whole face off")
                                gameOver(name)
                            else:
                                print("\nThe puppy wonders off into the trees while you tend to your important business.")
                                print("You throw the dead body over the bidge into the water. Hooray!")
                                print("A few seconds later, you see something emerge from the water. It's your friend coming back as a zombie.")
                                ohNo = input("Do you get back in the truck and run (r) away or alert (a) the authorities that there's a zombie on the loose? [r/a] ")
                                if ohNo == "r":
                                    print("\nYou and your remaining friends attempt to run away from the zombie and crash the truck into a tree.")
                                    print("There were no survivors.")
                                    gameOver(name)
                                else:
                                    print("\nThe authorities arive on the scene and discovers the dead body floating in the water and you tripping out on drugs.")
                                    print("You were arrested and charged with homicide and drug abuse. You will now be serving a sentence of 25 years to life.")
                                    gameOver(name)
                        else:
                            print("\nThe police arive on scene only to find you holding a knife covered in blood and your friend dead on the couch.")
                            print("The police immediately fire their weapons on you, mistaking your black hoodie for dark skin. You're dead.")
                            gameOver(name)  
                    else:

                        print("\nYou take a seat next to the spider.")
                        print("The spider turned out to be a really cool dude. He even made you a blanket from it's web.")
                        print("The blanket is so comfortable it put you to sleep.")
                        print("Though, you wake up 15 minutes later to the spider eating your face off.")
                        run = input("Do you run to the bathroom (b) to check the mirror or run out of the house (h)? [b/h] ")
                        if run == 'b':
                            print("\nYou check your face in the mirror and it's gone!")
                            print("All gone... nothing left.")
                            shoot = input("Do you put (p) yourself out of your missery or allow (a) yourself to live the rest of your life with no face? [p/a] ")
                            if shoot == 'p':
                                print("\nYou find a gun in your friend's parents room, put it to your head, and release yourself from a faceless life.")
                                print("Too bad you failed to realize that your face was just fine, you were only tripping on drugs.")
                                gameOver(name)
                            else:
                                print("\nYou make the brave decision to live without a face.")
                                print('You walk out of the bathroom and scream "I\'m ugly and I\'m proud!"')
                                print("Your hideousness spooked one of your friend and he shot you in your nonexistent face.")
                                gameOver(name)
                        else:
                            print("\nYou frantically run out of the house and into the street where a car mistakes you for a hideous monster and runs you over.")
                            gameOver(name)

                else:
                    print("\nThe Sprite tasted a little funny. You come to find out that the Sprite was spiked with Codeine. You were drinking lean.")
                    print("You begin to feel light headed so you go sit down on the couch to watch Netflix.")
                    print("In your daze, you fail to realize that your friend tripping on acid has mistaken you for a very large spider.")
                    print('Your friend begins to stab you with a knife while all you can mutter is "wtf bro."')
                    print("You died on the couch.")
                    gameOver(name)  
                
def name():
    print("Welcome to Alex's game of choices!")
    name= input("What is your name, player? ")
    game(name)

def gameOver(name):
    
    print("\nYou lose. Better luck next time, " +name+ "!")
    play=input("Would you like to play again? [y/n] ")
    if play == "y":
        game(name)
    else:
        quit

name()













    
    
