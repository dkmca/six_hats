from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=255, null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'users'
