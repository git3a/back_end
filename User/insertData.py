from User.models import UserInfo
from User.models import UserFavorite
from User.models import UserList
from User.models import UserRecipe

from django.http import HttpResponse
def insertUser(request):

	guser = request.GET.get("user")
	gemail = request.GET.get("email")
	gpassword = request.GET.get("password")
	data = UserInfo(user = guser, pwd = gpassword, email = gemail);
	data.save()
	return HttpResponse()

def insertUserImage(request):
	userid = request.GET.get('userid')
	url = request.GET.get("url")
	user = UserInfo.objects.get(id=userid)
	user.touxiang = url
	user.save()
	return HttpResponse()
	
def insertFavorite(request):
	userid = request.GET.get('userid')
	recipeid = request.GET.get('recipeid')
	data = UserFavorite(userId = userid, recipeId = recipeid)
	data.save()
	return HttpResponse()
	
	
def insertList(request):
	
	userid = request.GET.get('userid')
	recipeid = request.GET.get('recipeid')
	print(userid)
	print(recipeid)
	data = UserList(userId = userid, recipeId = recipeid)
	data.save()
	return HttpResponse()

def insertRecipe(request):

	recipename = request.GET.get("name")
	recipematerial = request.GET.get("material")
	recipestep = request.GET.get("steps")
	print(recipename)
	print(recipematerial)
	print(recipestep)
	data = UserRecipe(name=recipename, material= recipematerial, steps=recipestep)
	data.save()
	return HttpResponse()
