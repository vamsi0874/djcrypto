from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE,related_name='notes')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    
class Coin(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE,related_name='coins')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
