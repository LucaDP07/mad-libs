import time

# Function inputs Lists


def inputs_list(a, b):
    for i, element in enumerate(a):
        print(i+1, element)
    chosen = input('')
    while not chosen.isnumeric() or int(chosen) > len(a) or int(chosen) <= 0:
        chosen = input("Invalid data: Select\n" + b)
    el = a[int(chosen)-1]
    return el

# Function to start the game


def start_game():
    answer = input("Let's play, shall we?\n")
    while not any(answer.lower() == f for f in ['yes', 'y', "no", "n"]):
        answer = input('Please enter yes or no\n')
    if any(answer.lower() == f for f in ['yes', 'y']):
        print("Cool, let's play the game!\n")
    else:
        print("That's fine. See you soon\n")
        quit()


def select_name():
    name = input("Enter your name:\n ")
    while not name.isalpha():
        name = input("Enter a name:\n ")
    return name


def select_age():
    age = input("Enter your age:\n ")
    while not age.isnumeric():
        age = input("Enter your age, should be a number:\n ")
    return age


def select_adjective():
    adj = ['perfect', 'rough', 'gentle']
    print('Select an adjective: ')
    adjective_first = inputs_list(adj, " an adjective")
    return adjective_first


def select_color():
    colour = ['red', 'blue', 'green']
    print('Select a color')
    color_first = inputs_list(colour, "a color")
    return color_first


def select_noun():
    nouns = ['car', 'money', 'banana']
    print('Select a noun: ')
    noun_first = inputs_list(nouns, "a noun")
    return noun_first


def select_verb():
    verbs = ['running', 'starving', 'loving']
    print('Select a verb: ')
    verb_first = inputs_list(verbs, "a verb")
    return verb_first


def select_clothing():
    clothings = ['sock', 'pajama', 'skirt']
    print('Select your clothing')
    clothings_first = inputs_list(clothings, "a clothing")
    return clothings_first


def select_adjective_two():
    adj_second = ['angry', 'able', 'busy']
    print('Select an adjective: ')
    adjectives_second = inputs_list(adj_second, "an adjective")
    return adjectives_second


def select_celebrity():
    celeb = ['Ryan Reynolds', 'Emma Stone', 'Tom Hanks']
    print('Select a celebrity: ')
    celebrities = inputs_list(celeb, "a celebrity")
    return celebrities


def select_number():
    number = input('Enter a number:\n ')
    while not number.isnumeric():
        number = input('Enter a number, should be a number: ')
    return number


def select_friend():
    friend = input('Enter the name of a friend:\n ')
    while not friend.isalpha():
        friend = input('Invalida data: Enter a name:\n ')
    return friend


def select_noun_two():
    nouns_second = ['wood', 'ukelele', 'smoothie']
    print('Select a noun: ')
    noun_second = inputs_list(nouns_second, "a noun")
    return noun_second


def select_friend_two():
    friend_second = input('Enter the name of another friend:\n ')
    while not friend_second.isalpha():
        friend_second = input('Invalida data: Enter a name:\n ')
    return friend_second


def run_game():
    print("Welcome to the Mad Libs Game")
    time.sleep(2)

    # Calls the Question Function
    start_game()

    time.sleep(2)

    # User inputs story

    # Name input
    name = select_name()

    # Age Input
    age = select_age()

    # Adjectives List
    adjective_first = select_adjective()

    # Colors List
    color_first = select_color()

    # Nouns List
    noun_first = select_noun()

    # Verbs list
    verb_first = select_verb()

    # Clothings List
    clothings_first = select_clothing()

    # Adjectives Second List
    adjectives_second = select_adjective_two()

    # Celebrities List
    celebrities = select_celebrity()

    # Number Input
    number = select_number()

    # Friend First Input
    friend = select_friend()

    # Nouns Second List
    noun_second = select_noun_two()

    # Friend Second Input
    friend_second = select_friend_two()

    time.sleep(1)

    # Print story - Concat the inputs together in a story
    print('\nTitle: If I were president.')
    print('\n')
    time.sleep(3)
    print("My name is " + name + " and I'm " + age + " years old.")
    time.sleep(3)
    print("If I were president, I'd do a whole bunch of " + adjective_first + " things:")
    time.sleep(3)
    print("I would drive the biggest " + color_first + " car in the country, and that")
    time.sleep(3)
    print("car would go faster than any other " + noun_first + " in the world!")
    time.sleep(3)
    print("Everyone would eat pepperoni pizza for dinner.")
    time.sleep(3)
    print("I would live in the Statue of Liberty and build a " + verb_first + " pool at her feet.")
    time.sleep(3)
    print("I would wear a " + clothings_first + " on my head, and everyone would say I look " + adjectives_second + " like " + celebrities + ".")
    time.sleep(3)
    print("School would be open only " + number + " days a year.")
    time.sleep(3)
    print("I would give my friends the best jobs.")
    time.sleep(3)
    print("I would nominate " + friend + " to be secretary of the " + noun_second + ",")
    time.sleep(3)
    print("and " + friend_second + " could be vice president !")
    time.sleep(3)


if __name__ == '__main__':
    run_game()

