from django.urls import path
from .views import main, article, search, about, contact


urlpatterns = [
    path('', main, name='blog'),
    path(r'article/<str:URLTitle>', article, name='article'),
    path(r'search/', search, name='search_field'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),


]
