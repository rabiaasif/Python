from flask import Flask, request
from flask_json import FlaskJSON, JsonError, json_response, as_json
app = Flask(__name__)
FlaskJSON(app)

#user-movie data table
USER_MOVIE = {"user1":["harry potter", "titanic"]}
MOVIE_GENRE = {"harry potter":["fiction","thriller"], "titanic":["romance"]}
MOVIE_ACTOR = {"emma watson": ["harry potter"]}

def add_to_database(movie_title, movie_genres, actors, user):
    #check types
    if (type(movie_title) == str) and (type(user)==str) and (type(movie_genres)==list) and (type(actors)==list):
        #new entries 
        if user not in USER_MOVIE:
            USER_MOVIE[user]= [movie_title]
        #existing users
        else:
            temp = USER_MOVIE[user]
            #check if movie already in database
            if movie_title in temp:
                print "Movie already in database!"
            
            #if not we can add it to the database
            else:
                temp.append(movie_title)
                USER_MOVIE[user] = temp
            
        if movie_title not in MOVIE_GENRE:
            MOVIE_GENRE[movie_title] = movie_genres
        else:
            temp = MOVIE_GENRE[movie_title]
            
            if movie_title in temp:
                print "Movie already in database!"
            else:
                temp.append(movie_title)
                MOVIE_GENRE[movie_title] = temp
        for actor in actors:
            if actor not in MOVIE_ACTOR:
                MOVIE_ACTOR[actor] = [movie_title]
            else:
                temp = MOVIE_ACTOR[movie_title]
                temp.append(movie_title)
                MOVIE_ACTOR[user] = temp                
                
            
       # print MOVIE_GENRE
        #print USER_MOVIE
        #print MOVIE_ACTOR
                
            
            
                
            
        return "Sucessfully entered into database!"
    else:
        return "Please enter proper input!"
    
        

def search_movie():
    pass

if __name__ == '__main__':
    pass
   # app.run()