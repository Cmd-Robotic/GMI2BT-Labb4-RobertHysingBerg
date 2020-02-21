import flask
import sqlite3
Server = flask.Flask(__name__)
#this script provides the general server services
@Server.route('/')
def home():
    datconn = sqlite3.connect('database.db')
    datcurs = datconn.cursor()
    datcurs.execute("SELECT * FROM Weather")
    Data = datcurs.fetchall()
    datconn.close()
    return flask.render_template('home.html', WeatherData=Data)

@Server.route('/postData', methods=['POST'])
def getData():
    try:
        SaveData(flask.request.json)
        return flask.Response()
    except:
        print('Save Failure')
        return flask.Response()

def SaveData(Data):
    datconn = sqlite3.connect('database.db')
    Values = (Data['name'], Data['coord']['lat'], Data['coord']['lon'], Data['main']['temp'], Data['main']['humidity'], Data['main']['pressure'])
    datconn.execute("INSERT INTO Weather VALUES (?,?,?,?,?,?)", Values)
    datconn.commit()
    datconn.close()
    return True

if __name__ == "__main__":
    Server.run(debug=True)