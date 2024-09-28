from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet
from .schema import schema
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView



router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
]
