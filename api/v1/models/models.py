from tortoise import fields
from tortoise.models import Model
from uuid import uuid4


class Users(Model):
    user_id = fields.CharField(pk=True, max_length=36, default=uuid4())
    email = fields.CharField(unique=True, max_length=30, null=False)
    password_hash = fields.CharField(max_length=150, null=False)
    first_name = fields.CharField(max_length=30, null=False)
    last_name = fields.CharField(max_length=30, null=False)
    user_created = fields.DatetimeField(auto_now_add=True)

    def __json__(self):
        return {
            'user_id': self.user_id
        }

    def to_dict(self):
        return {
            'user_id': self.user_id
        }


class List_Details(Model):
    user = fields.ForeignKeyField('models.Users', on_delete=fields.CASCADE, related_name="lists_details")
    list_id = fields.CharField(pk=True, max_length=36, default=uuid4())
    list_title = fields.CharField(max_length=30, null=False)
    list_created = fields.DatetimeField(auto_now_add=True)
    list_modified = fields.DatetimeField(auto_now=True)


class Lists(Model):
    list = fields.ForeignKeyField('models.List_Details', on_delete=fields.CASCADE, related_name="lists")
    movie_id = fields.CharField(max_length=30, null=False)
    movie_title = fields.CharField(max_length=200, null=False)


class History(Model):
    user = fields.ForeignKeyField('models.Users', on_delete=fields.CASCADE, related_name="user_history")
    hist = fields.CharField(max_length=60, null=False)
    time_searched = fields.DatetimeField(auto_now_add=True)
