from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
     path('', views.MultipleModelView.as_view(), name='index'),
     path('category/<int:pk>', views.CategoryView.as_view(), name='category'), 
     path('favorite/<int:book_pk>', views.add_to_favorite, name='favorite_added'), 
     path('favorites/', views.FavoriteView.as_view(), name='favorites'), 
     url(r'^register/', views.register, name='register')
]

