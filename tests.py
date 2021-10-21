import unittest
from main import List_of_objects_routes, Route, func1, func2

class TestStringMethods(unittest.TestCase):

    def test_sort(self):
        newlist = sorted(List_of_objects_routes, key=lambda x: x.distance, reverse=False)
        self.assertEqual(newlist[0].distance, 131)

    def test_func1(self):
        self.assertEqual(func1(List_of_objects_routes, 1000), 10)

    def test_func1_2(self):
        self.assertEqual(func1(List_of_objects_routes, 100), 6)





if __name__ == '__main__':
    unittest.main()