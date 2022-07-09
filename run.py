print("Welcome to the Mad Libs Game")

playing = input("Let's play, shall we\n")

answer = "okay"
while answer not in ["Yes", "yes", "Y", "y", "No", "no", "N", "n"]: 
    answer = input("Are you feeling good? Yes or No\n") 

if answer=="Yes" or answer=="yes" or answer=="Y" or answer=="y": 
        print("Ok, let's play the game: \n")
elif answer=="No" or answer=="no" or answer=="N" or answer=="n": 
        print("That's fine. See you soon\n") 
        quit()
else: 
        print("Please type Yes or No\n") 

    

# User inputs

noun = input("Enter your name: ")
number = input("Enter your age: ")
adj = input("Enter an adjective: ")
color = input("Enter a color: ")
noun2 = input("Enter a noun: ")
food = input("Enter a type of food(plural): ")
noun3 = input("Enter a noun: ")
verb = input("Enter a verb ending in 'ing': ")
clothing = input("Enter an article of clothing: ")
adj2 = input("Enter an adjective: ")
celebrity = input("Enter the name of a celebrity: ")
number2 = input("Enter a number: ")
noun4 = input("Enter the name of a friend: ")
noun5 = input("Enter a noun: ")
noun6= input("Enter the name of another friend: ")
occupation = input("Enter an occupation: ")

# Print story

print(f"""
    My name is {noun} and I'm {number} years old.
    If I were president, I'd do a whole bunch of {adj} things:
    I would drive the biggest {color} car in the country, and that
    car would go faster than any other {noun2} in the world!
    Everyone would eat pepperoni {food} for dinner.
    I would live in the Statue of {noun3} and build a {verb} pool at her feet.
    I would wear a/an {clothing} on my head, and everyone would say I look {adj2} like {celebrity}.
    School would be open only {number2} days a year.
    I would give my friends the best jobs.
    I would nominate {noun4} to be secretary of the {noun5},
    and {noun6} could be vice {occupation}!

    """)



