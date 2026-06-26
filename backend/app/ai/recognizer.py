# from deepface import DeepFace

# def recognize_face(image_path):
#     try:
#         result = DeepFace.find(
#             img_path=image_path,
#             db_path="app/uploads",
#             enforce_detection=False
#         )

#         if len(result) > 0 and not result[0].empty:
#             matched_path = result[0].iloc[0]["identity"]

#             # get file name only
#             name = matched_path.split("\\")[-1].split(".")[0]

#             return {
#                 "status": True,
#                 "name": name
#             }

#         return {
#             "status": False,
#             "name": "Unknown Person"
#         }

#     except Exception:
#         return {
#             "status": False,
#             "name": "Unknown Person"
#         }
from deepface import DeepFace

def recognize_face(image_path):
    try:
        result = DeepFace.find(
            img_path=image_path,
            db_path="app/uploads",
            enforce_detection=False
        )

        print("Recognition Result:", result)

        if len(result) > 0 and not result[0].empty:
            matched_path = result[0].iloc[0]["identity"]

            name = matched_path.split("\\")[-1].split(".")[0]

            return {
                "status": True,
                "name": name
            }

        return {
            "status": False,
            "name": "Unknown Person"
        }

    except Exception as e:
        print("Recognition Error:", e)

        return {
            "status": False,
            "name": "Unknown Person"
        }