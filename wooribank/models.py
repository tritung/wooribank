from django.db import models
from django.contrib.auth.models import User


from enum import IntEnum

class UserTypes(IntEnum):
    SALE = 0
    LEADER = 1
    ADMIN = 2
    
    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

class UserInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    type = models.IntegerField(choices=UserTypes.choices(), default=UserTypes.SALE)
    
    def __str__(self):
        return self.user.username