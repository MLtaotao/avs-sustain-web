from django.test import RequestFactory, TestCase, Client
from django.test import Client as testclient
from django.contrib.auth.models import AnonymousUser, User


from .views import index, register_staff
from .models import *
from .forms import UserForm

# Create your tests here.

class IndexTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_index(self):
        # Create an instance of a GET request.
        request = self.factory.get('')

        # Or you can simulate an anonymous user by setting request.user to
        # an AnonymousUser instance.
        request.user = AnonymousUser()

        # Test my_view() as if it were deployed at /customer/details
        response = index(request)

        self.assertEqual(response.status_code, 200)



class ModelTest(TestCase):
    """docstring for ModelTest."""

    def setUp(self):
        self.user = User.objects.create_user(
            username = 'yutao', email = 'yutao@example.com', password = 'P@$$w0rd123'
        )

    def test_user_link_to_client(self):
        Client.objects.create(user = self.user)
        self.assertEqual(Client.objects.all().count(), 1)

    def test_user_link_to_staff(self):
        Staff.objects.create(user = self.user)
        self.assertEqual(Staff.objects.all().count(), 1)

    def test_user_link_to_conslutant(self):
        Consultant.objects.create(user = self.user)
        self.assertEqual(Consultant.objects.all().count(), 1)

    def test_user_link_to_conslutant1(self):
        Consultant.objects.create(user = self.user)
        self.assertEqual(Consultant.objects.all().count(), 1)
    def test_user_link_to_conslutant2(self):
        Consultant.objects.create(user = self.user)
        self.assertEqual(Consultant.objects.all().count(), 1)
    def test_user_link_to_conslutant3(self):
        Consultant.objects.create(user = self.user)
        self.assertEqual(Consultant.objects.all().count(), 1)
