from enum import Enum

from fastapi import FastAPI # fastapi package

# localhost:8000/docs
# localhost:8000/redoc
# localhost:8000/openapi.json

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI() # Creates instance of FastAPI

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/") # Path operation decorator, "/" for root, displayed on initial page
async def root():
    return {"message": "Hello World"}

@app.get("/items")
async def read_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

@app.get("/items/{item_id}") # gets an item from a collection of items
async def read_item(item_id: str, q: str | None = None, short: bool = False): # type declarations
    item = {"item_id": item_id} # query parameter
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a longer description"}
        )
    return item

@app.get("/users") # returns list of users
async def read_users():
    return ["Jim Carey", "Charlize Theron"]

@app.get("/users/me") # fixed paths must be evaluated first to avoid error
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}") # gets a user from a collection of users
async def read_user(user_id: str): # checks for string type
    return {"user_id": user_id}

@app.get("/models/{model_name}") # parameter model_name is set
async def get_model(model_name: ModelName): #path parameter requires ModelName class
    if model_name is ModelName.alexnet: # seeks enum member
        return {"model_name": model_name, "message": "Deep Learning FTW"}
    if model_name is ModelName.value == "lenet": # gets enum value
        return {"model_name": model_name, "message": "LeCNN all the images"}
    
    return {"model_name": model_name, "message": "Have some residuals"}

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_items(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id} # multiple query parameters
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str): # required parameter, needs to be set in URL
    item = {"item_id": item_id, "needy": needy}
    return item








