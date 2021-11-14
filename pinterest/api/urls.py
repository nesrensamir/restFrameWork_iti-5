from django.urls import path
from .views import movie_list, movie_create, movie_details, movie_delete, movie_update
urlpatterns = [
     path('movie/', movie_list, name='movie-index'),
     path('movie/create', movie_create, name='movie-create'),
     path('movie/<int:pk>', movie_details, name ='movie-details'),
     path('movie/delete/<int:pk>', movie_delete, name='movie-delete'),
     path('movie/update/<int:pk>', movie_update, name='movie-update'),


]