from typing import Union

from fastapi import FastAPI

#app = FastAPI(root_path="/api/v1")
#app = FastAPI(
#    title="My Project",
#    openapi_url=f"/api/v1/openapi.json",
#    docs_url=f"/api/v1/docs",
#    redoc_url=f"/api/v1/redoc",
#    root_path="/api" # <------ This root_path fix the problem
#a)

app = FastAPI(title='',
       docs_url='/docs', 
       redoc_url='/redoc',
       openapi_url='/openapi.json')

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
