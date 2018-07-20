from flask import Flask, request
from flask_restful import Api, Resource
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

# Configures app from a config.cfg
app.config.from_pyfile('config.cfg')

mysql.init_app(app)
api = Api(app)

# Base Class for Api Requests
class Weather_Request(Resource):
    def get(self, query):
        try:
            # connects to database and peforms query 
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(query)

            # stores data from sql query
            data = cursor.fetchall()

            # Creates and returns a json object to
            # print to the webpage
            weather_forecasts = []
            for item in data:
                i = {
                    'date_time': str(item[0]),
                    'humidity': str(item[1]),
                    'wetness': str(item[2]),
                    'wind_speed': str(item[3]),
                    'temperature': str(item[4]),
                    'pressure': str(item[5])
                    }
                weather_forecasts.append(i)
            return {'StatusCode':'200', 'Weather': weather_forecasts}
        except Exception as e:
            return {'error' : str(e) }


# Can get and query weather
class Weather(Weather_Request):
    def get(self):
        # url arguments do "/weather?<arg1>=<val1>&<arg2>=<val2>&..."
        # or just do "/weather" to get all data
        date_begin = request.args.get('begin', default='2018-06-27', type=str)
        date_end = request.args.get('end', default='2018-07-10', type=str)

        query = """
            SELECT 
                `date_time`,
                `humidity`,
                `wetness`,
                `wind_speed`,
                `temperature`,
                `pressure` 
            FROM 
                `weather_data_test`
            WHERE
                `date_time` BETWEEN
                    \'{begin}\'
                    and
                    \'{end}\'
                """.format(begin=date_begin, end=date_end)
        return super().get(query)


# Gets the most recent forecast entry
class Recent(Weather_Request):
    def get(self):
        query = """
            SELECT 
                `date_time`,
                `humidity`,
                `wetness`,
                `wind_speed`,
                `temperature`,
                `pressure` 
            FROM 
                `weather_data_test` 
            ORDER BY 
                `date_time` 
            DESC LIMIT 1""" 
        return super().get(query)


# Creates routes
api.add_resource(Weather, '/weather')
api.add_resource(Recent, '/weather/recent')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
