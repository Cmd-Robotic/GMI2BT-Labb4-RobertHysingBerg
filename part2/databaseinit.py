import sqlite3
#this script initialises the table used by the other two scripts, ONLY works if the database.db file exists and there is no Weather table already
datconn = sqlite3.connect('database.db')
datconn.execute('''CREATE TABLE Weather (City text, Latitude real, Longitude real, TemperatureKelvin real, Humidity real, AirPressure real)''')
datconn.commit()
datconn.close()