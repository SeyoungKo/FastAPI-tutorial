from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

# model
class Todo(BaseModel):
    name: str
    due_date: str
    description: str

app = FastAPI(title='Todo API', version='v1.0')

store_todo = []

@app.get('/')
async def home():
    return {'Hello': 'World'}

# create
@app.post('/todo/')
async def create_todo(todo: Todo):
    store_todo.append(todo)
    return todo

# read
@app.get('/todo/', response_model=list[Todo])
async def get_all_todos():
    return store_todo


@app.get('/todo/{id}')
async def get_todo(id: int):
    try:
        return store_todo[id]
    except:
        raise HTTPException(status_code=404, detail='Todo Not Found!')


# update
@app.put('/linux/{id}')
async def update_todo(id: int, todo: Todo):
    try:
        store_todo[id] = todo
        return store_todo[id]

    except:
        raise HTTPException(status_code=404, detail='Todo Not Found!')


# delete
@app.delete('/todo/{id}')
async def delete_linux(id: int):
    try:
        obj = store_todo[id]
        store_todo.pop(id)
        return obj
    except:
        raise HTTPException(status_code=404, detail='Todo Not Found!')