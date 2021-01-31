from django.contrib import admin
from .models import ListType, MovieCategory, Movies, WatchedMovies


@admin.register(ListType)
class ListTypeAdmin(admin.ModelAdmin):
    list_display = ['code_name', 'user']


@admin.register(MovieCategory)
class MovieCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category']


@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'title', 'overview', 'rated',
        'release_date', 'language', 'popularity',
        'vote_count', 'vote_average', 'category', 'region'
    ]


@admin.register(WatchedMovies)
class WatchedMoviesAdmin(admin.ModelAdmin):
    list_display = ['movie', 'code_name']
