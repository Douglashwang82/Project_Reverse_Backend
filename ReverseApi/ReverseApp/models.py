from django.db import models

# Create your models here.
class Topics(models.Model):
    TopicId = models.AutoField(primary_key=True)
    TopicContent = models.CharField(max_length=500)
    TotalVote = models.IntegerField(default=0)
    YesVote = models.IntegerField(default=0)


class Users(models.Model):
    UserId = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length = 30)
    UserPassword = models.CharField(max_length = 30)
    UserAvatarFileName = models.CharField(max_length=500)
    DateOfJoing = models.DateField()

    
class Comments(models.Model):
    CommentId = models.AutoField(primary_key=True)
    DateOfComment = models.DateField()
    CommentContent = models.CharField(max_length=500)
    UserName = models.CharField(max_length = 30, blank=True)
    