from django.urls import path
from . import views

urlpatterns = [
    path('', views.MultipleModelView.as_view(), name='index'),
]