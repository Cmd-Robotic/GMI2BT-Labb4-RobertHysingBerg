import requests
from time import sleep
#this script sends the post requests to the flask server that puts it in the database
#it works on 5 second intervals
counter = 0
while(counter < 1000000):
    JsonData = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London&appid=99dc469ab0a754185c74cedc83e4163b').json()
    print(JsonData)
    try:
        requests.post('http://127.0.0.1:5000/postData',json=JsonData)
        print('Transmit Success')
    except:
        print('Transmit Failure')
    counter += 1
    sleep(5)