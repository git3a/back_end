from django.db import models
# Create your models here.

class UserInfo(models.Model):

	#userid = models.CharField(max_length=100)
	user = models.CharField(max_length=100,unique=True)
	pwd = models.CharField(max_length=100)
	email = models.EmailField(unique=True,default="@")
	touxiang = models.CharField(max_length = 100,default="")
	#sex = models.CharField(max_length=32, choices=gender, default="男")

class UserFavorite(models.Model):
	userId = models.BigIntegerField()
	recipeId = models.BigIntegerField()
	
	
class UserList(models.Model):
	userId = models.BigIntegerField()
	recipeId = models.BigIntegerField()


class UserRecipe(models.Model):
	# Recipeid: INTEGRAL型で，主キー

	# recipeid = models.IntegerField(primary_key=True)
	# 名前：文字列100桁
	name = models.TextField()
	# 図
	#image = models.TextField()
	# material
	material = models.TextField()
	# 量
	#amount = models.TextField()
	# ステップ
	steps = models.TextField()
	#time = models.TextField()