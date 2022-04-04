
from fastapi import FastAPI,HTTPException,status
from typing import Optional,List
from pydantic import BaseModel


app = FastAPI(title="School Management System")
all_details = []

class Student(BaseModel):
    name:str
    age:int
    classb:str

@app.post("/Register Student",tags=["Students"])
def register(student:Student):
    all_details.append(student)
    return student


@app.get('/All Students/',tags=['Students'],response_model=List[Student])
def all_students():
    return all_details


@app.get('/student/{student_id}',tags=['Students'])
def get_student(student_id:int):
    try:
        return all_details[student_id]
    except:
        raise HTTPException(status_code=404,detail='student id not found')
@app.put('/student/{student_id}',tags=['Students'])

def edit_student_details(student_id:int, student:Student,tags=['Students']):
    try:
        all_details[student_id]=student
        return all_details[student_id]
    except:
        raise HTTPException(status_code=404,detail='student id not found')

@app.delete('/student/{student_id',tags=['Students'])
def delete_student(student_id:int):
    try:
        students=all_details[student_id]
        all_details.pop(student_id)
        return students

    except:
        raise HTTPException(status_code=404,detail='student id not found')

