from django.urls import path
from . import views

urlpatterns = [
     path('', views.MultipleModelView.as_view(), name='index'),
     path('booklist/', views.BookListView.as_view(), name='book_list'),
     #path('python/', views.sort_by, name='python_books'), 
     path('category/<int:pk>', views.CategoryView.as_view(), name='python_books'), 
]

