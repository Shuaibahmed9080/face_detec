from fastapi import FastAPI

from app.routes.face import router as face_router

from app.routes.users import router as user_router
from app.routes.recognition import router as recognition_router

from app.database import Base, engine
from app.models.attendance import Attendance

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# Register routes
app.include_router(face_router)
app.include_router(user_router)
app.include_router(recognition_router)


@app.get("/")
def home():
    return {
        "message": "Server Running"
    }
# from fastapi import FastAPI
# from app.routes.face import router as face_router
# from app.database import Base, engine
# from app.models.attendance import Attendance
# from app.routes.users import router as user_router
# from app.routes.recognition import router as recognition_router

# app = FastAPI()

# app.include_router(face_router)

# Base.metadata.create_all(bind=engine)

# app.include_router(user_router)
# app.include_router(recognition_router)

# @app.get("/")
# def home():
#     return {"message": "Server Running"}