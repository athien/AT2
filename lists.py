# NORTH METROPOLITAN TAFE
# DIPLOMA IN INFORMATION TECHNOLOGY (ADVANCED NETWORKING)
# ICTPRG443 - APPLY INTERMEDIATE PROGRAMMING

# STUDENT: ALEXANDER THIEN (20093897@tafe.wa.edu.au)
# ASSESSMENT 2: PART A - LISTS
# This is the first part of the program which is responsible for manipulation of lists using operations.

#   v0.1    2024/08/19  Basic definitions of functions in pseudocode, populated lists with some entries.
#   v0.2    2024/10/02  Functions converted to working code, added lines to support unittest.

print("ICTPRG443 - Apply Intermediate Programming Skills in Different Languages")
print("Assessment 2 - Part A: Lists")

# LISTS
actors = ["Tom Hanks", "Morgan Freeman", "Johnny Depp", "Harrison Ford", "Hugh Jackman", "Bruce Lee", "Jim Carrey", "Scarlett Johansson", "Anne Hathaway", "Emma Stone", "Julie Andrews", "Margot Robbie"]
movies = ["Forrest Gump", "The Shawshank Redemption", "Rango", "Indiana Jones and the Temple of Doom", "Logan", "Enter the Dragon", "The Mask", "The Island", "Interstellar", "Poor Things", "The Sound of Music", "The Wolf of Wall Street"]
games = ["Space Invaders", "Asteroids", "Ghosts and Goblins", "Arkanoid", "Wing Commander", "Street Fighter 2", "Ridge Racer", "Fallout", "Half-Life", "System Shock 2", "Battlefield 1942", "Warcraft 3: Reign of Chaos"]

# Add a new element to the chosen list using the append method.
def append_element(list, element):
    """Checks list if element is present and adds it."""
    if element not in list:
        list.append(element)
    return list

# Removes an existing element from the chosen list using the remove method.
def remove_element(list, element):
    """Removes requested element from list if it is present."""
    if element in list:
        list.remove(element)
    return list

# Sort the lists in ascending dictionary order.
def sort_ascending(list):
    """Sorts the list in ascending dictionary order."""
    list.sort()
    return list

# Sort the lists in descending dictionary order.
def sort_descending(list):
    """Sorts the list in descending dictionary order."""
    list.sort(reverse=True)
    return list

def search(list, element):
    """Searches the list for a specific element and returns the result."""
    if element in list:
        return True
    else:
        return False

# Selection menu for the main screen
def main_menu():
    print("1. Actors")
    print("2. Movies")
    print("3. Games")
    print("4. Exit")

# Submenu selection for list modification
def sub_menu():
    print("1. Add a new entry to the list.")
    print("2. Delete an existing entry from the list.")
    print("3. Sort the list in ascending dictionary order.")
    print("4. Sort the list in descending dictionary order.")
    print("5. Check list for requested entry.")
    print("6. Return to the main menu.")

# Main Program

print("My favourite actors are:", actors)
print("My favourite movies are:", movies)
print("My favourite games are:", games)

def play():     
    while True:
        print("Welcome to the main menu.")
        
        # Call the main_menu() function and invite the user to input their choice.
        main_menu()
        
        option = input("Please select a list to continue or quit the program. (enter a number between 1 and 4): ")
        
        if option == "1":
            chosen_list = actors
        elif option == "2":
            chosen_list = movies
        elif option == "3":
            chosen_list = games
        elif option == "4":
            break
        else:
            print("Invalid input. Please enter a number between one and four.")
            continue
        
        # Call the sub_menu() function and invite the user to input their chosen operation.
        while True:
            sub_menu()
            sub_option = input("Please enter the operation you want to perform (enter a number between 1 and 6): ")
            
            if sub_option == "1":
                value = input("Enter the value to be added to the list: ")
                append_element(chosen_list, value)
                print("The list has been updated with the addition:", chosen_list, end='\n\n')
            elif sub_option == "2":
                value = input("Enter the value to be removed from the list: ")
                remove_element(chosen_list, value)
                print("The list has been updated with the removal: ", chosen_list, end='\n\n')
            elif sub_option == "3":
                sort_ascending(chosen_list)
                print("The list has been sorted in ascending dictionary order: ", chosen_list, end='\n\n')
            elif sub_option == "4":
                sort_descending(chosen_list)
                print("The list has been sorted in descending dictionary order: ", chosen_list, end='\n\n')
            elif sub_option == "5":
                value = input("What entry do you wish to search the list for? ")
                if search(chosen_list, value):
                    print("The searched entry is present in the list.", end='\n\n')
                else:
                    print("The searched entry is not present in the list.", end='\n\n')
            elif sub_option == "6":
                break
            else:
                print("Invalid choice, please try again.", end='\n\n')

if __name__ == "__main__":
    play()
