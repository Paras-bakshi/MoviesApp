from sanic import Blueprint, response
from sanic_jwt_extended import jwt_required
from api.v1.managers import manager_title_details,manager_get_history,manager_id_details,manager_all_details

searches = Blueprint("search", url_prefix="/search")


@searches.get("/")
@jwt_required
async def title_details(request, token):
    # url = f"http://www.omdbapi.com/?apikey=12c8ec51"
    # src = ""
    # for key, value in request.args.items():
    #     if key == "title":
    #         src = value[0]
    #         url += f"&s={value[0]}"
    #     elif key == "year":
    #         url += f"&y={value[0]}"
    #     elif key == "type":
    #         url += f"&type={value[0]}"
    #     elif key == "page":
    #         url += f"&page={value[0]}"
    #
    # res = urlopen(url)
    # json_data = json.loads(res.read())
    # data=json_data["Search"]
    # await History.create(user_id=token.identity, hist=src)
    # return response.json({"data":data,
    #                      "success":True})

    res = await manager_title_details(request,token)
    return response.json(res)


@searches.get("/id/<ids>")
@jwt_required
async def id_details(request, token, ids):
    # url = f"http://www.omdbapi.com/?apikey=12c8ec51&i={ids}"
    # res = urlopen(url)
    # json_data = json.loads(res.read())
    # data=json_data
    # await History.create(user_id=token.identity, hist=ids)
    # return response.json({"data":data,
    #                      "success":True})

    res = await manager_id_details(request,token,ids)
    return response.json(res)


@searches.get("/all/")
@jwt_required
async def all_details(request, token):
    # url = f"http://www.omdbapi.com/?apikey=12c8ec51"
    # src = ""
    # for key, value in request.args.items():
    #     if key == "title":
    #         src = value[0]
    #         url += f"&s={value[0]}"
    #     elif key == "year":
    #         url += f"&y={value[0]}"
    #     elif key == "type":
    #         url += f"&type={value[0]}"
    #     elif key == "page":
    #         url += f"&page={value[0]}"
    #
    # res = urlopen(url)
    # json_data = json.loads(res.read())
    # json_search = json_data['Search']
    # data = await extra_func(json_search)
    # await History.create(user_id=token.identity, hist=src)
    # return response.json({"data":data,
    #                      "success":True})

    res = await manager_all_details(request,token)
    return response.json(res)


# async def get_tasks(session, data):
#     # tasks = []
#     # for rw in data:
#     omdbId = data['imdbID']
#     url = f"http://www.omdbapi.com/?i={omdbId}&apikey=4c92cc0a"
#     return session.get(url, ssl=False)
#     # return tasks
#
#
# async def extra_func(data):
#     async with aiohttp.ClientSession() as session:
#         tasks = await asyncio.gather(
#             *[get_tasks(session, movie) for movie in data]
#         )
#         responses = await asyncio.gather(*tasks)
#
#         lsc = []
#         for res in responses:
#             data1 = await res.json()
#             lsc.append(data1)
#         return lsc


@searches.get("/history")
@jwt_required
async def get_history(request, token):
    # user_id = token.identity
    # hist = await History.filter(user_id=user_id)
    # lst = []
    # for his in hist:
    #     lst.append(his.hist)
    # return response.json({"data":lst,
    #                       "success":True})

    res = await manager_get_history(request,token)
    return response.json(res)


