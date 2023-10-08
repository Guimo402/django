from django.db import models
from django.contrib.auth.models import User

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.URLField(max_length=256, blank=True)
    
    def __str__(self): # 这个函数的作用是用户名是什么
        return str(self.user)
