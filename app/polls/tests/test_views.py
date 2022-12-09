from django.test import TestCase, Client
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

from ..models import Osoba

class OsobaListViewTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/polls/osobas/')
        self.assertEqual(response.status_code, 403)

class OsobaTests(APITestCase):

    def test_create_osoba(self):
        self.client = APIClient()
        self.client.login(username='artur', password='123')
        url = '/polls/osobas/add/'
        data = {'imie': 'Ala', 'nazwisko': 'Kot', 'miesiac_urodzenia': 5}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Osoba.objects.count(), 1)
        self.assertEqual(Osoba.objects.get().name, 'Ala')

    def test_view_osoba(self):
        token = Token.objects.get(user__username='artur')
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        url = '/polls/osobas/1/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)