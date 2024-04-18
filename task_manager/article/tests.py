from django.test import TestCase, Client
from task_manager.article.models import Users
from django.urls import reverse_lazy


class CreateUserTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_read(self):
        response = self.client.get('/users/create/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, reverse_lazy('user_create'))
        self.assertNotContains(response, reverse_lazy('logout'))

    def test_create(self):
        obj_count_before = Users.objects.count()
        Users.objects.create(
            first_name="Mia",
            last_name="Lukovic",
            username="Mia2013",
        )
        obj_count_after = Users.objects.count()
        self.assertEqual(obj_count_after, obj_count_before + 1)
        test_user = Users.objects.last()
        assert test_user.first_name == "Mia"


class UpdateUserTest(TestCase):

    def setUp(self):
        self.initial_data = {
            'first_name': 'Test Mia',
            'last_name': 'Test Lukovic'
        }
        self.updated_data = {
            'first_name': 'New Mia',
            'last_name': 'New Lukovic'
        }
        self.instance = Users.objects.create(**self.initial_data)

    def test_update_model(self):
        instance_from_db = Users.objects.get(id=self.instance.id)
        self.assertEqual(instance_from_db.first_name, self.initial_data['first_name'])
        self.assertEqual(instance_from_db.last_name, self.initial_data['last_name'])
        for key, value in self.updated_data.items():
            setattr(instance_from_db, key, value)
        instance_from_db.save()
        updated_instance_from_db = Users.objects.get(id=self.instance.id)
        self.assertEqual(updated_instance_from_db.first_name, self.updated_data['first_name'])
        self.assertEqual(updated_instance_from_db.last_name, self.updated_data['last_name'])


class DeleteUserTest(TestCase):

    def setUp(self):
        self.initial_data = {
            'first_name': 'Test Mia',
            'last_name': 'Test Lukovic'
        }
        self.instance = Users.objects.create(**self.initial_data)

    def test_delete_model(self):
        self.assertTrue(Users.objects.filter(id=self.instance.id).exists())
        self.instance.delete()
        self.assertFalse(Users.objects.filter(id=self.instance.id).exists())


class MyTest(TestCase):
    fixtures = ["users.json"]

    def test_check_user(self):
        user = Users.objects.get(pk=5)
        self.assertEqual(user.username, "Titika")


class TestLogin(TestCase):

    def setUp(self):
        self.client = Client()

    def test_get_login(self):
        response = self.client.get(reverse_lazy('login'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='login.html')

    def test_post_login_sucsess(self):
        self.data = {
            'username': 'test',
            'password': '123'
        }
        response = self.client.post(
            reverse_lazy('login'),
            self.data,
            follow=True
        )
        self.assertEqual(response.status_code, 200)
