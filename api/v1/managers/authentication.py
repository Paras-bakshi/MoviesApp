import bcrypt
from api.v1.models import *
from sanic_jwt_extended import JWT
from tortoise.exceptions import IntegrityError
from api.v1.validation import *
from pydantic import ValidationError


async def manager_authenticate(request):
    # Validate the request data
    email = request.json.get("email", None)
    password = request.json.get("password", None)

    # Validate the provided credentials
    user = await Users.get_or_none(email=email)
    if user and bcrypt.checkpw(password.encode('utf-8'), user.password_hash.encode('utf-8')):
        access_token = JWT.create_access_token(identity=user.user_id)
        return {"access_token": access_token,
                "success": True}
    return {"error": {
        "status_code": 404,
        "message": "Invalid email or password",
        "details": "Check the email and password and enter valid email and password"},
        "success": False}


async def manager_register_user(request):
    try:
        # Validate the request data
        email = request.json.get("email", None)
        password = request.json.get("password", None)
        first_name = request.json.get("first_name", None)
        last_name = request.json.get("last_name", None)

        user1 = User(email=email, password=password, first_name=first_name, last_name=last_name)
    except ValidationError as e:
        s = str(e)
        li = (s.splitlines())
        print(li)
        dict = {}
        dict["Error"] = li[0]
        for x in range(1, len(li), 2):
            dict[li[x]] = li[x + 1]
        final_dict = {"error": {"status_code": 403, "message": "Invalid Arguments", "details": dict},
                      "Success": "False"}

        # {"details": dict}
        return final_dict

    # Hash the password
    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Store the user in the database
    try:
        await Users.create(email=email, password_hash=password_hash.decode('utf-8'), first_name=first_name,
                           last_name=last_name)
        usr = await Users.get(email=email)
        await List_Details.create(list_id=str(uuid4()), user_id=usr.user_id, list_title="Watched")
        await List_Details.create(list_id=str(uuid4()), user_id=usr.user_id, list_title="Favourites")
        await List_Details.create(list_id=str(uuid4()), user_id=usr.user_id, list_title="To watch")
        return {"data": "User registered successfully",
                              "success": True}
    except IntegrityError as e:
        return {"error": {"status_code": 403, "message": "Email ID already exists", "details": "No 2 accounts can be registered with same email id"},
                              "Success": "False"}

