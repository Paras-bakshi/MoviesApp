from sanic import Sanic, Blueprint
from tortoise.contrib.sanic import register_tortoise
import json
from api import api
from sanic_jwt_extended import JWT
from dotenv import load_dotenv
import os

load_dotenv()


app = Sanic(__name__)
app.blueprint(api)

register_tortoise(
    app,
    db_url=f"{os.getenv('DATABASE')}://{os.getenv('USERNAME')}:{os.getenv('PASSWORD')}@{os.getenv('HOST')}:{os.getenv('PORT')}/{os.getenv('DB')}",
    modules={"models": ["api.v1.models"]},
    generate_schemas=True
)

with JWT.initialize(app) as manager:
    manager.config.secret_key = os.getenv('SECRET')
    manager.config.use_blacklist = True


if __name__ == '__main__':
    app.run(debug=True)
