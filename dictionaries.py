# NORTH METROPOLITAN TAFE
# DIPLOMA IN INFORMATION TECHNOLOGY (ADVANCED NETWORKING)
# ICTPRG443 - APPLY INTERMEDIATE PROGRAMMING

# STUDENT: ALEXANDER THIEN (20093897@tafe.wa.edu.au)
# ASSESSMENT 2: PART B - DICTIONARIES
# This is the first part of the program which is responsible for manipulation of dictionaries using operations.

#   v0.1    2024/08/19  Basic definitions of functions in pseudocode, populated lists with some entries.
#   v0.2    2024/10/02  Functions converted to working code, added lines to support unittest.

print("ICTPRG443 - Apply Intermediate Programming Skills in Different Languages")
print("Assessment 2 - Part B: Dictionaries")

actorsDOB = {
    "Tom Hanks" : "09/07/1956" , 
    "Morgan Freeman" : "01/06/1937" , 
    "Johnny Depp" : "09/06/1963" , 
    "Harrison Ford" : "13/07/1942" , 
    "Hugh Jackman" : "12/10/1968" , 
    "Bruce Lee" : "27/11/1940" , 
    "Jim Carrey" : "17/01/1962" , 
    "Scarlett Johansson" : "22/11/1984" , 
    "Anne Hathaway" : "12/11/1982" , 
    "Emma Stone" : "06/11/1988" , 
    "Julie Andrews" : "01/10/1935" , 
    "Margot Robbie" : "02/07/1990"
}

moviesYear = {
    "Forrest Gump" : "1994" , 
    "The Shawshank Redemption" : "1995" , 
    "Rango" : "2011" , 
    "Indiana Jones and the Temple of Doom" : "1984" , 
    "Logan" : "2017" , 
    "Enter the Dragon" : "1973" , 
    "The Mask" : "1994" , 
    "The Island" : "2005" , 
    "Interstellar" : "2014" , 
    "Poor Things" : "2024" , 
    "The Sound of Music" : "1965" , 
    "The Wolf of Wall Street" : "2013"
}

gamesYear = {
    "Space Invaders" : "1978" , 
    "Asteroids" : "1979" , 
    "Ghosts and Goblins" : "1985" , 
    "Arkanoid" : "1986" , 
    "Wing Commander" : "1990" , 
    "Street Fighter 2" : "1991" , 
    "Ridge Racer" : "1993" , 
    "Fallout" : "1997" , 
    "Half-Life" : "1998" , 
    "System Shock 2" : "1999" , 
    "Battlefield 1942" : "2002" , 
    "Warcraft 3: Reign of Chaos" : "2002"
}
# Functions


# Add Value
def add_item(dictionary, key, value):
    """Takes the dictionary, the key, and the value before adding the entry to the dictionary."""
    dictionary[key] = value
    return dictionary

# Delete Value
def remove_item(dictionary, key):
    """Deletes an entry from the dictionary if a matching key is found."""
    if key in dictionary:
        del dictionary[key]
    return dictionary

#   Sort dictionary elements in ascending order
def sort_ascending(dictionary):
    """Takes the dictionary and its keys to arrange the entries in key ascending order."""
    return dict(sorted(dictionary.items()))

# Sort Descending
#   Sort dictionary elements in descending order
def sort_descending(dictionary):
    """Takes the dictionary and its keys to arrange the entries in key descending order."""
    return dict(sorted(dictionary.items(), reverse=True))

# Search dictionary for value
def search_dictionary(dictionary, value):
    """Takes the dictionary and its values to check if the entry is in the dictionary. Valid queries are returned."""
    if value in dictionary.values():
        return True
    else:
        return False


# Main Menu
def main_menu():
    print("1. Actors")
    print("2. Movies")
    print("3. Games")
    print("4. Exit")


# Sub Menu
def sub_menu():
    print("1. Add an entry to the dictionary.")
    print("2. Delete an entry from the dictionary.")
    print("3. Sort the dictionary in ascending order.")
    print("4. Sort the dictionary in descending order.")
    print("5. Search for an entry in the dictionary.")
    print("6. Go back to the main menu.")


# Actors
print("Actors:", actorsDOB)
# Movies
print("Movies:", moviesYear)
# Games
print("Games:", gamesYear, end='\n\n')



# Main Program
def play():
    while True:
        print("Welcome to the main menu!")
    
        # Calls the main menu function and informs the user of options.
        main_menu()
    
        option = input("Please enter a number that corresponds to the desired dictionary. (must be between 1 and 4): ")
    
        if option == "1":
            chosen_dict = actorsDOB
        elif option == "2":
            chosen_dict = moviesYear
        elif option == "3":
            chosen_dict = gamesYear
        elif option == "4":
            break
        else:
            print("Invalid choice! Please try again with a valid number.", end='\n\n')
            continue
    
        while True:
            sub_menu()
            sub_option = input("Please select the operation you wish to perform. (must be between 1 and 6): ")
    
            if sub_option == "1":
                key = input("Enter the key to add: ")
                value = input("Enter the value to add: ")
                add_item(chosen_dict, key, value)
                print("This is the dictionary after adding your key and value:", chosen_dict, end='\n\n')
            elif sub_option == "2":
                key = input("Enter the key you wish to delete: ")
                remove_item(chosen_dict, key)
                print("This is the dictionary after deleting your requested item:", chosen_dict, end='\n\n')
            elif sub_option == "3":
                chosen_dict = sort_ascending(chosen_dict)
                print("This is the dictionary after sorting by key values in ascending order:", chosen_dict, end='\n\n')
            elif sub_option == "4":
                chosen_dict = sort_descending(chosen_dict)
                print("This is the dictionary after sorting by key values in descending order:", chosen_dict, end='\n\n')
            elif sub_option == "5":
                value = input("Enter the value to search for: ")
                if search_dictionary(chosen_dict, value):
                    print("The entry is present in the dictionary.", end='\n\n')
                else:
                    print("The entry is not present in the dictionary.", end='\n\n')
            elif sub_option == "6":
                break
            else:
                print("Invalid choice! Please try again with a valid input.", end='\n\n')

if __name__ == "__main__":
    play()