from django.db import models
from django.contrib.auth.models import User


class BaseNote(models.Model):
    title = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # def __str__(self):
    #     return self