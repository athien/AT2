# NORTH METROPOLITAN TAFE
# DIPLOMA IN INFORMATION TECHNOLOGY (ADVANCED NETWORKING)
# ICTPRG443 - APPLY INTERMEDIATE PROGRAMMING

# STUDENT: ALEXANDER THIEN (20093897@tafe.wa.edu.au)
# ASSESSMENT 2: PART A - LISTS (TEST)
# This is the second part of the program which is responsible for testing the operations of the main program.

#   v0.1    2024/08/19  Basic definitions of functions in pseudocode, populated lists with some entries.
#   v0.2    2024/10/02  Functions converted to working code, added lines to support unittest.

# Import the unittest program
import unittest

# Import functions from the main python lists program
from lists import append_element, remove_element, sort_ascending, sort_descending, search

# Test scenarios for lists functions
class TestLists(unittest.TestCase):
    
    def test_append_element(self):
        """Tests the functionality of the append_element() operation."""
        test_list = []
        result = append_element(test_list, "Margot Robbie")
        self.assertEqual(result, ["Margot Robbie"])
        self.assertEqual(test_list, ["Margot Robbit"])
    
    def test_remove_element(self):
        """Tests the functionality of the remove_element() operation."""
        test_list = ["Margot Robbie", "Julie Andrews", "Emma Stone"]
        result = remove_element(test_list, "Julie Andrews")
        self.assertEqual(result, ["Margot Robbie", "Emma Stone"])

    def test_sort_ascending(self):
        """Tests the functionality of the sort_ascending() operation."""
        test_list = ["Logan", "Rango", "Enter the Dragon"]
        result = sort_ascending(test_list)
        self.assertListEqual(result, test_list)

    def test_sort_descending(self):
        """Test the functionality of the sort_descending() operation."""
        test_list = ["Anne Hathaway", "Morgan Freeman", "Scarlett Johansson"]
        result = sort_descending(test_list)
        self.assertListEqual(result, ["Scarlett Johansson", "Morgan Freeman", "Anne Hathaway"])

    def test_search(self):
        """Tests the functionality of the search() operation."""
        test_list = ["Asteroids"]
        self.assertTrue(search(test_list, "Asteroids"))
        self.assertFalse(search(test_list, "Battletoads"))


if __name__ == '__main__':
    unittest.main()
