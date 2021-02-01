from django.urls import path
from graphene_django.views import GraphQLView
from movie.graphql.schema import schema
from movie import views


urlpatterns = [
    path('populate_movies/<category>/', views.populate_data_view),
    path('',  GraphQLView.as_view(graphiql=True, schema=schema))
]
