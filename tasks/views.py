# # from django.shortcuts import render

# # Create your views here.
# from rest_framework import viewsets
# from .models import Task
# from .serializers import TaskSerializer

# class TaskViewSet(viewsets.ModelViewSet):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer


# # your_app_name/views.py
# from django.views.decorators.csrf import csrf_exempt
# from graphene_django.views import GraphQLView
# from django.urls import path
# from .schema import schema

# urlpatterns = [
#     path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
# ]

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, "tasks/home.html")

def task_list(request):
    tasks = Task.objects.all()
    return JsonResponse({"tasks": list(tasks.values())})

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer