from rest_framework import serializers
from .models import Book
from .messages import *
import re
class CreateBookSerializer(serializers.ModelSerializer):
    """
    Serializer class for Creating Book
    """
    name_of_book = serializers.CharField(max_length=20, required=True,allow_blank=False,trim_whitespace=True,
                                        error_messages=BOOK_VALIDATION_ERROR['name_of_book'])
    book_price = serializers.CharField(max_length=100, required=True,allow_blank=False,
                                        error_messages=BOOK_VALIDATION_ERROR['book_price'])
    authors_name = serializers.CharField(max_length=20, required=True,allow_blank=False,trim_whitespace=True,
                                        error_messages=BOOK_VALIDATION_ERROR['authors_name'])
    author_phone = serializers.CharField(max_length=20, required=True,allow_blank=False,
                                        error_messages=BOOK_VALIDATION_ERROR['author_phone'])

    def validate_book_price(self,value):
        """
        validates the book_price as it contains only digits
        """
        if not all(char.isdigit() for char in value):
            raise serializers.ValidationError(BOOK_VALIDATION_ERROR['book_price']['invalid'])
        return value

    def validate_author_phone(self,value):
        """
        validates author_phone
        """
        pattern = r'^\+?1?\d{10,15}$'
        if not re.match(pattern, value):
            raise serializers.ValidationError(BOOK_VALIDATION_ERROR['author_phone']['invalid'])
        return value


    def create(self, validated_data):
        """
        creating an instance of Book
        :param validated_data: data to be inserted
        :return: data instance
        """
        user = Book.objects.create(
            name_of_book=validated_data['name_of_book'],
            book_price=validated_data['book_price'],
            authors_name=validated_data['authors_name'],
            author_phone=validated_data['author_phone'],
        )
        return user

    class Meta:
        """
        class Meta for CreateBookSerializer
        """
        model = Book

        fields = ['id', 'name_of_book', 'book_price', 'authors_name', 'author_phone']


class UpdateBookSerializer(serializers.ModelSerializer):
    """
    Serializer class for Updating Book
    """
    name_of_book = serializers.CharField(max_length=20, required=True,allow_blank=False,trim_whitespace=True,
                                        error_messages=BOOK_VALIDATION_ERROR['name_of_book'])
    book_price = serializers.CharField(max_length=100, required=True ,allow_blank=False,
                                        error_messages=BOOK_VALIDATION_ERROR['book_price'])
    authors_name = serializers.CharField(max_length=20, required=True ,allow_blank=False,trim_whitespace=True,
                                        error_messages=BOOK_VALIDATION_ERROR['authors_name'])
    author_phone = serializers.CharField(max_length=20, required=True ,allow_blank=False,
                                        error_messages=BOOK_VALIDATION_ERROR['author_phone'])

    def validate_book_price(self,value):
        """
        validates the book_price as it contains only digits
        """
        if not all(char.isdigit() for char in value):
            raise serializers.ValidationError(BOOK_VALIDATION_ERROR['book_price']['invalid'])
        return value

    def validate_author_phone(self,value):
        """
        validates author_phone
        """
        pattern = r'^\+?1?\d{9,15}$'
        if not re.match(pattern, value):
            raise serializers.ValidationError(BOOK_VALIDATION_ERROR['author_phone']['invalid'])
        return value

    def update(self, instance, validated_data):
        """
        updating an instance of Book
        :param instance:old Book data
        :param validated_data:new Book data
        :return: updated data instance of Book
        """
        ins = Book.objects.filter(id=instance.id).update(
            name_of_book=validated_data.get('name_of_book'),
            book_price=validated_data.get('book_price'),
            authors_name=validated_data.get('authors_name'),
            author_phone=validated_data.get('author_phone'))
        return ins

    class Meta:
        """
        class Meta for UpdateBookSerializer
        """
        model = Book

        fields = ['id', 'name_of_book', 'book_price', 'authors_name', 'author_phone']