"""
Overall Intuition:
- This code uses Pydantic to create a Student data model.
- The model validates that name is a string and cgpa is a float.
- The Field() function adds validation rules for cgpa.
- cgpa must be greater than 0 and less than 10.
- A dictionary is unpacked into the Student model.
- Then the validated student object is converted into JSON format.
- Finally, the JSON string is printed.
"""

from pydantic import BaseModel,Field  # Imports BaseModel for creating Pydantic models and Field for adding validation rules

class Student(BaseModel):  # Defines a Student model class that inherits from Pydantic BaseModel
    name:str  # Creates a name field that must be a string
    cgpa:float=Field(gt=0,lt=10,description="A decimal value representing grades of  student")  # Creates a cgpa field that must be float, greater than 0, less than 10, and has a description
    
new_Student={'name':"hii",'cgpa':8.8}  # Creates a dictionary containing student data

student=Student(**new_Student)  # Unpacks the dictionary and creates a validated Student object
# print(student)  # This line is commented, but if enabled, it prints the Student object

student_json=student.model_dump_json()  # Converts the Student object into a JSON string

print(student_json)  # Prints the JSON string