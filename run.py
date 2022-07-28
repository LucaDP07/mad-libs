# Python Text Based Game - If I were president.
# Story taken and adapted from the website readbrightly.com


# Import time to print typewriter effect.
import time


# Function to set requirements for the items in the lists.
# If the data entered is not numeric, greater than the number
# of items in the lists, lower than zero or equal to zero,
# an error message will be displayed.
# A loop will repeatedly request data, until it is valid.


def inputs_list(a, b):
    for i, element in enumerate(a):
        print(i+1, element)
    chosen = input('')
    while not chosen.isnumeric() or int(chosen) > len(a) or int(chosen) <= 0:
        chosen = input("Invalid data. Select" + b)
    el = a[int(chosen)-1]
    return el


# Intro function begins the game and welcome the player.
# Moves the player into the game once they have agreed to play
# or quit the game if they decide to not play.


def start_game():
    answer = input("Let's play, shall we? y/n\n")
    while not any(answer.lower() == f for f in ["y", "n"]):
        answer = input('Please enter y or n\n')
    if any(answer.lower() == f for f in ["y"]):
        print("Cool, let's play the game!\n")
    else:
        print("That's fine. See you soon!\n")
        quit()

# While loop to ensure user adds a name


def select_name():
    name = input("Enter your name: ")
    while not name.isalpha():
        name = input("Invalid data. Enter a name: ")
    return name

# While loop to ensure user adds their age


def select_age():
    age = input("Enter your age: ")
    while not age.isnumeric():
        age = input("Invalid data. Should be a number: ")
    return age

# This function allows the player a choice in response.


def select_adjective():
    adj = ['stupid', 'rough', 'crazy']
    print('Select an adjective: ')
    adjective_one = inputs_list(adj, " an adjective: ")
    return adjective_one

# This function allows the player a choice in response.


def select_color():
    colour = ['red', 'blue', 'green']
    print('Select a color: ')
    color_first = inputs_list(colour, "a color: ")
    return color_first

# This function allows the player a choice in response.


def select_noun():
    nouns = ['car', 'money', 'banana']
    print('Select a noun: ')
    noun_first = inputs_list(nouns, "a noun: ")
    return noun_first

# This function allows the player a choice in response.


def select_verb():
    verbs = ['running', 'starving', 'loving']
    print('Select a verb: ')
    verb_first = inputs_list(verbs, "a verb: ")
    return verb_first

# This function allows the player a choice in response.


def select_clothing():
    clothings = ['sock', 'pajama', 'skirt']
    print('Select your clothing: ')
    clothings_first = inputs_list(clothings, "a clothing: ")
    return clothings_first

# This function allows the player a choice in response.


def select_adjective_second():
    adj_second = ['angry', 'able', 'busy']
    print('Select an adjective: ')
    adjectives_two = inputs_list(adj_second, "an adjective: ")
    return adjectives_two

# This function allows the player a choice in response.


def select_celebrity():
    celeb = ['Al Pacino', 'Emma Stone', 'Tom Hanks']
    print('Select a celebrity: ')
    celebrities = inputs_list(celeb, "a celebrity: ")
    return celebrities

# While loop to ensure user adds a number.


def select_number():
    number = input('Enter a number: ')
    while not number.isnumeric():
        number = input('Invalid data. Should be a number: ')
    return number

# While loop to ensure user adds a name.


def select_friend():
    friend = input('Enter the name of a friend: ')
    while not friend.isalpha():
        friend = input('Invalida data. Enter a name: ')
    return friend

# This function allows the player a choice in response.


def select_noun_two():
    nouns_second = ['forest', 'cave', 'car park']
    print('Select a noun: ')
    noun_second = inputs_list(nouns_second, "a noun: ")
    return noun_second

# While loop to ensure user adds a name.


def select_friend_two():
    friend_second = input('Enter the name of another friend: ')
    while not friend_second.isalpha():
        friend_second = input('Invalida data. Enter a name: ')
    return friend_second


def run_game():
    print("Welcome to the Mad Libs Game!")  # greeting message

    # The time sleep function creates a time delay at the end
    # of each sentance/block for a certain amount of seconds.
    time.sleep(2)

    # Display the intro function
    start_game()

    time.sleep(2)

    # Name variable
    name = select_name()

    # Age variable
    age = select_age()

    # Adjectives List
    adjective_one = select_adjective()

    # Colors variable
    color_first = select_color()

    # Nouns variable
    noun_first = select_noun()

    # Verbs variable
    verb_first = select_verb()

    # Clothings variable
    clothings_first = select_clothing()

    # Adjectives second variable
    adjectives_two = select_adjective_second()

    # Celebrities variable
    celebrities = select_celebrity()

    # Number variable
    number = select_number()

    # Friend variable
    friend = select_friend()

    # Nouns second variable
    noun_second = select_noun_two()

    # Friend second variable
    friend_second = select_friend_two()

    time.sleep(1)

    # The story can now be read with the words chosen by the user.
    print('\nTitle: If I were president.')
    print('\n')
    time.sleep(3)
    print("My name is " + name + " and I'm " + age + " years old.")
    time.sleep(3)
    print("If I were president, I'd do a whole")
    time.sleep(3)
    print("bunch of " + adjective_one + " things:")
    time.sleep(3)
    print("I would drive the biggest " + color_first + " car in the country")
    time.sleep(3)
    print("and that car would go faster")
    time.sleep(3)
    print("than any other " + noun_first + " in the world!")
    time.sleep(3)
    print("Everyone would eat pepperoni pizza for dinner.")
    time.sleep(3)
    print("I would live in the Statue of Liberty")
    time.sleep(3)
    print("and build a " + verb_first + " pool at her feet.")
    time.sleep(3)
    print("I would wear a " + clothings_first + " on my head, and everyone")
    time.sleep(3)
    print("would say I look " + adjectives_two + " like " + celebrities + ".")
    time.sleep(3)
    print("School would be open only " + number + " days a year.")
    time.sleep(3)
    print("I would give my friends the best jobs.")
    time.sleep(3)
    print("I would nominate " + friend + " to be")
    time.sleep(3)
    print("secretary of the " + noun_second + ",")
    time.sleep(3)
    print("and " + friend_second + " could be vice president!")
    time.sleep(3)
    print('\n')
    print("The End!")


if __name__ == '__main__':
    run_game()
