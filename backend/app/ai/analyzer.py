# from deepface import DeepFace

# def analyze_face(image_path):
#     try:
#         result = DeepFace.analyze(
#             img_path=image_path,
#             actions=["age", "gender"],
#             enforce_detection=False
#         )

#         return {
#             "age": result[0]["age"],
#             "gender": result[0]["dominant_gender"]
#         }

#     except Exception:
#         return {
#             "age": "Unknown",
#             "gender": "Unknown"
#         }
from deepface import DeepFace

def analyze_face(image_path):
    try:
        result = DeepFace.analyze(
            img_path=image_path,
            actions=["age", "gender"],
            enforce_detection=False
        )

        print("Analysis Result:", result)

        return {
            "age": result[0]["age"],
            "gender": result[0]["dominant_gender"]
        }

    except Exception as e:
        print("Analyzer Error:", e)

        return {
            "age": "Unknown",
            "gender": "Unknown"
        }