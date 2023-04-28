"""
url configurations for app 'api'
created a default router object and register the viewset class with it
Through this API URLs are determined automatically by the router
The '' url request takes to add_books function in views to fill details
The 'show' url requests show_books function to display data
The 'retrieve' url requests retrieve_books function to retrieve the data
The 'update' url requests delete_books function to update the data
The 'delete' url requests delete_books function to delete the data
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('Book', views.BookViewSet, basename='Books')

urlpatterns = [
    path('root/', include(router.urls)),
    ]