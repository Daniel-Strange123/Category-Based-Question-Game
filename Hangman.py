import random


scores = 0

Categories = {
    'animals': {
        'Meerkat': "I'm a 7 letter word and i am a Lion king star",
        'Mammoth': "I used to be the ancestors of Elephants",
        'Puma': "Four letter word and i belong to the cat family",
        'Ostrich':"I'm the tallest bird",
    },

    'fruits':{
        'Banana': "I am a long, yellow fruit that you have to peel before eating.",
        'Watermelon': "I am a massive summer fruit with a hard green shell and sweet pink flesh.",
        'Apple': "I belong to the rose family of plants, and 25% of my volume is just trapped air.",
        'Strawberry': "I am technically not a true berry, and I am the only fruit that carries its seeds on the outside."
},

    'country' : {
        'Egypt': "I am a desert country famous for the ancient Sphinx and giant stone pyramids.",
        'Japan': "I am an island nation famous for Tokyo, anime, and cherry blossom trees.",
        'Canada': "I have the longest coastline in the entire world and contain over half of the planet's lakes.",
        'Brazil': "I am a massive nation that shares a border with every country on my continent except for two."
},
    
}

Category = list(Categories.keys())

name = input("What is your name?")
print(f"Alright {name},pick a category.\n The categories involved are animals, fruits and country category.\n Just write animals, fruits or country.")





while True:
    while True:
        choice = input("Enter category: ").strip().lower()
        if choice in Categories:
            chosen_category = Categories[choice]
            break
        else:
            print("❌ Invalid choice. Please choose from either animals, fruits, or country.\n")
            continue 



    answer = random.choice(list(chosen_category.keys()))
    clue = chosen_category[answer]
    print("\nYour clue is:")
    print(clue)



    guess = input(f"what is your guess {name}  ")
    if guess.casefold() == answer.casefold():
        print("That is valid!!!!")
        scores += 1
    else:
        print(f"Nope, the answer is {answer}")
        scores -= 1    


    play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()

    if play_again not in ("yes", "y"):
        print(f"\nThanks for playing, {name}!")
        print(f"Your final score is: {scores}")
        break  

