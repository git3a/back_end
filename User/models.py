from django.db import models

# Create your models here.

class UserInfo(models.Model):

    #userid = models.CharField(max_length=100)
    user = models.CharField(max_length=100,unique=True)
    pwd = models.CharField(max_length=100)
    email = models.EmailField(unique=True,default="@")
    #sex = models.CharField(max_length=32, choices=gender, default="男")

    def __str__(self):
        return self.user
