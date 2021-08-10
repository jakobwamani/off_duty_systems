from django.urls import path

from mvp import views

urlpatterns = [
    path('', views.index, name='index'),
]