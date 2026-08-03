# Task API

## Description

A simple CRUD API built using FastAPI.

## Installation

pip install -r requirements.txt

## Run

uvicorn main:app --reload

## Swagger

http://127.0.0.1:8000/docs

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Home |
| GET | /health | Health Check |
| GET | /tasks | Get all tasks |
| GET | /tasks/{id} | Get one task |
| POST | /tasks | Create task |
| PUT | /tasks/{id} | Update task |
| DELETE | /tasks/{id} | Delete task |

## Example curl

curl http://127.0.0.1:8000/tasks