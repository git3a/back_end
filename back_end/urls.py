"""back_end URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Recipe import get_recipe
from Recipe import insertRecipe
from User import getData
from User import insertData


from image import uploadImage
#from User import get_user

urlpatterns = [
	path('admin/', admin.site.urls),
	path('getrecipe/', get_recipe.getRandonRecipe),
	path('getrecipebyid/', get_recipe.getRecipeById),
	path('getrecipebyUserid/', get_recipe.getRecipeByUserId),
	path('getrecipebyname/', get_recipe.getRecipeByName),
	path('getuser/', getData.getUser),
    path('getFavoriteRecipeId/', getData.getFavorite),
	path('insert/', insertData.insertUser),
	path('insertList/', insertData.insertList), 
	path('insertFavorite/', insertData.insertFavorite),
	path('insertTouxing/', insertData.insertUserImage),
	path('insertRecipe/', insertRecipe.insertRecipe),
	path('getList/', getData.getList),
	path('uploadImage/', uploadImage.uploadImage),
]
