# from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Task
from rest_framework.test import APIClient
from rest_framework import status

class TaskModelTest(TestCase):
    def test_task_str(self):
        task = Task.objects.create(title="Test Task")
        self.assertEqual(str(task), "Test Task")

class TaskAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.task_data = {
            "title": "Test Task",
            "description": "This is a test task.",
            "completed": False,
            "due_date": "2024-12-31T23:59:59Z",
            "priority": 1,
        }

    def test_create_task(self):
        response = self.client.post('/api/tasks/', self.task_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, "Test Task")

    def test_get_tasks(self):
        Task.objects.create(**self.task_data)
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_task_detail(self):
        task = Task.objects.create(**self.task_data)
        response = self.client.get(f'/api/tasks/{task.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Test Task")

    def test_update_task(self):
        task = Task.objects.create(**self.task_data)
        updated_data = {"title": "Updated Test Task"}
        response = self.client.put(f'/api/tasks/{task.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        task.refresh_from_db()
        self.assertEqual(task.title, "Updated Test Task")

    def test_delete_task(self):
        task = Task.objects.create(**self.task_data)
        response = self.client.delete(f'/api/tasks/{task.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)
