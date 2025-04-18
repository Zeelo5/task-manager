# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import TaskViewSet
# from .schema import schema
# from django.views.decorators.csrf import csrf_exempt
# from graphene_django.views import GraphQLView



# router = DefaultRouter()
# router.register(r'tasks', TaskViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
#     path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
# ]


# from django.urls import path
# from graphene_django.views import GraphQLView
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import TaskViewSet, home
# from django.views.decorators.csrf import csrf_exempt

# router = DefaultRouter()
# router.register(r'tasks', TaskViewSet)

# urlpatterns = [
#     path("", home, name="home"),
#     path("api/", include(router.urls)),
#     path('tasks/', task_list, name='task_list'),
#     path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),
# ]


from django.views.decorators.csrf import csrf_exempt
from django.urls import path, include
from graphene_django.views import GraphQLView
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, home, task_list  # Import `task_list` if you need it

# Create a router and register the `TaskViewSet`
router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', home, name='home'),  # Home view for the app
    path('api/', include(router.urls)), 
      # Route for the API using the router
    path('tasks/', task_list, name='task_list'),
    # path('graphql/', GraphQLView.as_view(graphiql=True), name='graphql'),  # GraphQL endpoint
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True)), name='graphql'),

]
