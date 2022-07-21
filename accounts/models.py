from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(max_length=150, unique=True)
    name = models.CharField(null=True, blank=True, max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'username', 'password']