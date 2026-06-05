from fastapi import FastAPI
from datetime import datetime

app = FastAPI(
    title="Employee Management API",
    description="Sample FastAPI application for learning and containerization",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Employee Management API",
        "documentation": "/docs",
        "version": "1.0.0"
    }


@app.get("/health")
def health():
    return {
        "status": "UP",
        "timestamp": datetime.now()
    }


@app.get("/info")
def info():
    return {
        "application": "Employee Management API",
        "environment": "Development",
        "version": "1.0.0",
        "developer": "Harshitha"
    }


@app.get("/employees")
def get_employees():
    return [
        {
            "id": 1,
            "name": "John",
            "department": "IT"
        },
        {
            "id": 2,
            "name": "David",
            "department": "HR"
        },
        {
            "id": 3,
            "name": "Priya",
            "department": "Finance"
        }
    ]


@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    return {
        "id": employee_id,
        "name": "Sample Employee",
        "department": "IT"
    }


@app.get("/search")
def search_employee(name: str):
    return {
        "message": f"Searching employee: {name}"
    }