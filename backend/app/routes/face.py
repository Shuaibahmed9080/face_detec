from fastapi import APIRouter, UploadFile, File
import cv2
import numpy as np
from app.ai.detector import detect_faces
from app.ai.recognizer import recognize_face
from app.ai.analyzer import analyze_face
from app.database import SessionLocal
from app.models.attendance import Attendance

router = APIRouter()


@router.post("/detect")
async def detect_face(file: UploadFile = File(...)):
    contents = await file.read()

    # convert bytes into numpy array
    np_arr = np.frombuffer(contents, np.uint8)

    # decode image
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    # check image valid or not
    if img is None:
        return {
            "status": False,
            "message": "Invalid image"
        }

    # save temporary image
    temp_path = "app/uploads/temp.jpg"
    cv2.imwrite(temp_path, img)

    # detect face
    results = detect_faces(img)

    if results and results.detections:

        # recognize person
        recognition = recognize_face(temp_path)

        # analyze age and gender
        analysis = analyze_face(temp_path)

        # database connection
        db = SessionLocal()

        # save attendance
        new_attendance = Attendance(
            name=recognition["name"],
            age=analysis["age"],
            gender=analysis["gender"],
            status="Present"
        )

        db.add(new_attendance)
        db.commit()
        db.close()

        return {
            "status": True,
            "message": "Face detected",
            "name": recognition["name"],
            "age": analysis["age"],
            "gender": analysis["gender"]
        }

    return {
        "status": False,
        "message": "No face found"
    }