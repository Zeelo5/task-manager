
# from django.db import models

# class Task(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     completed = models.BooleanField(default=False)

#     def __str__(self):
#         return self.title


from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)
    priority = models.IntegerField(default=1)
    # created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title