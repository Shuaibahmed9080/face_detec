# from fastapi import APIRouter, UploadFile, File, Form
# import os
# import shutil

# router = APIRouter()


# @router.post("/register")
# async def register_user(
#     name: str = Form(...),
#     user_id: str = Form(...),
#     file: UploadFile = File(...)
# ):
#     os.makedirs(
#         "app/uploads/faces",
#         exist_ok=True
#     )

#     file_path = f"app/uploads/faces/{file.filename}"

#     with open(file_path, "wb") as buffer:
#         shutil.copyfileobj(
#             file.file,
#             buffer
#         )

#     return {
#         "message": "User registered successfully",
#         "name": name,
#         "user_id": user_id
#     }
# # from fastapi import APIRouter, UploadFile, File, Form
# # import os
# # import shutil

# # # router = APIRouter()
# # router = APIRouter()


# # @router.post("/register")
# # async def register_user(
# #     name: str = Form(...),
# #     user_id: str = Form(...),
# #     file: UploadFile = File(...)
# # ):
# #     os.makedirs(
# #         "app/uploads/faces",
# #         exist_ok=True
# #     )

# #     file_path = f"app/uploads/faces/{file.filename}"

# #     with open(file_path, "wb") as buffer:
# #         shutil.copyfileobj(
# #             file.file,
# #             buffer
# #         )

# #     return {
# #         "message": "User registered successfully",
# #         "name": name,
# #         "user_id": user_id
# #     }