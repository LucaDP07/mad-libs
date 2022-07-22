import time

#Function inputs Lists


def inputs_list(a, b):
    for i,element in enumerate(a):
        print(i+1, element)
    chosen=input('')
    while not chosen.isnumeric() or int(chosen)>len(a):
        chosen = input("Invalid data: Select" + b)
    el=a[int(chosen)-1]
    return el

#Function to start the game


def start_game():
    answer = input("Let's play, shall we?\n")
    while not any(answer.lower() == f for f in ['yes', 'y', "no", "n"]):
        answer = input('Please enter yes or no')
    if any(answer.lower() == f for f in ['yes', 'y']):
        print("Cool, let's play the game!")
        
    else:
        print("That's fine. See you soon\n")
        quit()

# Welcome message
def select_color():
    colour = ['red', 'blue', 'green']
    print ('Select a color')
    colorFirst = inputs_list(colour, "a color")
    return colorFirst

    
def run_game():


    print("Welcome to the Mad Libs Game")
    time.sleep(2) 

    #Calls the Question Function   
    
    start_game()               
    time.sleep(2)

    #User inputs story

    #Name input
    name = input("Enter your name: ")
    while not name.isalpha():
        name= input("Enter a name: ")

    #Age Input
    age = input("Enter your age: ")
    while not age.isnumeric():
        age = input("Enter your age, should be a number: ")

    #Adjectives List
    adj = ['perfect', 'rough', 'gentle']
    print('Select an adjective: ')
    adjectiveFirst = inputs_list(adj, " an adjective")

    #Colors List
    colorFirst = select_color()

    #Nouns List
    nouns= ['car', 'money', 'banana']
    print('Select a noun: ')
    nounFirst = inputs_list(nouns, "a noun")

    #Verbs list
    verbs= ['running', 'starving', 'loving']
    print('Select a verb: ')
    verbFirst = inputs_list(verbs, "a verb")

    #Clothings List
    clothings = ['sock', 'pajama', 'skirt']
    print ('Select your clothing')
    clothingsFirst = inputs_list(clothings, "a clothing")

    #Adjectives Second List
    adjSecond= ['angry', 'able', 'busy']
    print('Select an adjective: ')
    adjectivesSecond = inputs_list(adjSecond, "an adjective")

    #Celebrities List
    celeb= ['Ryan Reynolds', 'Emma Stone', 'Tom Hanks']
    print('Select a celebrity: ')
    celebrities = inputs_list(celeb, "a celebrity")

    #Number Input
    number = input('Enter a number: ')
    while not number.isnumeric(): 
        number = input('Enter a number, should be a number: ')

    #Friend First Input
    friend = input('Enter the name of a friend: ')
    while not friend.isalpha():
        friend = input('Invalida data: Enter a name: ')

    #Nouns Second List
    nounsSecond = ['wood', 'ukelele', 'smoothie']
    print('Select a noun: ')
    nounSecond = inputs_list(nounsSecond, "a noun")

    #Friend Second Input
    friendSecond = input('Enter the name of another friend: ')
    while not friendSecond.isalpha():
        friendSecond = input('Invalida data: Enter a name: ')

    time.sleep(1)

    # Print story - Concat the inputs together in a story
    print('\nTitle: If I were president.')
    print('\n')
    time.sleep(3)
    print("My name is " + name + " and I'm " + age + " years old.")
    time.sleep(3)
    print("If I were president, I'd do a whole bunch of " + adjectiveFirst + " things:")
    time.sleep(3)
    print("I would drive the biggest " + colorFirst + " car in the country, and that")
    time.sleep(3)
    print("car would go faster than any other " + nounFirst + " in the world!")
    time.sleep(3)
    print("Everyone would eat pepperoni pizza for dinner.")
    time.sleep(3)
    print("I would live in the Statue of Liberty and build a " + verbFirst + " pool at her feet.")
    time.sleep(3)
    print("I would wear a " + clothingsFirst + " on my head, and everyone would say I look " + adjectivesSecond + " like " + celebrities + ".")
    time.sleep(3)
    print("School would be open only " + number + " days a year.")
    time.sleep(3)
    print("I would give my friends the best jobs.")
    time.sleep(3)
    print("I would nominate " + friend + " to be secretary of the " + nounSecond + ",")
    time.sleep(3)
    print("and " + friendSecond + " could be vice president !")
    time.sleep(3)

if __name__ == '__main__':
    run_game()