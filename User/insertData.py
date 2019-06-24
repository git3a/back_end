from User.models import UserInfo
from User.models import UserFavorite
from User.models import UserList

from django.http import HttpResponse
def insertUser(request):

	guser = request.GET.get("user")
	gemail = request.GET.get("email")
	gpassword = request.GET.get("password")
	data = UserInfo(user = guser, pwd = gpassword, email = gemail);
	data.save()
	return HttpResponse()
	
def insertFavorite(request):
	userid = request.GET.get('userid')
	recipeid = request.GET.get('recipeid')
	data = UserFavorite(usertId = userid, recipeId = recipeid)
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