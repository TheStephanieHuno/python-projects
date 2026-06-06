# Import FastAPI framework
from fastapi import FastAPI
from pydantic import BaseModel

# Create FastAPI app instance
app = FastAPI()

# -------------------------------
# STEP 1: Create Student Model
# -------------------------------
# This defines how a student record should look like
class Student(BaseModel):
    student_id: int
    name: str
    age: int
    score: float

# -------------------------------
# STEP 2: Temporary Database
# -------------------------------
# We use a list to store students (in memory)
students = []

# -------------------------------
# STEP 3: Home Route
# -------------------------------
@app.get("/")
def home():
    return {"message": "Student Record API is running"}

# -------------------------------
# STEP 4: Add a Student (CREATE)
# -------------------------------
@app.post("/students")
def add_student(student: Student):
    # Add new student to list
    students.append(student)
    return {"message": "Student added successfully", "student": student}

# -------------------------------
# STEP 5: View All Students (READ ALL)
# -------------------------------
@app.get("/students")
def get_all_students():
    return {"students": students}

# -------------------------------
# STEP 6: Get One Student by ID (READ ONE)
# -------------------------------
@app.get("/students/{student_id}")
def get_student_by_id(student_id: int):
    # Loop through students to find matching ID
    for student in students:
        if student.student_id == student_id:
            return {"student": student}

    # If not found
    return {"message": "Student not found"}