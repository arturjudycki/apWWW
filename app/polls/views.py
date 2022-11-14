from django.http import HttpResponse

from django.shortcuts import render
from rest_framework import status
from rest_framework import filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Osoba, Druzyna
from .serializers import OsobaModelSerializer, DruzynaModelSerializer

search_fields = ['imie']
filter_backends = (filters.SearchFilter)

@api_view(['GET'])
def osoba_list(request):
    if request.method == 'GET':
        osobas = Osoba.objects.all()
        serializer = OsobaModelSerializer(osobas, many=True)
        return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def osoba_detail(request, pk):

    try:
        osoba = Osoba.objects.get(pk=pk)
    except Osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OsobaModelSerializer(osoba)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OsobaModelSerializer(osoba, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        osoba.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def osoba_add(request):
    if request.method == 'POST':
        serializer = OsobaModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def osoba_detail_name(request, imie):

    try:
        osobas = Osoba.objects.all().filter(imie=imie)
    except Osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OsobaModelSerializer(osobas, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def druzyna_list(request):
    if request.method == 'GET':
        druzynas = Druzyna.objects.all()
        serializer = DruzynaModelSerializer(druzynas, many=True)
        return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def druzyna_detail(request, pk):

    try:
        druzyna = Druzyna.objects.get(pk=pk)
    except Druzyna.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DruzynaModelSerializer(druzyna)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DruzynaModelSerializer(druzyna, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        druzyna.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def druzyna_add(request):
    if request.method == 'POST':
        serializer = DruzynaModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")