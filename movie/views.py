import random
import requests
from django.conf import settings
from django.http import HttpResponse
from .models import MovieCategory,Movies


def populate_data(json_data, region, category):
    id = json_data.get("id")
    title = json_data.get("original_title")
    overview = json_data.get("overview") or None
    rated = json_data.get("adult")
    release_date = json_data.get("release_date") or None
    language = json_data.get("original_language")
    popularity = json_data.get("popularity")
    vote = json_data.get("vote_count")
    vote_avg = json_data.get("vote_average")
    category, created = MovieCategory.objects.get_or_create(category=category.upper())
    Movies.objects.get_or_create(
        id=id, title=title, overview=overview,
        release_date=release_date, rated=rated,
        language=language, popularity=popularity,
        vote_count=vote, vote_average=vote_avg,
        category=category, region=region
    )


def populate_data_view(request, category):
    base_url = f"https://api.themoviedb.org/3/movie/{category}?api_key={settings.API_KEY}&language=en-US"
    for page in range(1,5):
        region = settings.REGION
        url = base_url + f"&page={page}&region={region}"
        request_object = requests.get(url=url)
        json_data = request_object.json()
        if category == "latest":
            populate_data(json_data, region, category )
        else:
            movies_data = json_data["results"]
            for data in movies_data:
                populate_data(data, region, category)

    return HttpResponse(f"{category.upper()} MOVIES DATA DUMPED SUCCESSFULLY..!!")
