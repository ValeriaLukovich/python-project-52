from django.test import TestCase
from task_manager.statuses.models import Status
from task_manager.article.models import Users
from django.urls import reverse


class StatusCRUDTest(TestCase):
    def setUp(self):
        self.status = Status.objects.create(name='Winter')
        self.user = Users.objects.create_user(username='testuser', password='password123')
        self.client.login(username='testuser', password='password123')

    def test_create(self):
        initial_count = Status.objects.count()
        new_status = {
            'name': 'Spring',
        }
        response = self.client.post(reverse('status_create'), data=new_status)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Status.objects.count(), initial_count + 1)

    def test_read(self):
        response = self.client.get(reverse('statuses'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.status.name)

    def test_update(self):
        updated_status = {
            'name': 'Summer',
        }
        response = self.client.post(
            reverse('status_update', args=[self.status.pk]), data=updated_status
        )
        self.assertEqual(response.status_code, 302)
        self.status.refresh_from_db()
        self.assertEqual(self.status.name, updated_status['name'])

    def test_delete(self):
        initial_count = Status.objects.count()
        response = self.client.post(reverse('status_delete', args=[self.status.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Status.objects.count(), initial_count - 1)
