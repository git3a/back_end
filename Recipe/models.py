import json

from django.db import models


class UserEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UserInfo):
            return obj.name
        return json.JSONEncoder.default(self, obj)


# Create your models here.

class Recipe(models.Model):
    # Recipeid: INTEGRAL型で，主キー
    # recipeid = models.IntegerField(primary_key=True)
    userid = models.ForeignKey('User.UserInfo',on_delete=models.CASCADE)

    # 名前：文字列100桁
    name = models.TextField()
    # 図
    image = models.TextField()
    # material
    material = models.TextField()
    # 量
    amount = models.TextField()
    # ステップ
    step = models.TextField()
    # 時間
    time = models.TextField()
