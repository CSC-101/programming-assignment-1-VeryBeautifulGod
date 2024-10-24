import data
from data import Price, Rectangle, Book, Point, Circle, Employee


# Write your functions for each part in the space below.

# Part 1
def vowel_count(input_str: str) -> int:
    vowels = "aeiouAEIOU"
    vowel_counter = 0
    for char in input_str:
        if char in vowels:
            vowel_counter = vowel_counter + 1
    return vowel_counter

# Part 2
def short_lists(input_list: list[list[int]]) -> list[list[int]]:
    result = []
    for i in input_list:
        if len(i) == 2:
            result.append(i)
    return result

# Part 3
def ascending_pairs(nested_list:list[list[int]]) -> list[list[int]]:
    result = []
    for i in nested_list:
        if len(i) == 2:
            result.append(sorted(i))
        else:
            result.append(i)
    return result

# Part 4
def add_prices(price1, price2):
    total_dollars = price1.dollars + price2.dollars
    total_cents = price1.cents + price2.cents
    if total_cents >= 100:
        total_dollars += total_cents // 100
        total_cents = total_cents % 100
    return Price(total_dollars, total_cents)


# Part 5
def rectangle_area(rectangle: Rectangle) -> float:
    width = rectangle.bottom_right.x - rectangle.top_left.x
    height = rectangle.bottom_right.y - rectangle.top_left.y
    area = width * height
    return area

# Part 6
def books_by_author(author_name: str, books: list[Book]) -> list[Book]:
    matching_books = []

    for book in books:
        if author_name in book.authors:
            matching_books.append(book)

    return matching_books


# Part 7
def circle_bound(rectangle: Rectangle) -> Circle:
    center_x = (rectangle.top_left.x + rectangle.bottom_right.x) / 2
    center_y = (rectangle.top_left.y + rectangle.bottom_right.y) / 2
    center = Point(center_x, center_y)

    corner_x = rectangle.top_left.x
    corner_y = rectangle.top_left.y
    radius = ((corner_x - center_x) ** 2 + (corner_y - center_y) ** 2)**(1/2)

    return Circle(center, radius)

# Part 8
def below_pay_average(employees: list[Employee]) -> list[str]:
    if not employees:
        return []

    total_pay = 0
    for employee in employees:
        total_pay = total_pay + employee.pay_rate

    average_pay = total_pay / len(employees)

    below_average_employees = []
    for employee in employees:
        if employee.pay_rate < average_pay:
            below_average_employees.append(employee.name)

    return below_average_employees


