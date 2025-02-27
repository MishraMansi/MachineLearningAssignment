# 1. Difference between Lists and Tuples
# Lists are mutable, meaning we can change their elements, while tuples are immutable.
# Lists are slower compared to tuples due to mutability.

# Example
# my_list = [1, 2, 3]
# my_tuple = (1, 2, 3)

# Modifying the list (allowed)
# my_list.append(4)
# print("Modified List:", my_list)

# Modifying the tuple (not allowed, will cause an error)
# my_tuple.append(4)  # This will raise an AttributeError

# 2. Type Conversion in Python
# Python automatically converts types in expressions where possible.

# Integer to Float
# num_int = 10
# num_float = num_int + 5.5  # num_int is converted to float
# print("Converted Float:", num_float)

# # String to List
# string = "Hello"
# string_list = list(string)  # Converts string into a list of characters
# print("Converted List:", string_list)

# 3. Using += operator to increase value by 10
number = 20
number += 10  # Increases number by 10
print("Updated Number:", number)

# 4. Check if a year is a leap year
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year")
else:
    print(year, "is NOT a Leap Year")

# 5. Grading System
marks = int(input("Enter your marks: "))

if 90 <= marks <= 100:
    print("Grade: A")
elif 80 <= marks <= 89:
    print("Grade: B")
elif 70 <= marks <= 79:
    print("Grade: C")
elif 60 <= marks <= 69:
    print("Grade: D")
else:
    print("Grade: F")
