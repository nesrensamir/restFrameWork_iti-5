from django.db import models


# Create your models here.


class CommonInfo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    categories = models.ManyToManyField('Categories')
    casts = models.ManyToManyField('Actor')
    poster_image = models.ImageField(upload_to='pinterest_posters')

    class Meta:
        abstract = True


class Movie(CommonInfo):
    def __str__(self):
        return self.title


class Series(CommonInfo):
    season = models.CharField(max_length=50)
    episode = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Categories(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to='movie/actor/images')

    def __str__(self):
        return self.first_name
