from fastapi import FastAPI
from carina.routes.healthcheck import router


app = FastAPI()
app.include_router(router, prefix="/healthcheck", tags=["healtcheck"])
