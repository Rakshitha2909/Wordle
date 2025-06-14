# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 15:30:26 2025

@author: mnikh
"""


import random

guess=['Apple', 'Angle', 'Admit', 'Arena', 'Alien', 'Angry', 'Ample', 'Agile', 'Awake', 'Asset',
       "beach", "blaze", "break", "brick", "brain", "bench", "bloom", "brave", "bound", "blast",
       "catch", "clear", "climb", "clock", "chase", "crisp", "clean", "crash", "clamp", "clash",
       "dance", "drive", "drown", "drain", "depth", "dream", "doubt", "dashy", "donut", "dared",
       "eagle", "empty", "enter", "earth", "event", "enjoy", "elbow", "examine", "entry","equip",
       "field", "fancy", "flash", "frank", "flood", "fight", "focus", "funny", "frown", "faint",
       "grape", "grasp", "glove", "goose", "gloom", "grill", "gains", "giddy", "glory", "grind",
       "house", "heart", "hatch", "haste", "hello", "honey", "hover", "humid", "hollow", "hefty",
       "image", "inner", "input", "issue", "ivory", "icons", "impose", "incur", "itchy", "intro",
       "jumpy", "jolly", "jewel", "joint", "juice", "judge", "jiffy", "jumpy", "jocks", "jumpy",
       "knife", "kicks", "knee", "knack", "karma", "kinky", "knead", "knoll", "known", "kited",
       "liver", "lapse", "lunar", "lemon", "latch", "liver", "lobby", "lumpy", "lunar", "laugh",
       "magic", "mango", "march", "mighty", "motel", "mouse", "motel", "manic", "mount", "melon",
       "night", "noble", "nacho", "nifty", "nurse", "noisy", "noble", "nerdy", "naive", "newly"
       "ocean", "open", "onion", "oiled", "other", "oddly", "overt", "oaths", "outgo", "offed",
       "place", "plant", "pearl", "plaza", "piano", "pitch", "party", "proud", "prong", "plumb",
       "queen", "quick", "quiet", "quilt", "query", "quota", "quail", "quake", "qualm", "quest",
       "round", "reach", "rival", "roast", "rally", "rider", "rider", "ruler", "rainy", "roper",
       "shine", "stack", "swoop", "silly", "stone", "sweet", "spike", "storm", "shaky", "slink",
       "taste", "tiger", "tweak", "thank", "tango", "twist", "track", "trump", "thorn", "tenth",
       "under", "ultra", "unite", "usage", "untie", "usual", "unzip", "udder", "untie", "usher",
       "vivid", "vocal", "vapor", "vigor", "vials", "vixen", "vowel", "value", "vexed", "venue",
       "waste", "watch", "waste", "whale", "whisk", "worse", "wage", "wreak", "woman", "wiper",
       "xenon", "xenon", "xpects", "xylem", "xylol", "xerox", "xenic", "xenon", "xitus", "xenon",
       "young", "youth", "yield", "yahoo", "yikes", "yummy", "yacht", "yells", "yarns", "yucky",
       "zebra", "zesty", "zonal", "zippy", "zoned", "zoom", "zeals", "zoned", "zeroes", "zebra"
    ]


    
    
secret=random.choice(guess)
#print(secret)

def guessgame(user_guess):
    if(user_guess in guess ):
        print(f"{user_guess} is present 😊")
        if(secret==user_guess):
            return True
        else:
            return False
            
            
    return False

def five(user_guess):
    if(len(user_guess)==5):
        return True
    else:
        return False

def feedback():
    secretl=list(secret)
    guessl=list(user_guess)
    for i in range(len(guessl)):
        if(guessl[i] in secretl):
            if(guessl[i]==secretl[i]):
                print(f"-{guessl[i]} (correct) 💚")
            else:
                print(f"-{guessl[i]} (present but misplaced) 💛")
        else:
            print(f"-{guessl[i]} (incorrect) 🤍")
            

print("👋😊 Welcome to Wordle 🌟")  
print("You have 6 chances to guess the 5 letter word 🎰 🍀 🎯")
chance=1
#print(f"Chance: {chance}")
user_guess=input("Enter a 5 letter word: ")

while(chance<6):
    
    if(five(user_guess)):
        
        if(guessgame(user_guess)):
            print("🎉🎊👏 Congratulations 🏆🥳 ")
            print(f"Guess: {chance} Feedback for {user_guess} 📝: ")
            feedback()
            break
        else:
            print("Your guess is wrong ❌")
            
            print("Number of chances left: ",6-chance)
            print(f"Guess: {chance} Feedback for {user_guess} 📝: ")
            feedback()
            user_guess=input("Enter a 5 letter word: ")
            chance+=1
            
    else:
        print("Input is improper")
        print("Number of chances left: ",6-chance)
        user_guess=input("Enter a 5 letter word: ")
    
else:
    print("You are out of chances:( Better luck next time!!! ")
    print(f"The word is {secret}")
    
    
        
   

    
                
    