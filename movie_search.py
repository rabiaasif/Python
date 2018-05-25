from flask import Flask, request
from flask_json import FlaskJSON, JsonError, json_response, as_json
app = Flask(__name__)
FlaskJSON(app)

#user-movie data table
USER_MOVIE = {"user1":["harry potter", "titanic"]}
MOVIE_GENRE = {"harry potter":["fiction","thriller"], "titanic":["romance"]}
MOVIE_ACTOR = {"emma watson": ["harry potter"]}

def add_user(user):
    '''
    add user only, without adding movie - done, works well, tested in shell
    '''
    if (type(user)==str):
        if user not in USER_MOVIE:
            USER_MOVIE[user] = []
    else:
        return "Improper input"
        
def add_movie(movie_title, movie_genre, actors):
    '''
    add movie description- done, works well, tested in shell
    '''
    if (type(movie_title) == str) and (type(movie_genre) == list) and (type(actors) == list) :
        if movie_title not in MOVIE_GENRE:
            MOVIE_GENRE[movie_title] = movie_genre
        else:
            temp = MOVIE_GENRE[movie_title]
            for genre in movie_genre:
                if genre not in temp:
                    temp.append(genre)
                    
            MOVIE_GENRE[movie_title] = temp
             
        for actor in actors:
            if actor not in MOVIE_ACTOR:
                MOVIE_ACTOR[actor] = [movie_title]
            else:
                temp = MOVIE_ACTOR[actor]
                if movie_title not in temp:
                    temp.append(movie_title)
                    MOVIE_ACTOR[actor] = temp         
    
        
    else:
        return "improper input"
        
        
    

def add_to_database(movie_title, movie_genres, actors, user):
    '''
    add movie, user, genre, and actor, done, tested, works
    '''
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
                if movie_title not in temp:
                    temp.append(movie_title)
                    USER_MOVIE[user] = temp
            
        if movie_title not in MOVIE_GENRE:
            MOVIE_GENRE[movie_title] = movie_genres
        else:
            temp = MOVIE_GENRE[movie_title]
            
            if movie_title in temp:
                print "Movie already in database!"
            else:
                temp = MOVIE_GENRE[movie_title]
                for genre in movie_genres:
                    if genre not in temp:
                        temp.append(genre)
                    
            MOVIE_GENRE[movie_title] = temp
        for actor in actors:
            if actor not in MOVIE_ACTOR:
                MOVIE_ACTOR[actor] = [movie_title]
            else:
                temp = MOVIE_ACTOR[actor]
                if movie_title not in temp:
                    temp.append(movie_title)
                    MOVIE_ACTOR[actor] = temp                
                
            
       # print MOVIE_GENRE
        #print USER_MOVIE
        #print MOVIE_ACTOR
            
        return "Sucessfully entered into database!"
    else:
        return "Please enter proper input!"
    
        

@app.route('/<inpt>')
@as_json 
def search(inpt):
    if inpt in MOVIE_ACTOR:
        return MOVIE_ACTOR[inpt]
    elif inpt in USER_MOVIE:
        return USER_MOVIE[inpt]
    elif inpt in MOVIE_GENRE:
        return  MOVIE_GENRE[inpt]
    else:
        return "hi"
    
@app.route('/<genre>')
@as_json    
def search_genre(genre):
    movie_list = []
    for movie in MOVIE_GENRE.keys():
        if genre in MOVIE_GENRE[movie]:
            if movie not in movie_list:
                movie_list.append(movie)
    return movie_list 
   

if __name__ == '__main__':
    pass
    #app.run()