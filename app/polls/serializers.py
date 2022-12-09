from rest_framework import serializers
from .models import Osoba, Druzyna
from datetime import datetime

class DruzynaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Druzyna
        fields = ['id', 'nazwa', 'kraj']
        read_only_fields = ['id']

class OsobaModelSerializer(serializers.ModelSerializer):
    wlasciciel = serializers.ReadOnlyField(source='wlasciciel.username')
    class Meta:
        model = Osoba
        fields = ['id', 'imie', 'nazwisko', 'miesiac_urodzenia', 'data_dodania', 'druzyna', 'wlasciciel']
        read_only_fields = ['id']

    def validate_imie(self, value):

        if not value.isalpha():
            raise serializers.ValidationError(
                "Imię może zawierać tylko litery.",
            )
        return value

    def validate_miesiac_urodzenia(self, value):

        if value > datetime.now().month:
            raise serializers.ValidationError(
                "Miesiąc urodzenia nie może być przyszłości.",
            )
        return value

