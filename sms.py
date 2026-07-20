'''Student Management System using FastAPI'''
from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional
import json

app = FastAPI()

class Student(BaseModel):

    enroll : Annotated[str, Field(..., description='ID of the student', examples='LNCFBTC00001')]
    roll_no : Annotated[str, Field(..., description='Roll no. of the student', examples=['001'])]
    first_name : Annotated[str, Field(..., description='First name of the student')]
    last_name : Annotated[str, Field(..., description=':Last name of the student')]
    father_name : Annotated[str, Field(..., description="Father's name")]
    mother_name : Annotated[str, Field(..., description="Mother's name")]
    course : Annotated[str, Field(..., description='Course which student persue', examples=['B.Tech', 'BBA', 'B.Com']
    




