### MovieGraphQL API Project
##### Follow below steps to run your localserver.
Step-1
```sh
git clone https://github.com/GauravGirase/MovieGraphQL.git
```
Step-2
Create virtual env and install requirements.txt file
```sh
virtualenv venv
venv\Scripts\activate
pip install -r requirements.txt
```
Step-3
You need to update DB configuration in settings file
```sh
'NAME': 'DB_name',
'USER': 'DB_user',
'PASSWORD': 'DB_password',
```

Step-4
run migrate
```sh
python manage.py migrate
```
Step-5
Runserver
```sh
python manage.py runserver
```
Done

### Now You can use Graphql api, before that we need to follow below steps to dump movie db
Step-1
Hit Below urls in browser to populate movie db from [MovieDB API](https://developers.themoviedb.org/3/getting-started/introduction).
```sh
http://127.0.0.1:8000/popular/
http://127.0.0.1:8000/upcoming/
http://127.0.0.1:8000/latest/
```
Step-2
Access GraphQL
```shell
http://127.0.0.1:8000/graphql/
```
Step-3
Sample query show list of all movies present in the database.
```sh
query ShowAll{
  
   allMovies{
      Id
      title
      overview
      releaseDate
      rated
      region
      voteCount
      voteAverage
      popularity
      category{
         category
      
   }    
}
   
}
```
Step-4
Sample query to show detailed data of a particular movie given id as the argument.
```sh
query ShowSpecific{
   specificMovie(id:476928){
      Id
      title
      overview
      releaseDate
      region
      rated
      popularity
      voteCount
      voteAverage
      category{
         category
      }
   }
}
```

Step-5
Now You need to create one super user to create new list with unique codename.
```sh
python manage.py createsuperuser
```
Step-6
Now you can create list with unique code name for above created user.
```sh
mutation createlist{
   createListType(codeName:"Action",userId:2){
      listType
      {
         codeName 
      }
   } 
}

```
Step-7
Sample query to push movies(Wathedlist) in previously created list.
```sh
mutation CreateWatched{
   createWatchedList(movieID:506281,type:"action")
   {
      watched{
         movie {
            releaseDate
            title
         }
         codeName{
            codeName
         }
      }   
   }
}
```

Step-8
General query to see movie recommendation based on watched list by providing codename.
```sh
query recommended{
   recommendedMovies(codename:"action"){
     movie{
      Id
      title
      overview
      rated
      region
      releaseDate
      category{
         category
      }
   }
   }
   
}


```









