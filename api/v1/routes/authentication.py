from sanic import Blueprint, response
from sanic_jwt_extended import jwt_required
from api.v1.managers import manager_authenticate, manager_register_user

auth = Blueprint("auth")


@auth.post("/login")
async def authenticate(request):

    res = await manager_authenticate(request)
    return response.json(res)


@auth.post("/logout")
@jwt_required
async def logout(request, token):
    await token.revoke()
    return response.json({"data": "Logged out",
                          "success": True})
    # return response.json(dict(msg="Goodbye"), status=200)


@auth.post('/signup')
async def register_user(request):
    res = await manager_register_user(request)
    return response.json(res)