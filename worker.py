import requests
import psycopg2
import psycopg2.extras
from datetime import datetime
import logging
from keys import api_key
from keys import db_password

def get_data():
    #url = 'http://api.wunderground.com/api/' + api_key + '/conditions/q/CA/San_Francisco.json'
    url = url = 'http://api.wunderground.com/api/' + api_key + '/conditions/q/UK/london.json'
    r = requests.get(url).json()
    #print(r)
    data = r['current_observation']
    location = data['observation_location']['full']
    weather = data['weather']
    wind_str = data['wind_string']
    #temperature = data['temp_f']
    a = data['temp_f']
    temperature = int((a-32)*5/9)
    humidity = data['relative_humidity']
    precip = data['precip_today_string']
    icon_url = data['icon_url']
    observation_time = data['observation_time']
    print(temperature)


#open a database connection
    try:
        conn = psycopg2.connect(dbname='weatherapp', user='postgres', host='localhost', password='srinath33')
        print('opened database successfully')

    except:
        print(datetime.now(), 'unable to connect to database')
        logging.exception('unable to open the database')
        return

    else:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

#write data to database
    cur.execute(
        """INSERT INTO station_reading(location,weather,wind_str,temperature,humidity,precip,icon_url,observation_time) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""",
        (location, weather, wind_str, temperature, humidity, precip, icon_url, observation_time))
    conn.commit()
    cur.close()
    conn.close()
    print('data written', datetime.now())

get_data()











