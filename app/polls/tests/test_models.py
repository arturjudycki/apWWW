from django.test import TestCase

from ..models import Osoba, Druzyna


class OsobaModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Osoba.objects.create(imie='Juraj', nazwisko='Janosik')
        Osoba.objects.create(imie='Sherlock', nazwisko='Holmes')

    def test_first_name_label(self):
        osoba = Osoba.objects.get(id=1)
        field_label = osoba._meta.get_field('imie').verbose_name
        self.assertEqual(field_label, 'imie')

    def test_first_name_max_length(self):
        osoba = Osoba.objects.get(id=1)
        max_length = osoba._meta.get_field('imie').max_length
        self.assertEqual(max_length, 45)

    def test_osoba_different_id(self):
        juraj = Osoba.objects.get(imie="Juraj")
        sherlock = Osoba.objects.get(imie="Sherlock")
        self.assertEqual(sherlock.id - juraj.id, 1)

class DruzynaModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Druzyna.objects.create(nazwa='IMDB FC', kraj='UK')
        Druzyna.objects.create(nazwa='Filmweb FC', kraj='PL')

    def test_druzyna_different_id(self):
        imdb = Druzyna.objects.get(kraj="UK")
        filmweb = Druzyna.objects.get(kraj="PL")
        self.assertEqual(filmweb.id - imdb.id, 2)