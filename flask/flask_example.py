import random
from flask import Flask, request
from flask_json import FlaskJSON
from flask import jsonify
from flaskext.mysql import MySQL
app = Flask(__name__)
FlaskJSON(app)

#intialize database using mysql before entering in database
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password1'
app.config['MYSQL_DATABASE_DB'] = 'test'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor() 

   


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down...'


@app.route('/encrp/<length>')
def encrypt(word,key):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for i in word:
        result += alpha[word.find(i) + key]
    return result
        

@app.route('/password/<length>')
def password_generator(length):
    alpha_num = [1,2,3,4,5,6,7,8,9,0,'q','w','e','r','t','y','u','i','o','i','o',\
             'p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n',\
             'm']
    password = ''
    i = 0
    while i < int(int(length)):
        temp = random.choice(alpha_num)
        if random.random() > 0.75 and type(temp) == str:
            temp = temp.upper()      
        password += str(temp)
        i+=1
    return (password)

@app.route('/string')
def return_string():
    return "this is a string"

@app.route('/dict')
def some_dictionary():
    a = {1:2, 2:3, 3:4, 4:5}
    return jsonify(a)

@app.route('/db')
def enter_db():
    cursor.execute(
            """INSERT INTO 
                generation_marble (material, nickname,generation,size,size_name, pattern, origin, grade, colours_string,image_path,is_purchased, is_handmade, games_played, user_id)
            VALUES (%s)""", ("any name here"))
    conn.commit() 



if __name__ == '__main__':  
    app.run()