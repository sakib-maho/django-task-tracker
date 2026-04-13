from django.test import Client, TestCase
from django.urls import reverse

from .models import Task


class TaskModelTests(TestCase):
    def test_create_task_defaults(self):
        task = Task.objects.create(title="Write tests")
        self.assertEqual(task.status, Task.Status.TODO)
        self.assertEqual(task.priority, Task.Priority.MEDIUM)


class TaskViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_task_create_and_list(self):
        create_url = reverse("task_create")
        response = self.client.post(
            create_url,
            {
                "title": "Build feature",
                "description": "Implement task tracker",
                "status": Task.Status.IN_PROGRESS,
                "priority": Task.Priority.HIGH,
            },
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Task.objects.count(), 1)
        self.assertContains(response, "Build feature")

    def test_api_task_list(self):
        Task.objects.create(title="Task A")
        response = self.client.get(reverse("api_task_list"))
        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(len(payload["data"]), 1)
