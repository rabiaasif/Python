import requests 
import json
import turtle


def space_info():
    r = requests.get('http://api.open-notify.org/astros.json')
    space_info = json.loads(r.text)
    print ("number of people in space: " + str(space_info['number']))
    for i in space_info['people']:
        print (i['name'] + ' is in ' + i['craft'])
        
    url = 'http://api.open-notify.org/iss-now.json'
    r = requests.get(url)
    position = json.loads(r.text)['iss_position']
    lat = position['latitude']
    lon = position['longitude']
    print ('Latitude: ' + lat  + " , " + 'Longitude' + lon)
    
    screen = turtle.Screen()
    screen.setup(720,360)
    screen.setworldcoordinates(-180,-90,180,90)
    screen.bgpic('map.jpg')
    
    screen.register_shape('iss.png')
    iss = turtle.Turtle()
    iss.shape('iss.png')
    iss.setheading(90)
    
    iss.penup()
    iss.goto(lon,lat)
    
    

if __name__ == '__main__':  
    space_info()