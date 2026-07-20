'''Student Management System using FastAPI'''
from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional
import json

app = FastAPI()

class Student(BaseModel):

    roll_no : Annotated[str, Field(..., description='Roll no. of the student', examples=['001'])]
    name : Annotated[str, Field(..., description='Name of the student')]
    




