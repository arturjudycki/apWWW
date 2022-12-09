from django.test import TestCase

from ..models import Osoba


class OsobaModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Osoba.objects.create(imie='Juraj', nazwisko='Janosik')

    def test_first_name_label(self):
        osoba = Osoba.objects.get(id=1)
        field_label = osoba._meta.get_field('imie').verbose_name
        self.assertEqual(field_label, 'imie')

    def test_first_name_max_length(self):
        osoba = Osoba.objects.get(id=1)
        max_length = osoba._meta.get_field('imie').max_length
        self.assertEqual(max_length, 45)