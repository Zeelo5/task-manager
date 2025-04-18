import graphene
from graphene_django.types import DjangoObjectType
from .models import Task

class TaskType(DjangoObjectType):
    class Meta:
        model = Task
        fields = "__all__" 

# class Query(graphene.ObjectType):
#     all_tasks = graphene.List(TaskType)

#     def resolve_all_tasks(root, info):
#         return Task.objects.all()


# schema.py (continued)
class Query(graphene.ObjectType):
    tasks = graphene.List(TaskType)  # Fetch all tasks
    task = graphene.Field(TaskType, id=graphene.Int())  # Fetch a task by ID

    def resolve_tasks(self, info):
        return Task.objects.all()  # Return all tasks

    def resolve_task(self, info, id):
        try:
            return Task.objects.get(pk=id)  # Return a task by ID
        except Task.DoesNotExist:
            return None  # Handle not found

# schema.py (continued)
class CreateTask(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=True)
        completed = graphene.Boolean()

    task = graphene.Field(TaskType)

    def mutate(self, info, title, description, completed=False):
        task = Task(title=title, description=description, completed=completed)
        task.save()
        return CreateTask(task=task)




class UpdateTask(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        description = graphene.String()
        completed = graphene.Boolean()

    task = graphene.Field(TaskType)

    def mutate(self, info, id, description=None, completed=None):
        task = Task.objects.get(pk=id)
        if description is not None:
            task.description = description
        if completed is not None:
            task.completed = completed
        task.save()
        return UpdateTask(task=task)



class DeleteTask(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        try:
            task = Task.objects.get(pk=id)
            task.delete()
            return DeleteTask(success=True)
        except Task.DoesNotExist:
            return DeleteTask(success=False)

# schema.py (continued)
class Mutation(graphene.ObjectType):
    create_task = CreateTask.Field()
    update_task = UpdateTask.Field()
    delete_task = DeleteTask.Field()

# schema.py (continued)
schema = graphene.Schema(query=Query, mutation=Mutation)
