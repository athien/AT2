# NORTH METROPOLITAN TAFE
# DIPLOMA IN INFORMATION TECHNOLOGY (ADVANCED NETWORKING)
# ICTPRG443 - APPLY INTERMEDIATE PROGRAMMING

# STUDENT: ALEXANDER THIEN (20093897@tafe.wa.edu.au)
# ASSESSMENT 2: PART B - DICTIONARIES (TEST)
# This is the second part of the program which is responsible for testing the operations of the main program.

#   v0.1    2024/08/19  Basic definitions of functions in pseudocode, populated lists with some entries.
#   v0.2    2024/10/02  Functions converted to working code, added lines to support unittest.

# Import unittest framework
import unittest

# Import functions from the main dictionaries program file
from dictionaries import add_item, remove_item, sort_ascending, sort_descending, search_dictionary, actorsDOB

# Test Scenarios for the dictionary functions
class TestDictionaries(unittest.TestCase):
    
    def test_add_item(self):
        """Tests the functionality of the add_item() operation."""
        test_dict = {}
        result = add_item(test_dict, "Anne Hathaway", "12/11/1982")
        self.assertEqual(test_dict, result)
    
    def test_remove_item(self):
        """Tests the functionality of the remove_item() operation."""
        test_dict = {"Anne Hathaway" : "12/11/1982" , "Bruce Lee" : "27/11/1940" , "Emma Stone" : "06/11/1988"}
        remove_item(test_dict, "Bruce Lee")
        result = {"Anne Hathaway" : "12/11/1982" , "Emma Stone" : "06/11/1988"}
        self.assertEqual(test_dict, result)
    
    def test_sort_ascending(self):
        """Tests the functionality of the sort_ascending() operation."""
        test_dict = {"Rango" : "2011" , "Logan" : "2017" , "Interstellar" : "2014"}
        result = sort_ascending(test_dict)
        self.assertEqual(result, test_dict)
    
    def test_sort_descending(self):
        """Tests the functionality of the sort_descending() operation."""
        sortedActors = sort_descending(actorsDOB)
        self.assertEqual(sortedActors, actorsDOB)
    
    def test_search_dictionary(self):
        """Tests the functionality of the search_dictionary() operation."""
        
        self.assertTrue(search_dictionary(actorsDOB, "13/07/1942"))
        self.assertFalse(search_dictionary(actorsDOB, "Julie Andrews"))

if __name__ == '__main__':
    unittest.main()