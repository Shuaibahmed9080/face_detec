# from fastapi import APIRouter, UploadFile, File
# from deepface import DeepFace
# import os
# import shutil

# router = APIRouter()


# @router.post("/recognize")
# async def recognize_face(
#     file: UploadFile = File(...)
# ):
#     temp_path = f"app/uploads/{file.filename}"

#     os.makedirs(
#         "app/uploads",
#         exist_ok=True
#     )

#     with open(temp_path, "wb") as buffer:
#         shutil.copyfileobj(
#             file.file,
#             buffer
#         )

#     if not os.path.exists(
#         "app/uploads/faces"
#     ):
#         return {
#             "known": False,
#             "message": "No registered users"
#         }

#     for image in os.listdir(
#         "app/uploads/faces"
#     ):
#         stored_path = f"app/uploads/faces/{image}"

#         result = DeepFace.verify(
#             img1_path=temp_path,
#             img2_path=stored_path
#         )

#         if result["verified"]:
#             return {
#                 "known": True,
#                 "message": "Face recognized"
#             }

#     return {
#         "known": False,
#         "message": "Unknown Person"
#     }
# # from fastapi import APIRouter, UploadFile, File
# # from deepface import DeepFace
# # import os
# # import shutil

# # router = APIRouter()


# # @router.post("/recognize")
# # async def recognize_face(
# #     file: UploadFile = File(...)
# # ):
# #     temp_path = f"app/uploads/{file.filename}"

# #     with open(temp_path, "wb") as buffer:
# #         shutil.copyfileobj(
# #             file.file,
# #             buffer
# #         )

# #     for image in os.listdir(
# #         "app/uploads/faces"
# #     ):
# #         stored_path = f"app/uploads/faces/{image}"

# #         result = DeepFace.verify(
# #             img1_path=temp_path,
# #             img2_path=stored_path
# #         )

# #         if result["verified"]:
# #             return {
# #                 "known": True,
# #                 "message": "Face recognized"
# #             }

# #     return {
# #         "known": False,
# #         "message": "Unknown Person"
# #     }