import uvicorn
from fastapi import FastAPI
from routers import table
from routers import reservation

app = FastAPI()
app.include_router(table.router)
app.include_router(reservation.router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
