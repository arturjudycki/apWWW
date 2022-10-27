from rest_framework import serializers
from .models import User, Competition, Registration, Osoba, Druzyna

class UserSerializer(serializers.Serializer):
    iduser = serializers.IntegerField(required=True, db_column='idUser', primary_key=True)
    email = serializers.CharField(max_length=200, required=True)
    password = serializers.CharField(max_length=45, required=True)
    firstname = serializers.CharField(max_length=45, db_column='firstName', required=True)
    lastname = serializers.CharField(max_length=45, db_column='lastName', required=True)
    age = serializers.IntegerField(required=True)
    gender = serializers.CharField(max_length=45, required=True)

    def create(self, validated_data):
        return User.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.iduser = validated_data.get('iduser', instance.name)
        instance.email = validated_data.get('email', instance.shirt_size)
        instance.password = validated_data.get('password', instance.miesiac_dodania)
        instance.firstname = validated_data.get('firstname', instance.team)
        instance.lastname = validated_data.get('lastname', instance.team)
        instance.age = validated_data.get('age', instance.team)
        instance.gender = validated_data.get('gender', instance.team)
        instance.save()
        return instance
class CompetitionSerializer(serializers.Serializer):
    idcompetition = serializers.IntegerField(required=True, db_column='idCompetition', primary_key=True)
    city = serializers.CharField(max_length=45, required=True)
    street = serializers.CharField(max_length=45, required=True)
    date = serializers.DateField(required=True)
    description = serializers.CharField(max_length=255)
    def create(self, validated_data):
        return Competition.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.idcompetition = validated_data.get('idcompetition', instance.name)
        instance.city = validated_data.get('city', instance.shirt_size)
        instance.street = validated_data.get('street', instance.miesiac_dodania)
        instance.date = validated_data.get('date', instance.team)
        instance.description = validated_data.get('description', instance.team)
        instance.save()
        return instance

class RegistrationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ['idregistration', 'status', 'idcompetition', 'iduser']

class OsobaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Osoba
        fields = ['id', 'imie', 'nazwisko', 'miesiac_urodzenia', 'data_dodania', 'druzyna']
        read_only_fields = ['id']

class DruzynaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Druzyna
        fields = ['id', 'nazwa', 'kraj']
        read_only_fields = ['id']