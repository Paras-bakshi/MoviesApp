from api.v1.models import List_Details
from tortoise.timezone import datetime
from uuid import uuid4



async def manager_list_of_lists(request, token):
    userid = token.identity
    data = await List_Details.filter(user_id=userid)
    lst = []
    for row in data:
        ls = {}
        ls["title"] = row.list_title
        ls["list_id"] = row.list_id
        lst.append(ls)
    return {"data": lst,
                          "success":True}


async def manager_list_details(request, token, id):
    data = await List_Details.get(list_id=id)
    ls = {}
    ls["title"] = data.list_title
    ls["list_id"] = data.list_id
    ls["list_created"] = str(data.list_created)
    ls["list_modified"] = str(data.list_modified)
    return {"data": ls, "success":True}

async def manager_create_list(request, token):
    name = request.json.get("name", None)
    user_id = token.identity
    lst = await List_Details.filter(user_id=user_id, list_title=name)
    if lst:
        return {"error": {
            "error": {
                "status_code": 404,
                "message": "List already exists",
                "details": "Lists with same name cannot be created"
            },
            "success": False
        }}
    await List_Details.create(list_id=str(uuid4()), list_title=name, user_id=user_id)
    return {"data": f"List {name} created",
                          "success":True}


async def manager_update_list(request, token, id):
    nme = request.json.get("name", None)
    user_id = token.identity
    lst = await List_Details.filter(user_id=user_id, list_title=nme)
    if lst:
        return {"error": {
            "error": {
                "status_code": 404,
                "message": "List name already exists",
                "details": "Lists with same name cannot be create"
            },
            "success": False
        }}
    await List_Details.filter(list_id=id).update(list_title=nme, list_modified=datetime.now())
    return {"data": "list details updated",
                          "success":True}


async def manager_delete_list(request, token):
    name = request.json.get("name", None)
    user_id = token.identity
    lst = await List_Details.get_or_none(user_id=user_id, list_title=name)
    if lst is None:
        return {"error": {
            "error": {
                "status_code": 404,
                "message": "List does not exist",
                "details": "List which is not present, cant be deleted"
            },
            "success": False
        }}
    await List_Details.filter(list_id=lst.list_id).delete()
    return {"data": f"List {name} deleted",
                          "success":True}