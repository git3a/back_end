from django.http import HttpResponse
from User.models import UserInfo
from django.core import serializers
import json


def get(request):
	#user_list = []
	guser = request.GET.get("user")
	user_dict = {}
	users = UserInfo.objects.filter(user = guser)
	for user in users:
		#user_dict = {}
		#user_dict['userid'] = user.userid
		user_dict['user'] = user.user
		user_dict['pwd'] = user.pwd
		user_dict['email'] = user.email
		#user_dict['sex'] = user.sex

	
	return HttpResponse(json.dumps(user_dict,ensure_ascii=False),content_type="application/json")

