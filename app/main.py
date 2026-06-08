from fastapi import FastAPI

app = FastAPI()

employees = [
    {"id": 1, "name": "Yash", "Role":"Pyhton"},
    {"id": 2, "name": "Abhishek", "Role":"Pyhton"},
    {"id": 3, "name": "Lavesh", "Role":"Pyhton"},
    {"id": 4, "name": "Mayank", "Role":"Pyhton"}
]

tasks = [
    {"id": 1, "task": "FastAPI"},
    {"id": 2, "task": "GIT"},
    {"id": 3, "task": "GenAI"}
]

@app.get("/employees")
def employees_data():
    return employees