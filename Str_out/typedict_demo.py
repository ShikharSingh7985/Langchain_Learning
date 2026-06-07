"""
Overall Intuition:
- This code uses TypedDict to define the expected structure of a dictionary.
- Person is a type hint that says the dictionary should contain name as string and age as integer.
- Then a dictionary is created using this Person type.
- Finally, the dictionary is printed.
- Important point: TypedDict only helps with static type checking; it does not validate types at runtime.
- So even though age is written as int, Python will still allow '35' as a string while running.
"""

from typing import TypedDict  # Imports TypedDict, which is used to define the expected key-value structure of a dictionary

class Person(TypedDict) :  # Defines a TypedDict named Person with fixed keys and expected value types
    name: str  # Specifies that the name key should have a string value
    age:int  # Specifies that the age key should have an integer value

new_Person : Person={'name' : 'nitish' ,'age': '35'}  # Creates a dictionary typed as Person, but age is given as string; Python allows it at runtime

print(new_Person)  # Prints the dictionary