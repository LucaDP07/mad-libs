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

# User inputs story 1
name = input("Enter your name: ")

age = input("Enter your age: ")
while not age.isnumeric():
        age = input("Enter your age, should be a number: ")

adj= ['perfect', 'rough', 'gentle']
print ('Select an adjective: ')
for i,adj in enumerate(adj):
        print(i+1, adj)
chosen=input('')
while not chosen.isnumeric() or int(chosen)>len(adj):
        chosen = input("Invalid data: Select an adjective")
aj=adj[int(chosen)-1]

color = ['red', 'blue', 'green']
print ('Select a color')
for i,color in enumerate(color):
        print(i+1, color)
chosen=input('')
while not chosen.isnumeric() or int(chosen)>len(color):
        chosen = input('Invalid data: Select a color')
colors=color[int(chosen)-1]

noun= ['car', 'money', 'banana']
print('Select a noun: ')
for i,noun in enumerate(noun):
        print(i+1, noun)
chosen=input('')
while not chosen.isnumeric() or int(chosen)>len(noun):
        chosen = input('Invalid data: Select a noun')
nn=noun[int(chosen)-1]

verb= ['running', 'starving', 'loving']
print('Select a verb: ')
for i,verb in enumerate(verb):
        print(i+1, verb)
chosen=input('')
while not chosen.isnumeric() or int(chosen)>len(verb):
        chosen = input('Invalid data: Select a verb')
ver=verb[int(chosen)-1]

clothings = ['socks', 'pajamas', 'skirt']
print ('Select your clothing')
for i,clothings in enumerate(clothings):
        print(i+1, clothings)
chosen=input('')
while not chosen.isnumeric() or int(chosen)>len(clothings):
        chosen = input('Invalid data: ')
cloth=clothings[int(chosen)-1]

second_adj= ['angry', 'able', 'busy']
print('Select an adjective: ')
for i,second_adj in enumerate(second_adj):
        print(i+1, second_adj)
chosen=input('')
while not chosen.isnumeric() or int(chosen)>len(second_adj):
        chosen = input('Invalid data: Select an adjective: ')
adj=second_adj[int(chosen)-1]

celebrity= ['Ryan Reynolds', 'Emma Stone', 'Tom Hanks']
print('Select a celebrity: ')
for i,celebrity in enumerate(celebrity):
        print(i+1, celebrity)
chosen=input('')
while not chosen.isnumeric() or int(chosen)>len(celebrity):
        chosen = input('Invalid data: Select a celebrity: ')
cel=celebrity[int(chosen)-1]

number = input('Enter a number: ')
while not number.isnumeric():
        number = input('Enter a number, should be a number: ')

friend = input('Enter the name of a friend: ')
while not friend.isalpha():
        friend = input('Invalida data: Enter a name: ')

second_noun = ['wood', 'ukelele', 'smoothie']
print('Select a noun: ')
for i,second_noun in enumerate(second_noun):
        print(i+1, second_noun)
chosen=input('')
while not chosen.isnumeric() or int(chosen)>len(second_noun):
        chosen = input('Invalid data: Select a noun: ')
nn=second_noun[int(chosen)-1]

second_friend = input('Enter the name of another friend: ')
while not second_friend.isalpha():
        second_friend = input('Invalida data: Enter a name: ')
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
print("I would wear a/an " + clothings + " on my head, and everyone would say I look " + second_adj + " like " + celebrity + ".")
time.sleep(3)
print("School would be open only " + number + " days a year.")
time.sleep(3)
print("I would give my friends the best jobs.")
time.sleep(3)
print("I would nominate " + friend + " to be secretary of the " + second_noun + ",")
print("and " + second_friend + " could be vice president !")
time.sleep(3)
play = input("Play again?")