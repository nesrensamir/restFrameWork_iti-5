from django.contrib import admin
from .models import Movie, Categories, Actor
# Register your models here.

admin.site.register(Movie)
admin.site.register(Categories)
admin.site.register(Actor)
