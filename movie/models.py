from django.db import models
from django.contrib.auth.models import User


class MovieCategory(models.Model):
    category = models.CharField(max_length=20, unique=True )

    def __str__(self):
        return self.category


class Movies(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    overview = models.TextField(null=True)
    rated = models.CharField(max_length=20)
    release_date = models.DateField(null=True, blank=True)
    language = models.CharField(max_length=10)
    popularity = models.DecimalField(max_digits=10, decimal_places=6, null=True)
    vote_count = models.IntegerField()
    vote_average = models.DecimalField(max_digits=10, decimal_places=6, null=True)
    category = models.ForeignKey(MovieCategory, on_delete=models.CASCADE)
    region = models.CharField(max_length=10)

    def __str__(self):
        return self.title


class ListType(models.Model):
    code_name = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.code_name


class WatchedMovies(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE, default=None)
    code_name = models.ForeignKey(ListType, on_delete=models.CASCADE, default=None)

    class Meta:
        unique_together = ("movie", "code_name")
