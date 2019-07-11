from django.db import models
# Create your models here.

class UserInfo(models.Model):

	#userid = models.CharField(max_length=100)
	user = models.CharField(max_length=64,unique=True)
	pwd = models.CharField(max_length=64)
	email = models.EmailField(unique=True,default="@")
	touxiang = models.TextField("")
	#sex = models.CharField(max_length=32, choices=gender, default="男")

class UserFavorite(models.Model):
	userId = models.BigIntegerField()
	recipeId = models.BigIntegerField()
	
	
class UserList(models.Model):
	userId = models.BigIntegerField()
	recipeId = models.BigIntegerField()

