from rest_framework import serializers
from ReverseApp.models import Users, Topics, Comments

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topics
        fields = ("TopicId", "TopicContent", "TotalVote", "YesVote")

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ("UserId", "UserName", "UserPassword", "UserAvatarFileName", "DateOfJoing")

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ("CommentId", "DateOfComment", "CommentContent", "UserId")