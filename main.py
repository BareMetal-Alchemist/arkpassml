from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import gen


app = FastAPI()

@app.get("/generate")
def generate():
    password = gen.genPass()
    return JSONResponse(content={"password": password})

