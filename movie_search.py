from flask import Flask, request
from flask_json import FlaskJSON, JsonError, json_response, as_json
app = Flask(__name__)
FlaskJSON(app)

#user-movie data table
USER_MOVIE = {"user1":["harry potter", "titanic"], "user2": ["harry potter 2", "bee movie"]}
MOVIE_GENRE = {"harry potter":["fiction","thriller"], "titanic":["romance"]}
MOVIE_ACTOR = {"emma watson": ["harry potter"]}

@app.route('/user_movie')
@as_json
def view_movie():
    result = ''
    for user in USER_MOVIE.keys():
        if user != 'favicon.ico':
            result += "- "+user + ":" + " "
            for movie in USER_MOVIE[user][:-1]:
                result += movie + ", "
            if USER_MOVIE[user] != []:
                result += USER_MOVIE[user][-1] + " "
    return result[1:]

@app.route('/movie_genre')
@as_json
def view_genre():
    result = ''
    for user in MOVIE_GENRE.keys():
        if user != 'favicon.ico':
            result += "- "+user + ":" + " "
            for movie in MOVIE_GENRE[user][:-1]:
                result += movie + ", "
            result += MOVIE_GENRE[user][-1] + " "
    return result[1:]

@app.route('/movie_actor')
@as_json
def view_actor():
    
    result = ''
    for user in MOVIE_ACTOR.keys():
        if user != 'favicon.ico':
            result += "- "+user + ":" + " "
            for movie in MOVIE_ACTOR[user][:-1]:
                result += movie + ", "
            result += MOVIE_ACTOR[user][-1] + " "
    return result[1:]   

@app.route('/<user>')
@as_json
def add_user(user):
    '''
    add user only, without adding movie - done, works well, tested in shell
    '''


    if user not in USER_MOVIE:
        USER_MOVIE[user] = []
        return user + " has been added to the database!"
    else:
        return user + " is already in the database!"
 
 

@app.route('/movie/<movie_title>/<movie_genre>/<actors>')
@as_json       
def add_movie(movie_title, movie_genre, actors):
    '''
    add movie description- done, works well, tested in shell
    '''
    movie_genre = parser(movie_genre)
    actors = parser(actors)    
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
                
    return "added to database"
        
    

@app.route('/add/<user>/<movie_genres>/<actors>/<movie_title>')
@as_json
def add_to_database(movie_title, movie_genres, actors, user):
    '''
    add movie, user, genre, and actor, done, tested, works
    '''
    movie_genres = parser(movie_genres)
    actors = parser(actors)
   
  
    
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
 
    
        

@app.route('/search/<inpt>')
@as_json 
def search(inpt):
    result = ''
    
    inpt = str(inpt)
    if inpt in MOVIE_ACTOR:
        for i in MOVIE_ACTOR[inpt]:
            result += i
            result += "-" 
      
                             
        
    if inpt in USER_MOVIE:
        for i in USER_MOVIE[inpt]:
            result += i
            result += "-"
          
       
    if inpt in MOVIE_GENRE:
        for i in MOVIE_GENRE[inpt]:
            
            result +=  i
            result += "-"
            
            
    if search_genre(inpt) != "No results":
    
        result +=  search_genre(inpt)
        result += "-"
        
    
       
    if result == "":
        return "No results"
    else:
        return result 
        
    
   
def search_genre(genre):
    movie_list = []
    for movie in MOVIE_GENRE.keys():
        if genre in MOVIE_GENRE[movie]:
            if movie not in movie_list:
                movie_list.append(movie)
    if movie_list == []:
        return "No results"
    else:
        result = ""
        for movie in movie_list:
            result += movie 
            result += "-"
            
        
          
    return result 
    
def parser(dash_string):
    return dash_string.split("-")
   

if __name__ == '__main__':
      
    app.run()