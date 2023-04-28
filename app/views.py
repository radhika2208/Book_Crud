from django.shortcuts import render, redirect
from django.views import View
from rest_framework import viewsets
from rest_framework.response import Response
import requests
from rest_framework import status
from .models import Book
from .serializer import  CreateBookSerializer,UpdateBookSerializer
from .form import BookForm
from.constants import *
from .messages import *
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book

    def get_serializer_class(self):
        """
        Get the Serializer Class as CreateBookSerializer or UpdateBookSerializer as per required action
        """
        if self.action == ['list', 'create']:
            return CreateBookSerializer
        else:
            return UpdateBookSerializer

    def get_queryset(self, pk=None):
        """
        Get the queryset of Book Model
        """
        return Book.objects.filter().order_by('id')

    def list(self, request, *args, **kwargs):
        """
        list all the Books Data
        """
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        """
        Retrieves an instance of Book Model
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        """
        Create new Book instance with Books Data
        """

        serializer = CreateBookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        """
        Updates the instance with its new values
        """
        ins = self.get_object()
        serializer = self.get_serializer(ins, data=request.data)
        if serializer.is_valid():
            serializer.update(ins, serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'msg': MESSAGE_1}, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        """
        Partially updates the instance with its new values
        """
        ins = self.get_object()
        serializer = self.get_serializer(ins, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.update(ins, serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'msg': MESSAGE_2}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        """
        Delete an instance of Book
        """
        data = self.get_object()
        data.delete()
        return Response({'msg': MESSAGE_3})
