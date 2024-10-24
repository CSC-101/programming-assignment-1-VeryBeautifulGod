import data
import hw1
import unittest
from data import Price, Rectangle, Point, Book, Circle, Employee

# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_vowel_count_1(self):
        input_str = "AEIOUaeiou"
        result = hw1.vowel_count(input_str)
        expected = 10
        self.assertEqual(expected, result)

    def test_vowel_count_2(self):
        input_str = "bcdfghjkl"
        result = hw1.vowel_count(input_str)
        expected = 0
        self.assertEqual(expected, result)
    # Part 2
    def test_short_lists_1(self):
        input_list = [[1, 2], [3, 4, 5], [6, 7], [8]]
        result = hw1.short_lists(input_list)
        expected = [[1, 2], [6, 7]]
        self.assertEqual(expected, result)

    def test_short_lists_2(self):
        input_list = [[1, 2], [3, 4], [5, 6]]
        result = hw1.short_lists(input_list)
        expected = [[1, 2], [3, 4], [5, 6]]
        self.assertEqual(expected, result)

    # Part 3
    def test_ascending_pairs_1(self):
        input_list = [[3, 1], [5, 2], [7, 8, 9], [4, 4], [10, 5]]
        result = hw1.ascending_pairs(input_list)
        expected = [[1, 3], [2, 5], [7, 8, 9], [4, 4], [5, 10]]
        self.assertEqual(expected, result)

    def test_ascending_pairs_2(self):
        input_list = [[6, 2], [4, 4], [8, 3]]
        result = hw1.ascending_pairs(input_list)
        expected = [[2, 6], [4, 4], [3, 8]]
        self.assertEqual(expected, result)

    # Part 4
    def test_add_prices_1(self):
        price1 = Price(5, 75)
        price2 = Price(3, 50)
        result = hw1.add_prices(price1, price2)
        expected = Price(9, 25)
        self.assertEqual(expected, result)

    def test_add_prices_2(self):
        price1 = Price(2, 85)
        price2 = Price(3, 50)
        result = hw1.add_prices(price1, price2)
        expected = Price(6, 35)
        self.assertEqual(expected, result)

    # Part 5
    def test_rectangle_area_1(self):
        top_left = Point(1, 2)
        bottom_right = Point(5, 6)
        rect = Rectangle(top_left, bottom_right)
        result = hw1.rectangle_area(rect)
        expected = 16
        self.assertEqual(expected, result)

    def test_rectangle_area_2(self):
        top_left = Point(-3, -2)
        bottom_right = Point(1, 2)
        rect = Rectangle(top_left, bottom_right)
        result = hw1.rectangle_area(rect)
        expected = 16
        self.assertEqual(expected, result)

    # Part 6
    def test_books_by_author_1(self):
        book1 = Book(["F. Scott Fitzgerald"], "The Great Gatsby")
        book2 = Book(["George Orwell"], "1984")
        book3 = Book(["Harper Lee"], "To Kill a Mockingbird")
        books = [book1, book2, book3]
        result = hw1.books_by_author("George Orwell", books)
        expected = [book2]
        self.assertEqual(expected, result)

    def test_books_by_author_2(self):
        book1 = Book(["George Orwell"], "1984")
        book2 = Book(["George Orwell"], "Animal Farm")
        book3 = Book(["Harper Lee"], "To Kill a Mockingbird")
        books = [book1, book2, book3]
        result = hw1.books_by_author("George Orwell", books)
        expected = [book1, book2]
        self.assertEqual(expected, result)

    # Part 7
    def test_circle_bound_small_rectangle(self):
        top_left = Point(1, 1)
        bottom_right = Point(3, 3)
        rect = Rectangle(top_left, bottom_right)
        result = hw1.circle_bound(rect)
        expected_center = Point(2, 2)
        expected_radius = 2**(1/2)
        expected_circle = Circle(expected_center, expected_radius)
        self.assertEqual(expected_circle, result)

    def test_circle_bound_large_rectangle(self):
        top_left = Point(-4, -2)
        bottom_right = Point(4, 2)
        rect = Rectangle(top_left, bottom_right)
        result = hw1.circle_bound(rect)
        expected_center = Point(0, 0)
        expected_radius = 20**(1/2)
        expected_circle = Circle(expected_center, expected_radius)
        self.assertEqual(expected_circle, result)

    # Part 8
    def test_below_pay_average_1(self):
        employees = [
            Employee("Alice", 50000),
            Employee("Bob", 60000),
            Employee("Charlie", 45000),
            Employee("David", 70000)
        ]
        result = hw1.below_pay_average(employees)
        expected = ["Alice", "Charlie"]
        self.assertEqual(expected, result)

    def test_below_pay_average_2(self):
        employees = [
            Employee("Eve", 80000),
            Employee("Frank", 90000),
            Employee("Grace", 85000)
        ]
        result = hw1.below_pay_average(employees)
        expected = ["Eve"]
        self.assertEqual(expected, result)





if __name__ == '__main__':
    unittest.main()
