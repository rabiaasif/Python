import random
from flask import Flask, request
from flask_json import FlaskJSON
from flask import jsonify
app = Flask(__name__)
FlaskJSON(app)

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



if __name__ == '__main__':  
    app.run()