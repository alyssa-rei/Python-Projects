#
#
#
# Python:   3.10.5
#
# Author:   Alyssa Rei
#
# Purpose:  The Tech Academy - Python Course; creating our first program together.
#           Demonstrating how to pass variables from function to function
#           while producing a functional game.
#
#
#



def start(nice=0, mean=0, name=""):
    # Get user's name
    name = describe_game(name)
    nice, mean, name = nice_mean(nice, mean, name)

def describe_game(name):
    """
        Check if this a new game or not.
        If it is new, get the user's name.
        If it is not new, thank the player for
        playing again and continue with the game.
    """

    # Meaning, if we do not already have this user's name,
    # then they are a new player and we need to get their name

    if name != "":
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name !="":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted \nby several people. \nYou can choose to be nice or mean,")
                    print("but at the end of the game, your fate \nwill be sealed by your actions.")
                    stop = False
    return name



def nice_mean(nice, mean, name):
    stop = True
    while stop:
        show_score(nice, mean, name)
        pick = input("\nA stranger approaches you for a \nconversation. Will you be nice \nor mean? (N/M) \n>>> ").lower()
        if pick == "n":
                print("\nThe stranger walks away smiling...")
                nice = (nice + 1)
                stop = False
        if pick == "m":
                print("\nThe stranger glares at you \nmenacingly and storms off...")
                mean = (mean + 1)
                stop = False
        pick = input("\nA stranger approaches you and asks \nto use your phone. Will you be nice \nor mean? (N/M) \n>>> ").lower()
        if pick == "n":
                print("\nThe stranger uses your phone \nand thanks you...")
                nice = (nice + 1)
                stop = False
        if pick == "m":
                print("\nThe stranger glares at you \nmenacingly and storms off...")
                mean = (mean + 1)
                stop = False
        pick = input("\nA stranger approaches you to ask \nfor directions. Will you be nice \nor mean? (N/M) \n>>> ").lower()
        if pick == "n":
                print("\nThe stranger thanks you and drives away...")
                nice = (nice + 1)
                stop = False
        if pick == "m":
                print("\nThe stranger glares at you \nmenacingly and drives off...")
                mean = (mean + 1)
                stop = False
    score(nice, mean, name) # Pass the 3 variables to the score()



def show_score(nice, mean, name):
    print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name, nice, mean))



def score(nice, mean, name):
    # Score function is being passed the values stored within the three variables
    if nice > 1: # if condition is valid, call win function passing in the variables so it can use them
        win(nice, mean, name)
    if mean > 1: # if condition is valid, call lose function passing in the variables so it can use them
        lose(nice, mean, name)
    else:        # else, call nice_mean function passing in the variables so it can use them
        nice_mean(nice, mean, name)



def win(nice, mean, name):
    # Substitute the {} wildcards with our variable values
    print("\nNice job, {}. You win! \nEveryone loves you and you've \nmade lots of friends along the way!".format(name))
    # Call again function and pass in our variables
    again(nice, mean, name)

def lose(nice, mean, name):
    # Substitute the {} wildcards with our variable values
    print("\nAhh, too bad, game over! \n{}, you live in a dirty, beat-up van \nby the river, wretched, \nand alone!".format(name))
    # Call again function and pass in our variables
    again(nice, mean, name)



def again(nice, mean, name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (Y/N):\n>>> ").lower()
        if choice == "y":
            stop = False
            reset(nice, mean, name)
        if choice == "n":
            print("\nOh, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\nEnter ( Y ) for 'YES', ( N ) for 'NO':\n>>>")



def reset(nice, mean, name):
    nice = 0
    mean = 0
    # Notice, I do not reset the name variables as that same user has elected to play again
    start(nice, mean, name)



if __name__ == "__main__":
    start()