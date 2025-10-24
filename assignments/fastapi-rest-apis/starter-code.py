"""Starter code mínimo para a tarefa "Construindo APIs REST com FastAPI".

Execute com:
    uvicorn starter-code:app --reload

Endpoints:
    GET  /items
    POST /items
    GET  /items/{item_id}
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4

app = FastAPI(title="FastAPI Starter - Assignment")


class Item(BaseModel):
    id: Optional[str] = None
    name: str
    description: Optional[str] = None


items: List[Item] = []


@app.get("/items", response_model=List[Item])
def list_items():
    return items


@app.post("/items", response_model=Item)
def create_item(item: Item):
    item.id = str(uuid4())
    items.append(item)
    return item


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: str):
    for it in items:
        if it.id == item_id:
            return it
    raise HTTPException(status_code=404, detail="Item not found")
