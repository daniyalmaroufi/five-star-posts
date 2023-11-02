from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    score = models.IntegerField(default=0)
    scores_count=models.BigIntegerField(default=0)


class Score(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='user')
    post = models.ForeignKey(Post,on_delete=models.CASCADE,null=True,related_name='post')
    score = models.IntegerField(default=0)
