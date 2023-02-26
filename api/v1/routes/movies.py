from sanic import Blueprint, response
from sanic_jwt_extended import jwt_required
from api.v1.managers import manager_add_movie,manager_remove_movie,manager_movies_in_list

movie = Blueprint("movies", url_prefix="/movies")


# POST api/v1/movies → Add a movie to a list
@movie.post("/")
@jwt_required
async def add_movie(request, token):
    # list_title = request.json.get("list", None)
    # movie_title = request.json.get("movie", None)
    # user_id = token.identity
    # lst = await List_Details.get_or_none(user_id=user_id, list_title=list_title)
    # if lst is None:
    #     return response.json({"error": {
    #         "status_code": 404,
    #         "message": "List not created",
    #         "details": "The name of list which is entered does not exist. Create the list first"},
    #     "success": False})
    # lst_det = await Lists.filter(list_id=lst.list_id, movie_title__iexact=movie_title)
    # print(lst_det)
    # if lst_det :
    #     return response.json({"error": {
    #         "status_code": 404,
    #         "message": "Movie already added",
    #         "details": "The movie is already added in the list specified."},
    #         "success": False})
    # url = f"http://www.omdbapi.com/?apikey=12c8ec51&t={movie_title}"
    # res = urlopen(url)
    # json_data = json.loads(res.read())
    # if json_data["Response"] == "True" :
    #     await Lists.create(list_id=lst.list_id, movie_title=json_data['Title'], movie_id=json_data['imdbID'])
    #     return response.json({"data": "Movie added in the specified list",
    #                           "success": True})
    # return response.json({"error": {
    #     "status_code": 404,
    #     "message": "No movie with this name",
    #     "details": "No movie exist with the specified name in the omdb api."},
    #     "success": False})
    res = await manager_add_movie(request, token)
    return response.json(res)


# DELETE api/v1/movies → Remove a movie from a list
@movie.delete("/")
@jwt_required
async def remove_movie(request, token):
    # list_title = request.json.get("list", None)
    # movie_title = request.json.get("movie", None)
    # user_id = token.identity
    # lst = await List_Details.get_or_none(user_id=user_id, list_title=list_title)
    # if lst is None:
    #     return response.json({"error": {
    #         "status_code": 404,
    #         "message": "List not created",
    #         "details": "The name of list which is entered does not exist. Create the list first"},
    #         "success": False})
    # mov = await Lists.get_or_none(list_id=lst.list_id,movie_title__iexact=movie_title)
    # if mov is None:
    #     return response.json({"error": {
    #         "status_code": 404,
    #         "message": "Movie not present",
    #         "details": "The movie is not present in the list specified."},
    #         "success": False})
    # await Lists.filter(list_id=lst.list_id,movie_title__iexact=movie_title).delete()
    # return response.json({"data": "Movie removed from specified list",
    #                       "success": True})

    res = await manager_remove_movie(request, token)
    return response.json(res)


# GET api/v1/movies/?list_name=<list_name>  → get a list of all the movies in a list
@movie.get("/")
@jwt_required
async def movies_in_list(request, token):
    # list_name = request.args["list_name"]
    # user_id = token.identity
    # lst = await List_Details.get_or_none(user_id=user_id, list_title=list_name[0])
    # if lst is None:
    #     return response.json({"error": {
    #         "status_code": 404,
    #         "message": "List not created",
    #         "details": "The name of list which is entered does not exist. Create the list first"},
    #         "success": False})
    # details = await Lists.filter(list_id=lst.list_id)
    # lst_details = []
    # for obj in details:
    #     ls = {}
    #     ls["movie_title"] = obj.movie_title
    #     ls["imdbID"] = obj.movie_id
    #     lst_details.append(ls)
    # return response.json({"data": lst_details,
    #                       "success": True})

    res = await manager_movies_in_list(request, token)
    return response.json(res)
