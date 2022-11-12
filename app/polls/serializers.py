from rest_framework import serializers
from .models import User, Competition, Registration, Osoba, Druzyna

class UserSerializer(serializers.Serializer):
    iduser = serializers.IntegerField(required=True)
    email = serializers.CharField(max_length=200, required=True)
    password = serializers.CharField(max_length=45, required=True)
    firstname = serializers.CharField(max_length=45, required=True)
    lastname = serializers.CharField(max_length=45, required=True)
    age = serializers.IntegerField(required=True)
    gender = serializers.CharField(max_length=45, required=True)

    def create(self, validated_data):
        return User.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.iduser = validated_data.get('iduser', instance.iduser)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.firstname = validated_data.get('firstname', instance.firstname)
        instance.lastname = validated_data.get('lastname', instance.lastname)
        instance.age = validated_data.get('age', instance.age)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.save()
        return instance
class CompetitionSerializer(serializers.Serializer):
    idcompetition = serializers.IntegerField(required=True)
    city = serializers.CharField(max_length=45, required=True)
    street = serializers.CharField(max_length=45, required=True)
    date = serializers.DateField(required=True)
    description = serializers.CharField(max_length=255)
    def create(self, validated_data):
        return Competition.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.idcompetition = validated_data.get('idcompetition', instance.idcompetition)
        instance.city = validated_data.get('city', instance.city)
        instance.street = validated_data.get('street', instance.street)
        instance.date = validated_data.get('date', instance.date)
        instance.description = validated_data.get('description', instance.description)
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