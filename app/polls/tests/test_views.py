from django.test import TestCase, Client

from ..models import Osoba

class OsobaListViewTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/polls/osobas/')
        self.assertEqual(response.status_code, 403)