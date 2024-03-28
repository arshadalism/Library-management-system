from db_client import database
from Schema import User_signup, User_login
from fastapi import HTTPException
from db import user_col
import string
import secrets
import asyncio
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def random_library_id_gen():
    length = 10
    letters = string.ascii_letters + string.digits + "@#$&*()+_{}-.=%"
    library_id = "".join(secrets.choice(letters) for i in range(length))
    return library_id


async def signup(signup_data: User_signup):
    try:
        if await user_col.find_one({"email": signup_data.email}):
            raise HTTPException(status_code=400, detail="User is already registered")
        library_id = await random_library_id_gen()
        enrollment = signup_data.enrollment
        user_signup_data = {
            "_id": enrollment,
            "name": signup_data.name,
            "course": signup_data.course,
            "email": signup_data.email,
            "password": pwd_context.hash(signup_data.password),
            "library_id": library_id
        }
        await user_col.insert_one(user_signup_data)
        return {"result": "User signup successfully", "library_id": library_id}
    except Exception as e:
        return {"error": str(e)}


async def login(login_data: User_login):
    user = await user_col.find_one({"email": login_data.email})
    print("user", user)
    print(login_data.password)
    if not user or not pwd_context.verify(login_data.password, user["password"]):
        raise HTTPException(status_code=404, detail="email or password is incorrect")
    return {"message": "Login successfully"}


async def get_library_id(enrollment: int):
    result = await user_col.find_one({"_id": enrollment}, {"_id": 0, "library_id": 1})
    if result:
        return {'library_id': result['library_id']}
    return {"Sorry, No user exists"}


async def main():
    # student_data = User_signup(name="Arshad", enrollment=2100100484, course="B-tech", email="arshad123@gmail.com",password=123456)
    # response = await signup(student_data)
    # print(response)
    # login_student = User_login(email="arshad123@gmail.com", password=126, library_id='kLuIz7Gy-N')
    # result = await login(login_student)
    # print(result)
    # res = await get_library_id(210010484)
    # print(res)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
