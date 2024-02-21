from fastapi import FastAPI
from web_app import api_router
import uvicorn

if __name__ == '__main__':
    app = FastAPI()
    app.include_router(api_router)
    uvicorn.run(
        app=app,
        host="localhost",
        port=8080
    )
