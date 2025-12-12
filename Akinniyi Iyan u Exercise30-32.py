#Exercise 30 Comparison between Dogs, Cats and people

people = 20
cats = 30
dogs = 15

if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The World is Saved")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry")            

dogs += 5 

if people >= dogs:
    print("People are greater than or equal to dogs")

if people <= dogs:
    print("People are less than or equal to dogs")

if people == dogs:
    print("People are dogs")

#Exercise 31 if, elif and esleif comparisons

people = 30
cars = 40 
trucks = 15

if cars > people:
    print("We shouls take the cars")

elif cars < people:
    print("We should not take the cars")

else:
    print("We can't decide")   

if trucks > cars:
    print("That's to many trucks")

elif trucks < cars:
    print("Maybe we could take the trucks")

else:
    print("We still can't decide")   


if people > trucks:
    print("Alright let's just take the trucks.")

else:
    print("Fine, let's stay home then")

#Exercise 32 Decison making in a scary place

print("""You enter a dark room with two doors
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("There is a giant bear here eating a cheese cake")
    print("What do you do?")
    print("1. Take the cake")
    print("2. Scream at teh bear")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good Job!")

    elif bear == "2":
        print("The bear eats your legs off. Good Job!")

    else:
        print(f"well doing {bear} is probably better")        
    print("bear runs away")        

elif door == "2":
    print("You stare into the endless abyss at cthulhu")
    print("1. Blueberries")
    print("2. Yellow jacket clothespins")
    print("3. Understanding revolvers yelling melodies")  

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powere by a mind of it's own")
        print("Good Job!")

    else:
        print("The insanity rots your eyes into a pool of goo")
        print("Good Job!")        

else:
    print("You stumble around and fall on a knife and die")        