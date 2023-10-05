#Work it
#Make it
#Do it
#Makes us
#Harder
#Better
#Faster
#Stronger

#importing stuff and setting variables
import random
level = 1

possible_beast_types = ["bear","max_harrison"]
#in the actual game Beast level will be decided by what kind of beast we have attacking us. 
Beast_Body = ["torso","leg","arm","head"]

print("a level",level ,random.choice(possible_beast_types), "has appeared")

#assigning the values
max_harrison = {
'attack_chance': random.randint(0, 1),
'health': 10*level,
'attack': 10*level
}

bear = {
'attack_chance': random.randint(0, 1),
'health': 10*level,
'attack': 5*level
}

print(max_harrison["attack_chance"])