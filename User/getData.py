from django.http import HttpResponse
from User.models import UserInfo
from User.models import UserFavorite
from User.models import UserList
from django.core import serializers
import json

class UserEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,UserInfo):
            return obj.user
        return json.JSONEncoder.default(self,obj)

def getUser(request):
	#user_list = []
	guser = request.GET.get("user")
	user_dict = {}
	users = UserInfo.objects.filter(user = guser)
	for user in users:
		#user_dict = {}
		user_dict['userId'] = str(user.id)
		user_dict['user'] = user.user
		user_dict['pwd'] = user.pwd
		user_dict['email'] = user.email
		user_dict['url'] = user.touxiang
		#user_dict['sex'] = user.sex

	
	return HttpResponse(json.dumps(user_dict,ensure_ascii=False),content_type="application/json")


def getFavorite(request):
	#user_list = []
	userid = request.GET.get("id")
	
	user_dict = {'favorite':[]}
	favorites = UserFavorite.objects.filter(userId = userid)
	for favorite in favorites:
		#user_dict = {}
		#user_dict['userid'] = user.userid
		user_dict['favorite'].append(str(favorite.recipeId))
		#user_dict['sex'] = user.sex
	return HttpResponse(json.dumps(user_dict,ensure_ascii=False),content_type="application/json")
    
def getList(request):
	userid = request.GET.get("id")
	print(userid)
	user_list = {'list':[]}
	lists = UserList.objects.filter(userId = userid)
	for list in lists:
		
		user_list['list'].append(str(list.recipeId))
	
	return HttpResponse(json.dumps(user_list,cls=UserEncoder,ensure_ascii=False), content_type="application/json")
