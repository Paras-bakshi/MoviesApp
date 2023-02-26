import os
from urllib.request import urlopen
import json
import aiohttp
import asyncio
from api.v1.models import History

URL = f"http://www.omdbapi.com/?apikey={os.getenv('API_KEY')}"

async def manager_title_details(request, token):
    url = URL
    src = ""

    for key, value in request.args.items():
        if key == "title":
            src = value[0]
            url += f"&s={value[0]}"
        elif key == "year":
            url += f"&y={value[0]}"
        elif key == "type":
            url += f"&type={value[0]}"
        elif key == "page":
            url += f"&page={value[0]}"

    await History.create(user_id=token.identity, hist=src)
    res = urlopen(url)
    json_data = json.loads(res.read())
    if json_data['Response'] == "True" :
        data = json_data["Search"]
        return {"data": data, "success": True}
    else:
        return {"error": {
            "status_code": 404,
            "message": json_data["Error"]},
            "success": False}


async def manager_id_details(request, token, ids):
    url = URL+f"&i={ids}"
    res = urlopen(url)
    json_data = json.loads(res.read())
    await History.create(user_id=token.identity, hist=ids)
    if json_data['Response'] == "True" :
        return {"data":json_data, "success":True}
    else :
        return {"error": {
            "status_code": 404,
            "message": json_data["Error"]},
            "success": False}


async def manager_all_details(request, token):
    url = URL
    src = ""
    for key, value in request.args.items():
        if key == "title":
            src = value[0]
            url += f"&s={value[0]}"
        elif key == "year":
            url += f"&y={value[0]}"
        elif key == "type":
            url += f"&type={value[0]}"
        elif key == "page":
            url += f"&page={value[0]}"

    await History.create(user_id=token.identity, hist=src)
    res = urlopen(url)
    json_data = json.loads(res.read())
    print(json_data)
    if json_data['Response'] == "True":
        json_search = json_data['Search']
        data = await extra_func(json_search)
        return {"data":data, "success":True}
    else :
        return {"error": {
            "status_code": 404,
            "message": json_data["Error"]},
            "success": False}

async def get_tasks(session, data):
    # tasks = []
    # for rw in data:
    omdbId = data['imdbID']
    # url = f"http://www.omdbapi.com/?i={omdbId}&apikey=4c92cc0a"
    url = URL+f"&i={omdbId}"
    return session.get(url, ssl=False)
    # return tasks


async def extra_func(data):
    async with aiohttp.ClientSession() as session:
        tasks = await asyncio.gather(
            *[get_tasks(session, movie) for movie in data]
        )
        responses = await asyncio.gather(*tasks)

        lsc = []
        for res in responses:
            data1 = await res.json()
            lsc.append(data1)
        return lsc


async def manager_get_history(request, token):
    user_id = token.identity
    hist = await History.filter(user_id=user_id)
    lst = []
    for his in hist:
        lst.append(his.hist)
    return {"data":lst, "success":True}