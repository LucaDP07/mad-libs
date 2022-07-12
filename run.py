

print("Welcome to the Mad Libs Game")

playing = input("Let's play, shall we?\n")

answer = "okay"

while answer not in ["Yes", "yes", "Y", "y", "No", "no", "N", "n"]: 
    answer = input("Invalid data. Ready to start? Yes or No\n") 

if answer=="Yes" or answer=="yes" or answer=="Y" or answer=="y": 
        print("Ok, let's play the game: \n")
        
elif answer=="No" or answer=="no" or answer=="N" or answer=="n": 
        print("That's fine. See you soon\n") 
        quit()
else: 
        print("Please type Yes or No\n") 

print('\nTitle: If I were president')
print('\n')
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

# Print story #1

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
play = input('Play again? Y/N')


print('\nTitle: Taking the Train')
print('\n')
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

print(f"""
    I love {verb} on a train from my {noun} to the {adj city}.
    Trains are {adj} because they {verb2} on special {noun2} made of {noun3} instead of roads.
    It's fun {verb3} for the train and {verb4} the {noun4} sound as the train arrives.
    While {verb5} on the train, I like to look out the {noun5} and see the countryside, passing {noun6}
    and {verb6} {noun7} and {adj3} {noun8} as we {verb7} past. 

    """)

play = input('Play again? Y/N')


print('\nTitle: Christmas Tree')
print('\n')
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
exclamation = input('Enter an exclamation')

# Print story #3

print(f"""
    Every {noun} we {verb} to a tree {noun2} far away.
    Not just any {adj} farm, a {adj2} tree {noun3}.
    My dad and I {verb2} onto the {noun4} to {verb3} for the perfect {noun4}. 
    Some people like them {adj2} and {adj3} and some like them {color} and fat. 
    We are searching for a tall and {adj4} one!
    "Over there!" I exclaim, "dad, it's over there!" Off we {verb4} saw in hand to {verb5} this year's {noun6} down. 
    {exclamation} it's Christmas finally!

    """)

play = input('Play again? Y/N')


print('\nTitle: My Favorite Weather')
print('\n')
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

print(f"""
  My {adj} weather is during the month of {noun} when it's {adj2} outside and everyone is {verb} and having a {adj3} time. 
  The sun is {verb2} and {adj4}, and the people wear {adj5} clothes to stay {adj6}.
  Many people {verb3} on vacation in this weather. 
  It's a {adj7} time to {verb4} things like go {verb5} at a {noun2} or to explore {adj8} places. 
  What's your {adj8} type of {noun3}?

    """)

















