from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
# Create your models here.


class role(models.Model):
    roleid = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class user(AbstractUser):
    username = None
    email = models.EmailField(primary_key=True)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    roleid = models.ForeignKey(role, on_delete=models.CASCADE, default=1)
    is_active = models.BooleanField(default=False)
    
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
