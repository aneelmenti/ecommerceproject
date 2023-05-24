from django.urls import path
from . import views
app_name = 'productapp'
urlpatterns = [
    path('search', views.search, name='search'),
    ]
