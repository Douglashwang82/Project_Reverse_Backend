import json
from math import fabs
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ReverseApp.models import Topics, Users, Comments
from ReverseApp.serializers import TopicSerializer, UserSerializer, CommentSerializer
from django.core.files.storage import default_storage

# Create your views here.
@csrf_exempt
def topicApi(request,id = 0):
    if request.method == 'GET':
        topics = Topics.objects.all()
        topics_serializer = TopicSerializer(topics, many = True)
        return JsonResponse(topics_serializer.data, safe = False)
    elif request.method == 'POST':
        topics_data = JSONParser().parse(request)
        topics_serializer = TopicSerializer(data = topics_data)
        if topics_serializer.isvalid():
            topics_serializer.save()
            return JsonResponse("Added Successfully:Topic", safe = False)
        return JsonResponse("Fail to Add:Topic", safe = False)
    elif request.method == 'PUT':
        topic_data = JSONParser().parse(request)
        topic = Topics.object.get(TopicId = topic_data['TopicId'])
        topics_serializer = TopicSerializer(topic, data = topic_data)
        if topics_serializer.is_valid():
            topics_serializer.save()
            return JsonResponse("Updated Successfully:Topic", safe = False)
        return JsonResponse("Faild to Update:Topic", safe = False)
    elif request.method == 'DELETE':
        topic=Topics.objects.get(TopicId=id)
        topic.delete()
        return JsonResponse("Deleted Successfully:Topic",safe=False)


@csrf_exempt
def userApi(request,id = 0):
    if request.method == 'GET':
        users = Users.objects.all()
        user_serializer = UserSerializer(users, many = True)
        return JsonResponse(user_serializer.data, safe = False)
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data = user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Added Successfully:User", safe = False)
    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        user = Users.object.get(UserId = user_data['UserId'])
        user_serializer = UserSerializer(user, data = user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Updated Successfully: User", safe = False)
        return JsonResponse("Fail to Update:User")
    elif request.method == 'DELETE':
        user = Users.objects.get(UserId = id)
        user.delete()
        return JsonResponse("Deleted Successfully:User", safe = False)


@csrf_exempt
def commentApi(request,id = 0):
    if request.method == 'GET':
        comments = Comments.objects.all()
        comment_serializer = CommentSerializer(comments, many = True)
        return JsonResponse(comment_serializer.data, safe = False)
    elif request.method == 'POST':
        comment_data = JSONParser().parse(request)
        comment_serializer = CommentSerializer(data = comment_data)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return JsonResponse("Added Successfully: Comment", safe = False)
        return JsonResponse("Fail to Update: Commnet", safe = False)
    elif request.method == 'PUT':
        comment_data = JSONParser().parse(request)
        comment = Comments.objects.get(CommentId = comment_data["CommentId"])
        comment_serializer = CommentSerializer(comment, data = comment_data)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return JsonResponse("Updated Successfully:Comment")
        return JsonResponse("Fail to Update:Comment", safe = False)
    elif request.method == 'DELETE':
        comment = Comments.objects.get(CommentId = id)
        comment.delete()
        return JsonResponse("Deleted Successfully: Comment", safe = False)

@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)