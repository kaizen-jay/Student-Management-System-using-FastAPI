'''Student Management System using FastAPI'''
from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional
import json

app = FastAPI()

class Student(BaseModel): #This is the Student pydantic model

    enroll : Annotated[str, Field(..., description="Enrollment no. of the student", examples=["LNCFBTC00001"])]
    roll_no : Annotated[str, Field(..., description='Roll no. of the student', examples=["001"])]
    first_name : Annotated[str, Field(..., description='First name of the student')]
    last_name : Annotated[str, Field(..., description=':Last name of the student')]
    age : Annotated[int, Field(..., gt=0, lt=30, description='Age of the student')]
    gender : Annotated[Literal['Male', 'Female', 'Others'], Field(..., description='Gender of the student')]
    father_name : Annotated[str, Field(..., description="Father's name")]
    mother_name : Annotated[str, Field(..., description="Mother's name")]
    course : Annotated[str, Field(..., description='Course which student persue', examples=["B.Tech", "BBA", "B.Com"])]
    city : Annotated[str, Field(..., description='City where student lives in')]

    #the above code i have written is so that the user gets a detailed description of what details they are filling...

#-----------------Updating student details--------------------

class StudentUpdate(BaseModel): #this is the StudentUpdate pydantic model
    roll_no : Annotated[Optional[str], Field(default=None)]
    first_name : Annotated[Optional[str], Field(default=None)]
    last_name : Annotated[Optional[str], Field(default=None)]
    age : Annotated[Optional[int], Field(default=None)]
    gender : Annotated[Optional[Literal['Male', 'Female', 'Others']], Field(default=None)]
    father_name : Annotated[Optional[str], Field(default=None)]
    mother_name : Annotated[Optional[str], Field(default=None)]
    course : Annotated[Optional[str], Field(default=None)]
    city : Annotated[Optional[str], Field(default=None)]
    #as we have use none datatype it automatically takes any input given to it
    #Annotated is used to add description
    #Literal is used to give options

#------------Loading data-----------
#whenever we call this function it will load the data 
def load_data():
    with open('students.json', 'r') as f:#opening it in read mode
        data = json.load(f)
    return data

#----------Saving data-------------

def save_data(data):
    with open('students.json', 'w') as f:
        json.dump(data, f, indent=4)
#jo data hame input mil raha hai ham use data me dump kar rahe hai


#--------------------Endpoints---------------------

@app.get('/')
def hello():
    return("STUDENT MANAGEMENT SYSTEM") #This is the first end point of our api

@app.post('/add')
def add_student(student: Student):
    data = load_data()
    #check krna hai ki student already exist ya nahi
    if student.enroll in data:
        raise HTTPException(status_code=400, detail='Student already exist')

    data[student.enroll] = student.model_dump(exclude=["enroll"]) 

    save_data(data)

    return JSONResponse(status_code=201, content={'message': 'Student created successfully'})
print("Test")

