from django.http import HttpResponse
from Recipe.models import Recipe
from User.models import UserInfo
from django.core.serializers.json import DjangoJSONEncoder

import json

class UserEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,UserInfo):
            return obj.user
        return json.JSONEncoder.default(self,obj)

def get(request):
    #recipe_list = []
    recipe_dict = {}
    recipes = Recipe.objects.all()[:1]
    for recipe in recipes:
        #recipe_dict = {}
        #recipe_dict['recipeid'] = recipe.recipeid
        recipe_dict['name'] = recipe.name
        recipe_dict['image'] = recipe.image
        recipe_dict['material'] = recipe.material
        recipe_dict['amount'] = recipe.amount
        recipe_dict['step'] = recipe.step
        #recipe_dict['User'] = recipe.User
        #recipe_list.append(recipe_dict)
        #print(recipe_dict['userid'])
    #return HttpResponse(json.dump(recipe_list, ensure_ascii=False),)
    return HttpResponse(json.dumps(recipe_dict,cls=UserEncoder,ensure_ascii=False), content_type="application/json")

