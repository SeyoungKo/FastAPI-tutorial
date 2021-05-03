from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# request
class Package(BaseModel):
    name: str
    number: str
    description: Optional[str] = None

# response
class PackageIn(BaseModel):
    secret_id: int
    name: str
    number: str
    description: Optional[str] = None

@app.get('/')
async def hello_world():
    return {'Hello': 'World'}

# using pydantic BaseModel
@app.post('/package/')
async def make_package(package: Package):
    return package

# pydantic BaseModel with path parameter
@app.post('/package/{priority}')
async def make_package2(priority: int, package: Package, value: bool):
    return {'priority': priority, **package.dict(), 'value': value}

# pydantic BaseModel with response_model
@app.post('/package3/', response_model=Package, response_model_include={'description'}) # response result include / exclude
async def make_package3(package: PackageIn):
    return package

########################################################
# path parameter
@app.get('/component/{component_id}')
async def get_component(component_id):
    return {'component_id': component_id}

# define parameter types
@app.get('/component/{component_id}')
async def get_component(component_id: int):
    return {'component_id': component_id}

# query parameter (using keyword argument)
@app.get('/component/')
async def read_component(number: int, text: str):
    return {'number': number, 'text': text}

# using optional str type query parameter
@app.get('/component/')
async def read_component(number: int, text: Optional[str]):
    return {'number': number, 'text': text}