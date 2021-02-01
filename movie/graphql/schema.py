import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError
from movie.models import ListType, Movies, MovieCategory, WatchedMovies, User


class ListTypeType(DjangoObjectType):
    class Meta:
        model = ListType


class  UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('username',)


class MovieCategoryType(DjangoObjectType):
    class Meta:
        model = MovieCategory
        fields = ('category',)


class MoviesType(DjangoObjectType):
    class Meta:
        model = Movies


class WatchedMoviesType(DjangoObjectType):
    class Meta:
        model = WatchedMovies


class Query(graphene.ObjectType):
    all_movies = graphene.List(MoviesType)
    specific_movie = graphene.Field(MoviesType, id=graphene.Int())
    watched_movies = graphene.List(WatchedMoviesType)
    recommended_movies = graphene.List(WatchedMoviesType, codename=graphene.String())

    def resolve_all_movies(self,root):
        return Movies.objects.all()

    def resolve_specific_movie(self,root,id):
        try:
            return Movies.objects.get(pk=id)

        except:
            raise GraphQLError("NO SUCH RECORD FOUND IN DATABASE..!")

    def resolve_watched_movies(self,root):
        return WatchedMovies.objects.all()

    def resolve_recommended_movies(self,root,codename):
        codename = codename.upper()
        print(codename)
        try:
            return WatchedMovies.objects.filter(code_name__code_name=codename)
        except:
            raise GraphQLError("NO SUCH CODENAME IS FOUND...!!")


class CreateListType(graphene.Mutation):
    class Arguments:
        code_name = graphene.String()
        user_id = graphene.Int()

    list_type = graphene.Field(ListTypeType)

    @staticmethod
    def mutate(info, root, code_name,user_id):
        code_name = code_name.upper()
        existing_list = ListType.objects.filter(code_name=code_name)
        data = User.objects.values("id")
        user_ids = []
        for d in data:
            user_ids.append(d["id"])
        if user_id in user_ids:
            if not existing_list:
                type, created = ListType.objects.get_or_create(code_name=code_name,user_id=user_id)
            else:
                raise GraphQLError("CODENAME IS ALREADY EXISTS..!")
            return CreateListType(list_type=type)
        else:
            raise GraphQLError("NO SUCH USER FOUND..!")


class CreateWatched(graphene.Mutation):
    class Arguments:
        type = graphene.String()
        movieID = graphene.Int()

    watched = graphene.Field(WatchedMoviesType)
    @staticmethod
    def mutate(root,info,type,movieID):
        type = type.upper()
        try:
            list_type = ListType.objects.get(code_name=type)
            watched_movie =  WatchedMovies.objects.create(movie_id=movieID, code_name=list_type)
            return CreateWatched(watched=watched_movie)
        except:
            raise GraphQLError("NO SUCH CODENAME EXISTS..!")


class Mutation(graphene.ObjectType):
    create_watched_list = CreateWatched.Field()
    create_list_type = CreateListType.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
