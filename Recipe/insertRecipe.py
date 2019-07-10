from django.http import HttpResponse
from Recipe.models import Recipe
import pymysql
from User.models import UserInfo

def insertRecipe(request):

    user_id = request.GET.get("user_id")
    user = UserInfo.objects.get(id=user_id) # Get user_id instance
    recipe_name = request.GET.get("name")
    recipe_image = request.GET.get("img_url")
    recipe_material = request.GET.get("material")
    recipe_amount = request.GET.get("amount")
    recipe_steps = request.GET.get("steps")
    recipe_time  = request.GET.get("time")
    data = Recipe(userid=user,name=recipe_name, image=recipe_image, material=recipe_material, amount=recipe_amount,
                  step=recipe_steps, time=recipe_time)

    data.save()
    return HttpResponse()



