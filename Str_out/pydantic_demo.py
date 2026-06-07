from pydantic import BaseModel,Field

class Student(BaseModel):
    name:str
    cgpa:float=Field(gt=0,lt=10,description="A decimal value representing grades of  student")
    
new_Student={'name':"hii",'cgpa':8.8}

student=Student(**new_Student)
# print(student)

student_json=student.model_dump_json()

print(student_json)