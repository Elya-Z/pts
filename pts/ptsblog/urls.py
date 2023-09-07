from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # post views
    path('', views.index, name='index'),
]
