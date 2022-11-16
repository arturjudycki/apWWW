from django.http import HttpResponse

from django.shortcuts import render
from rest_framework import status
from rest_framework import filters
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Osoba, Druzyna
from .serializers import OsobaModelSerializer, DruzynaModelSerializer

from django.http import Http404
from rest_framework.views import APIView

from django_filters.rest_framework import DjangoFilterBackend

@api_view(['GET'])
def osoba_list(request):
    if request.method == 'GET':
        osobas = Osoba.objects.all()
        serializer = OsobaModelSerializer(osobas, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def osoba_detail(request, pk):

    try:
        osoba = Osoba.objects.get(pk=pk)
    except Osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        osoba = Osoba.objects.get(pk=pk)
        serializer = OsobaModelSerializer(osoba)
        return Response(serializer.data)

@api_view(['PUT', 'DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def osoba_update_delete(request, pk):

    try:
        osoba = Osoba.objects.get(pk=pk)
    except Osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
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

# class OsobaList(APIView):
#
#     def get(self, request, format=None):
#         osobas = Osoba.objects.all()
#         serializer = OsobaModelSerializer(osobas, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = OsobaModelSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class OsobaDetail(APIView):
#
#     def get_object(self, pk):
#         try:
#             return Osoba.objects.get(pk=pk)
#         except Osoba.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         osoba = self.get_object(pk)
#         serializer = OsobaModelSerializer(osoba)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         osoba = self.get_object(pk)
#         serializer = OsobaModelSerializer(osoba, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         osoba = self.get_object(pk)
#         osoba.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# class OsobaAdd(APIView):
#
#     def post(self, request, format=None):
#         serializer = OsobaModelSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class OsobaDetailName(APIView):
#
#     def get(self, request, imie, format=None):
#         osobas = Osoba.objects.all().filter(imie=imie)
#         serializer = OsobaModelSerializer(osobas, many=True)
#         return Response(serializer.data)

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")