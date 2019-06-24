from django.db import models
# Create your models here.

class UserInfo(models.Model):

	#userid = models.CharField(max_length=100)
	user = models.CharField(max_length=100,unique=True)
	pwd = models.CharField(max_length=100)
	email = models.EmailField(unique=True,default="@")
	touxiang = models.CharField(max_length = 100)
	#sex = models.CharField(max_length=32, choices=gender, default="男")

class UserFavorite(models.Model):
	userId = models.BigIntegerField()
	recipeId = models.BigIntegerField()
	
	
class UserList(models.Model):
	userId = models.BigIntegerField()
	recipeId = models.BigIntegerField()