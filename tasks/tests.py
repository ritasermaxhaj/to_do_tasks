from django.test import TestCase
from django.contrib.auth.models import User
from tasks.models import Task
from django.urls import reverse

# Create your tests here.
class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.task = Task.objects.create(
            title='Test Task',
            user=self.user,
            due_date='2025-05-06',
            is_completed=False,
            comment='This is a test task.'
        )

    def test_task_creation(self):
        self.assertEqual(self.task.title, 'Test Task')
        self.assertEqual(self.task.user.username, 'testuser')
        self.assertEqual(str(self.task.due_date), '2025-05-06')
        self.assertFalse(self.task.is_completed)
        self.assertEqual(self.task.comment, 'This is a test task.')

class TaskViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_task_creation_view(self):
        response = self.client.post(reverse('task_create'), {
            'title': 'New Task',
            'due_date': '2025-05-06',
            'is_completed': False,
            'comment': 'This is a new task.'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 1)
        
    def test_delete_task_view(self):
        task = Task.objects.create(user=self.user, title='Task to delete', comment='Delete this task', due_date='2025-05-06')
        response = self.client.post(reverse('task_delete', args=[task.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 0)