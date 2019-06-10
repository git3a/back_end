from User.models import UserInfo

def insert(request):
	guser = request.GET.get("user")
	gemail = request.GET.get("email")
	gpassword = request.GET.get("password")
	data = UserInfo(guser = guser, pwd = gpassword, email = gpassword);
	data.save()