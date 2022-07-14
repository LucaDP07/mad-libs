import time

# Welcome messages
print("Welcome to the Mad Libs Game")
time.sleep(2)
answer = input("Let's play, shall we?\n")

# While loop
while answer not in ["Yes", "yes", "Y", "y", "No", "no", "N", "n"]: 
        
        answer = input("Wrong input. Do you want to play? Yes or No\n") 
# If statement
if answer == "Yes" or answer == "yes" or answer == "Y" or answer == "y": 
        print("Ok, let's play the game: \n")
elif answer == "No" or answer == "no" or answer == "N" or answer == "n": 
        print("That's fine. See you soon\n") 
        quit()
else: 
        print("Please type Yes or No\n") 

# User inputs story #1
colors = ['red', 'blue', 'green']
noun = input("Enter your name: ")
number = input("Enter your age: ")
while not number.isnumeric():
        number = input("Enter your age, should be a number: ")
noun4 = input("Enter the name of a friend: ")
adj = input("Enter an adjective: ")
print ('Select number of colour')
for i,colour in enumerate(colors):
    print(i+1, colour)
chosen=input('')
while not chosen.isnumeric() or int(chosen)>len(colors):
        chosen = input("invalid data: ")
color=colors[int(chosen)-1]
noun2 = input("Enter a noun: ")
food = input("Enter a type of food(plural): ")
noun3 = input("Enter a noun: ")
verb = input("Enter a verb ending in 'ing': ")
while not verb.endswith('ing'):
        verb = input("invalid: ")
clothing = input("Enter an article of clothing: ")
adj2 = input("Enter an adjective: ")
celebrity = input("Enter the name of a celebrity: ")
number2 = input("Enter a number: ")
while not number2.isnumeric():
        number2 = input("Enter a number, should be a number: ")
noun4 = input("Enter the name of a friend: ")
noun5 = input("Enter a noun: ")
noun6= input("Enter the name of another friend: ")
occupation = input("Enter an occupation: ")
time.sleep(1)

# Print story #1

print('\nTitle: If I were president.')
print('\n')
time.sleep(3)
print("My name is " + noun + "and I'm " + number + " years old.")
time.sleep(3)
print("If I were president, I'd do a whole bunch of " + adj + " things:")
time.sleep(3)
print("I would drive the biggest " + color + " car in the country, and that")
time.sleep(3)
print("car would go faster than any other " + noun2 + " in the world!")
time.sleep(3)
print("Everyone would eat pepperoni " + food + " for dinner.")
time.sleep(3)
print("I would live in the Statue of " + noun3 + " and build a " + verb + " pool at her feet.")
time.sleep(3)
print("I would wear a/an " + clothing + " on my head, and everyone would say I look " + adj2 + " like " + celebrity + ".")
time.sleep(3)
print("School would be open only " + number2 + " days a year.")
time.sleep(3)
print("I would give my friends the best jobs.")
time.sleep(3)
print("I would nominate " + noun4 + " to be secretary of the " + noun5 + ",")
print("and " + noun6 + " could be vice " + occupation + " !")
time.sleep(3)
play = input("Play again?")

answer = input("Let's play, shall we?\n")
# While loop
while answer not in ["Yes", "yes", "Y", "y", "No", "no", "N", "n"]: 
        
        answer = input("Wrong input. Do you want to play? Yes or No\n") 
# If statement
if answer == "Yes" or answer == "yes" or answer == "Y" or answer == "y": 
        print("Ok, let's play the game: \n")
elif answer == "No" or answer == "no" or answer == "N" or answer == "n": 
        print("That's fine. See you soon\n") 
        quit()
else: 
        print("Please type Yes or No\n") 

# User inputs story #2

verb = input("Enter a verb ending in 'ing': ")
noun = input("Enter the name of a place: ")
adj = input("Enter an adjective: ")
adj2 = input("Enter an adjective: ")
verb2 = input("Enter a verb: ")
noun2 = input("Enter a plural noun: ")
noun3 = input("Enter a noun: ")
verb3 = input("Enter a verb ending in 'ing': ")
verb4 = input("Enter a verb ending in 'ing': ")
noun4 = input("Enter a plural noun: ")
verb5 = input("Enter a verb ending in 'ing': ")
noun5 = input("Enter a plural noun: ")
noun6 = input("Enter a plural noun/places: ")
verb6 = input("Enter a verb ending in 'ing': ")
noun7 = input("Enter a plural noun/places: ")
adj3 = input("Enter an adjective: ")
noun8 = input("Enter a plural noun: ")
verb7 = input("Enter a verb: ")

# Print story #2

print('\nTitle: Taking the Train')
print('\n')
time.sleep(3)
print("I love " + verb + " on a train from my " + noun + " to the " + adj + " city.")
time.sleep(3)
print("Trains are " + adj2 + " because they " + verb2 + " on special " + noun2 + " made of " + noun3 + " instead of roads.")
time.sleep(3)
print("It's fun " + verb3 + " for the train and " + verb4 + " the " + noun4 + " sound as the train arrives.")
time.sleep(3)
print("While " + verb5 + " on the train, I like to look out the " + noun5 + " and see the countryside, passing " + noun6 + " ")
print("and " + verb6 + " " + noun7 + " and " + adj3 + " " + noun8 + " as we " + verb7  + " past.")
time.sleep(3)
play = input("Play again?")

answer = input("Let's play, shall we?\n")
# While loop
while answer not in ["Yes", "yes", "Y", "y", "No", "no", "N", "n"]: 
        
        answer = input("Wrong input. Do you want to play? Yes or No\n") 
# If statement
if answer == "Yes" or answer == "yes" or answer == "Y" or answer == "y": 
        print("Ok, let's play the game: \n")
elif answer == "No" or answer == "no" or answer == "N" or answer == "n": 
        print("That's fine. See you soon\n") 
        quit()
else: 
        print("Please type Yes or No\n") 

# User inputs story #3


noun = input("Enter the name of a month ")
verb = input("Enter a verb: ")
noun2 = input("Enter the name of a place: ")
adj = input("Enter an adjective: ")
adj2 = input("Enter an adjective: ")
noun3 = input("Enter the name of a place: ")
verb2 = input("Enter a verb: ")
noun4 = input("Enter a noun: ")
verb3 = input("Enter a verb: ")
noun5 = input("Enter a noun: ")
adj2 = input("Enter an adjective: ")
adj3 = input("Enter an adjective: ")
color = input("Enter a color: ")
adj4 = input("Enter an adjective: ")
verb4 = input("Enter a verb: ")
verb5 = input("Enter a verb: ")
noun6 = input("Enter a noun: ")

# Print story #3

print('\nTitle: Christmas Tree')
print('\n')
time.sleep(3)
print("Every " + noun + " we " + verb + " to a tree " + noun2 + " far away.")
time.sleep(3)
print("Not just any " + adj + " farm, a " + adj2 + " tree " + noun3 + ".")
time.sleep(3)
print("My dad and I " + verb2 + " onto the " + noun4 + " to " + verb3 + " for the perfect " + noun4 + ".")
time.sleep(3)
print("Some people like them " + adj2 + " and " + adj3 + " and some like them " + color + " and fat.")
time.sleep(3)
print("We are searching for a tall and " + adj4 + " one!")
time.sleep(3)
print("Then I finally see it. Off we " + verb4 + " saw in hand to " + verb5 + " this year's " + noun6 + " down.")
time.sleep(3)
print("It's Christmas now!")
time.sleep(3)
play = input("Play again?")

answer = input("Let's play, shall we?\n")
# While loop
while answer not in ["Yes", "yes", "Y", "y", "No", "no", "N", "n"]: 
        
        answer = input("Wrong input. Do you want to play? Yes or No\n") 
# If statement
if answer == "Yes" or answer == "yes" or answer == "Y" or answer == "y": 
        print("Ok, let's play the game: \n")
elif answer == "No" or answer == "no" or answer == "N" or answer == "n": 
        print("That's fine. See you soon\n") 
        quit()
else: 
        print("Please type Yes or No\n")  

# User inputs story #4

adj = input("Enter an adjective: ")
noun = input("Enter a noun: ")
adj2 = input("Enter an adjective: ")
verb = input("Enter a verb ending in 'ing': ")
adj3 = input("Enter an adjective: ")
verb2 = input("Enter a verb ending in 'ing': ")
adj4 = input("Enter an adjective: ")
adj5 = input("Enter an adjective: ")
adj6 = input("Enter an adjective: ")
verb3 = input("Enter a verb: ")
adj8 = input("Enter an adjective: ")
verb4 = input("Enter a verb: ")
verb5 = input("Enter a verb ending in 'ing': ")
noun2 = input("Enter a noun: ")
adj7 = input("Enter an adjective: ")
adj8 = input("Enter an adjective: ")
noun3 = input("Enter a noun: ")

# print story #4

print('\nTitle: My Favorite Weather')
print('\n')
time.sleep(3)
print("My " + adj + " weather is during the month of " + noun + " when it's " + adj2 + " outside and everyone is " + verb + " and having a " + adj3 + " time.")
time.sleep(3)
print("The sun is " + verb2 + " and " + adj4 + ", and the people wear " + adj5 + " clothes to stay " + adj6 + ".")
time.sleep(3)
print("Many people " + verb3 + " on vacation in this weather.")
time.sleep(3)
print("It's a " + adj7 + " time to " + verb4 + " things like go " + verb5 + " at a " + noun2 + " or to explore " + adj8 + " places.")
time.sleep(3)
print("What's your " + adj8 + " type of " + noun3 + "?")

answer = input("Let's play, shall we?\n")
# While loop
while answer not in ["Yes", "yes", "Y", "y", "No", "no", "N", "n"]: 
        
        answer = input("Wrong input. Do you want to play? Yes or No\n") 
# If statement
if answer == "Yes" or answer == "yes" or answer == "Y" or answer == "y": 
        print("Ok, let's play the game: \n")
elif answer == "No" or answer == "no" or answer == "N" or answer == "n": 
        print("That's fine. See you soon\n") 
        quit()
else: 
        print("Please type Yes or No\n") 
