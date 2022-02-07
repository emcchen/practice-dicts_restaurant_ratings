"""Restaurant rating lister."""

#initialize empty dictionary
ratings = {}

#read ratings in from txt file
file = open("scores.txt")

#store in dictionary
for line in file:
    #split line at colon to get restaurant & rating
    lines = line.strip().split(":")
    restaurant = lines[0]
    rating = lines[1]

    ratings[restaurant] = int(rating)

#Spit out ratings in alphabetical order
for restaurant, rating in sorted(ratings.items()):
    print(f"{restaurant} is rated at {rating}.")

def add_ratings():
    """Prompts user for a new restaurant and rating"""
    new_restaurant = input("Restaurant name? ")
    new_score = input("Restaurant score? ")
    ratings[new_restaurant] = new_score

    for restaurant, rating in sorted(ratings.items()):
        print(f"{restaurant} is rated at {rating}.")
