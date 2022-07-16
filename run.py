import time
#import random

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

# User inputs story 1

colours = ['red', 'blue', 'green']
clothings = ['socks', 'pajamas', 'skirt']
name = input("Enter your name: ")
age = input("Enter your age: ")

while not age.isnumeric():
 age = input("Enter your age, should be a number: ")

adj = input("Enter an adjective: ")
print ('Select number of color')

for i,colour in enumerate(colours):
        print(i+1, colour)
chosen=input('')
while not chosen.isnumeric() or int(chosen)>len(colours):
        chosen = input("invalid data: ")
color=colours[int(chosen)-1]

noun = input("Enter a noun: ")
verb = input("Enter a verb ending in 'ing': ")

while not verb.endswith('ing'):
        verb = input("invalid data: ")

print ('Select your clothing')

for i,clothings in enumerate(clothings):
        print(i+1, clothings)
chosen=input('')
while not chosen.isnumeric() or int(chosen)>len(clothings):
        chosen = input("invalid data: ")
cloth=clothings[int(chosen)-1]

adj2 = input("Enter an adjective: ")
celebrity = input("Enter the name of a celebrity: ")
number = input("Enter a number: ")

while not number.isnumeric():
        number = input("Enter a number, should be a number: ")

friend = input("Enter the name of a friend: ")
noun2 = input("Enter a noun: ")
friend2 = input("Enter the name of another friend: ")
time.sleep(1)

# Print story 1

print('\nTitle: If I were president.')
print('\n')
time.sleep(3)
print("My name is " + name + " and I'm " + age + " years old.")
time.sleep(3)
print("If I were president, I'd do a whole bunch of " + adj + " things:")
time.sleep(3)
print("I would drive the biggest " + color + " car in the country, and that")
time.sleep(3)
print("car would go faster than any other " + noun + " in the world!")
time.sleep(3)
print("Everyone would eat pepperoni pizza for dinner.")
time.sleep(3)
print("I would live in the Statue of Liberty and build a " + verb + " pool at her feet.")
time.sleep(3)
print("I would wear a/an " + clothings + " on my head, and everyone would say I look " + adj2 + " like " + celebrity + ".")
time.sleep(3)
print("School would be open only " + number + " days a year.")
time.sleep(3)
print("I would give my friends the best jobs.")
time.sleep(3)
print("I would nominate " + friend + " to be secretary of the " + noun2 + ",")
print("and " + friend2 + " could be vice president !")
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

# User inputs story 2

adj3 = ['beautiful', 'breakable', 'meaningless']
noun3 = ['peak', 'jungle', 'beach']
verb2 = input("Enter a verb ending in 'ing': ")
print ("Select a place: ")
print ('Select an adjective')
for i,adjective in enumerate(adj3):
    print(i+1, adjective)
chosen=input('')
while not chosen.isnumeric() or int(chosen)>len(adj3):
        chosen = input("invalid data: ")
adjective=adj3[int(chosen)-1]
adj4 = input("Enter an adjective: ")
verb3 = input("Enter a verb: ")
noun6 = input("Enter a noun: ")
verb4 = input("Enter a verb ending in 'ing': ")

while not verb.endswith('ing'):
        verb = input("invalid data: ")

verb5 = input("Enter a verb ending in 'ing': ")

while not verb.endswith('ing'):
        verb = input("invalid data: ")

verb6 = input("Enter a verb ending in 'ing': ")

while not verb.endswith('ing'):
        verb = input("invalid data: ")

verb7 = input("Enter a verb ending in 'ing': ")

while not verb.endswith('ing'):
        verb = input("invalid data: ")

adj5 = input("Enter an adjective: ")
verb8 = input("Enter a verb: ")

# Print story 2

print('\nTitle: Taking the Train')
print('\n')
time.sleep(3)
print("I love " + verb2 + " on a train from my " + noun3 + " to the " + adj3 + " city.")
time.sleep(3)
print("Trains are " + adj4 + " because they " + verb3 + " on special rails made of " + noun6 + " instead of roads.")
time.sleep(3)
print("It's fun " + verb4 + " for the train and " + verb5 + " the sound as the train arrives.")
time.sleep(3)
print("While " + verb6 + " on the train, I like to look out the window and see the countryside, passing valleys ")
print("and " + verb7 + " villages and " + adj5 + " mountains as we " + verb8  + " past.")
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

# User inputs story 3

color2 = ['purple', 'yellow', 'black']
noun12 = ['December', 'August', 'October']
print("Select the name of a month ")
verb9 = input("Enter a verb: ")
adj6 = input("Enter an adjective: ")
adj7 = input("Enter an adjective: ")
noun15 = input("Enter the name of a place: ")
verb11 = input("Enter a verb: ")
noun17 = input("Enter a noun: ")
adj8 = input("Enter an adjective: ")
adj9 = input("Enter an adjective: ")
print("Select a color ")
adj10 = input("Enter an adjective: ")
verb12 = input("Enter a verb: ")
verb13 = input("Enter a verb: ")
noun18 = input("Enter a noun: ")

# Print story 3

print('\nTitle: Christmas Tree')
print('\n')
time.sleep(3)
print("Every " + noun12 + " we " + verb9 + " to a tree farm far away.")
time.sleep(3)
print("Not just any " + adj6 + " farm, a " + adj7 + " tree farm.")
time.sleep(3)
print("My dad and I go onto the " + noun15 + " to " + verb11 + " for the perfect " + noun17 + ".")
time.sleep(3)
print("Some people like them " + adj8 + " and " + adj9 + " and some like them " + color2 + " and fat.")
time.sleep(3)
print("We are searching for a tall and " + adj10 + " one!")
time.sleep(3)
print("Then I finally see it. Off we " + verb12 + " saw in hand to " + verb13 + " this year's " + noun18 + " down.")
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

# User inputs story 4

adj11 = ['salty', 'dirty', 'noisy']
verb14 = ['jump', 'meet', 'send']
adj12 = input("Enter an adjective: ")
noun19 = input("Enter a month: ")
print("Select an adjective: ")
verb15 = input("Enter a verb ending in 'ing': ")

while not verb.endswith('ing'):
        verb = input("invalid data: ")

adj13 = input("Enter an adjective: ")
verb16 = input("Enter a verb ending in 'ing': ")

while not verb.endswith('ing'):
        verb = input("invalid data: ")

adj14 = input("Enter an adjective: ")
adj15 = input("Enter an adjective: ")
adj16 = input("Enter an adjective: ")
print("Select a verb: ")
adj17 = input("Enter an adjective: ")
verb18 = input("Enter a verb: ")
verb19 = input("Enter a verb ending in 'ing': ")

while not verb.endswith('ing'):
        verb = input("invalid data: ")
        
noun20 = input("Enter a noun: ")

# print story 4

print('\nTitle: My Favorite Weather')
print('\n')
time.sleep(3)
print("My " + adj12 + " weather is during the month of " + noun19 + " when it's " + adj11 + " outside and everyone is " + verb15 + " and having a " + adj13 + " time.")
time.sleep(3)
print("The sun is " + verb16 + " and bright, and the people wear " + adj14 + " clothes to stay " + adj15 + ".")
time.sleep(3)
print("Many people " + verb14 + " on vacation in this weather.")
time.sleep(3)
print("It's a " + adj17 + " time to " + verb18 + " things like go " + verb19 + " at a " + noun20 + " or to explore new places.")
time.sleep(3)
print("What's your type of weather?")

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
