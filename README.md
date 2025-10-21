Shopping Cart System (Using Python Magic Methods)
* Project Overview

This project demonstrates how magic methods (also called dunder methods) in Python can make classes behave like built-in data types.
The program simulates a shopping cart system, where you can add products, merge carts, compare carts, and display totals — all using magic methods for elegant, object-oriented design.

* Objectives

To understand the concept of Magic Methods / Dunder Methods in Python.

To implement Object-Oriented Programming (OOP) concepts such as:

Classes and Objects

Encapsulation

Operator Overloading

Method Overriding

To show how operators like +, ==, and functions like len() can be customized for user-defined objects.

* Features

  Add products to shopping carts
  Merge two shopping carts using + operator
  Compare total prices of two carts using == operator
  Display cart contents using print()
  Get total item count using len()

* Magic Methods Used
Magic Method	Purpose	Example Usage
__init__()	Initializes objects when created	p1 = Product("Laptop", 85000)
__str__()	Returns readable string representation	print(cart)
__len__()	Returns total number of items	len(cart)
__add__()	Merges two carts using +	merged = c1 + c2
__eq__()	Compares total prices of two carts	c1 == c2


* Technologies Used

Programming Language: Python 3.x

Concepts: Object-Oriented Programming, Magic Methods

* How to Run

Copy the code into a file named shopping_cart.py.

Run the file in your Python environment or terminal:

python shopping_cart.py


Observe the printed outputs and behavior of overloaded operators.
