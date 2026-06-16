import random
user1 = input("what card would you like to pull? (workout)\n")
user2 = input("what card would you like to pull? (2)\n")
user3 = input("what card would you like to pull? (3)\n")
user4 = input("what card would you like to pull? (4)\n")

cards = [user1, user2, user3, user4]

full_w = [2,3,4,5,6,7,8,9,10, "wild card(15)"]

min_w = [5, 10, 7, 3]

stretches = ["Arms", "Back", "Legs", "Stomach", ]

w = 0
s = 0

def stretch():
    strch = random.sample(stretches, 1)
    return(f"Stretch your {strch} for 10 seconds")


def workout():
    card = random.sample(cards, 1)
    rep = random.sample(full_w, 1)
    return(f"do {card} {rep} times")

def min_workout():
    card = random.sample(cards, 1)
    rep = random.sample(min_w, 1)
    return(f"do {card} {rep} times")

print("Stretch or Workout first? s/w")
first_in = input()

if first_in == "s":

    while s < 8:
        print("Ready? y/n")
        s_in = input()

        if s_in == "y":
            print(stretch())
            s += 1
        else:
            print("goodbye")
            break
        
        if s == 8:
                print("Moving on to the workout..\n")
                def routine():
                   print("Full workout or min? f/m")
                   full_min = input()
                   if full_min == "f":
                       while w < 50:
                           print("Draw y/n")
                           workout_in = input()
                           if workout_in == "y":
                               print(workout())
                               w += 1
                           else:
                               print("Seems to be a problem")
                               break
                   elif full_min == "m":
                       while w < 20:
                           print("Draw y/n")
                           min_in = input()
                           if min_in == "y":
                               print(min_workout())
                               w += 1
                           else:
                               print("There seems to be a problem")
                               break
                   else:
                        print("There seems to be a problem")
                        full_min()

if first_in == "w":
    routine()