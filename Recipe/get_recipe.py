from django.http import HttpResponse
from Recipe.models import Recipe
from User.models import UserInfo
from django.core.serializers.json import DjangoJSONEncoder

import json
import random

class UserEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,UserInfo):
            return obj.user
        return json.JSONEncoder.default(self,obj)

def getRandonRecipe(request):
    #recipe_list = []
	recipe_dict = {'id':[],'name':[], 'image':[]}
	h = set()
	while (len(h) < 6):
		h.add(random.randint(1,100))
	for index in h:
		
		recipes = Recipe.objects.filter(id = index)
		for recipe in recipes:
			#recipe_dict = {}
			#recipe_dict['recipeid'] = recipe.recipeid
			recipe_dict['id'].append(recipe.id)
			recipe_dict['name'].append(recipe.name)
			recipe_dict['image'].append(recipe.image)
		
	return HttpResponse(json.dumps(recipe_dict,cls=UserEncoder,ensure_ascii=False), content_type="application/json")

def getRecipeById(request):
    #recipe_list = []
	recipe_dict = {}
	index = request.GET.get("id")
	recipes = Recipe.objects.filter(id = index)
	for recipe in recipes:
		#recipe_dict = {}
		#recipe_dict['recipeid'] = recipe.recipeid
		recipe_dict['id'] = (recipe.id)
		recipe_dict['name'] = (recipe.name)
		recipe_dict['image'] = (recipe.image)
		recipe_dict['material'] = (recipe.material)
		recipe_dict['amount'] = (recipe.amount)
		recipe_dict['step'] = (recipe.step)
		recipe_dict['time'] = recipe.time
		#recipe_dict['User'] = recipe.User
		#recipe_list.append(recipe_dict)
		#print(recipe_dict['userid'])
	#return HttpResponse(json.dump(recipe_list, ensure_ascii=False),)
	return HttpResponse(json.dumps(recipe_dict,cls=UserEncoder,ensure_ascii=False), content_type="application/json")

def getRecipeByName(request):

	recipe_dict = {'id':[],'name':[], 'image':[]}
	searchWord = request.GET.get("searchWord")
	print(searchWord)
	recipes = Recipe.objects.filter(name__contains = searchWord)
	for recipe in recipes:
		recipe_dict['id'].append(recipe.id)
		recipe_dict['name'].append(recipe.name)
		recipe_dict['image'].append(recipe.image)
	#return HttpResponse(json.dump(recipe_list, ensure_ascii=False),)
	return HttpResponse(json.dumps(recipe_dict,cls=UserEncoder,ensure_ascii=False), content_type="application/json")

