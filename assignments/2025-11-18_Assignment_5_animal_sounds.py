'''
1.	Write a program to print the lyrics of the song "Old MacDonald." Your program should print the lyrics for five different animals, similar to the example verse below. 
Old MacDonald had a farm, Ee-igh, Ee-igh, Oh! 
And on that farm he had a cow, Ee-igh, Ee-igh, Oh! With a moo, moo here and a moo, moo there. 
Here a moo, there a moo, everywhere a moo, moo. 
Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!
Hints:
•	print()
•	animal list[ ]
•	for loop


'''

# create the list of animals and their sounds
animal_list = [
    ["cow", "moo"],
    ["pig", "ooink"],
    ["sheep", "baaa"],
    ["horse", "whinny"],
    ["duck", "quack"]
]

print("This program print the lyrics of the song 'Old MacDonald' with five different animal sounds.")
print("Developed by Htet Khant Linn.")
print("------------------------------\n")

def main():
    # loop through each animal in the list
    for animal in animal_list:
        name = animal[0] # get the animal name
        sound = animal[1] # get the animal sound
        
        # print the song
        print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")
        print(f"And on that farm he had a {name}, Ee-igh, Ee-igh, Oh!")
        print(f"With a {sound}, {sound} here and a {sound}, {sound} there.")
        print(f"Here a {sound}, there a {sound}, everywhere a {sound}, {sound}.")
        print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")
        print("")

if __name__ == "__main__":
    main()