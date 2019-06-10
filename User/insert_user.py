from User.models import UserInfo
from django.http import HttpResponse
def insert(request):
	guser = request.GET.get("user")
	gemail = request.GET.get("email")
	gpassword = request.GET.get("password")
	data = UserInfo(user = guser, pwd = gpassword, email = gemail);
	data.save()
	return HttpResponse()