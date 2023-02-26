from sanic import Blueprint, response
from sanic_jwt_extended import jwt_required
from api.v1.managers import manager_list_of_lists,manager_create_list,manager_update_list,manager_delete_list,manager_list_details

lists = Blueprint("lists", url_prefix="/mylists")


# GET api/v1/mylists/all → Get a list of all my lists
@lists.get("/all")
@jwt_required
async def list_of_lists(request, token):


    res = await manager_list_of_lists(request,token)
    return response.json(res)


# GET api/v1/mylists/<list-id>
@lists.get("/<id>")
@jwt_required()
async def list_details(request, token, id):

    res = await manager_list_details(request,token,id)
    return response.json(res)


# POST api/v1/mylists  creating a list
@lists.post("/")
@jwt_required()
async def create_list(request, token):

    res = await manager_create_list(request,token)
    return response.json(res)


# PUT api/v1/mylists/<list-id>
@lists.put("/<id>")
@jwt_required()
async def update_list(request, token, id):
    # nme = request.json.get("name", None)
    # user_id = token.identity
    # lst = await List_Details.filter(user_id=user_id, name=nme)
    # if lst:
    #     return response.json({"error": {
    #         "error": {
    #             "status_code": 404,
    #             "message": "List name already exists",
    #             "details": "Lists with same name cannot be create"
    #         },
    #         "success": False
    #     }})
    # await List_Details.filter(list_id=id).update(list_title=nme, list_modified=datetime.now())
    # return response.json({"data": "list details updated",
    #                       "success":True})

    res = await manager_update_list(request,token,id)
    return response.json(res)


# DELETE api/v1/mylists
@lists.delete("/")
@jwt_required()
async def delete_list(request, token):
    # name = request.json.get("name", None)
    # user_id = token.identity
    # lst = await List_Details.get_or_none(user_id=user_id, list_title=name)
    # if lst is None:
    #     return response.json({"error": {
    #         "error": {
    #             "status_code": 404,
    #             "message": "List does not exist",
    #             "details": "List which is not present, cant be deleted"
    #         },
    #         "success": False
    #     }})
    # await List_Details.filter(list_id=lst.list_id).delete()
    # return response.json({"data": f"List {name} deleted",
    #                       "success":True})
    res = await manager_delete_list(request,token)
    return response.json(res)


