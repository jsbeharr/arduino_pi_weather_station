from flask import Flask
from flask_restful import Api, Resource
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

app.config.from_pyfile('config.cfg')

mysql.init_app(app)

api = Api(app)

class All(Resource):
    def get(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("""
                    SELECT 
                        `date_time`,
                        `humidity`,
                        `wetness`,
                        `wind_speed`,
                        `temperature`,
                        `pressure` 
                    FROM 
                        `weather_data_test`""")

            data = cursor.fetchall()

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

class Recent(Resource):
    def get(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("""
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
                    DESC LIMIT 1""")

            data = cursor.fetchall()
            
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


api.add_resource(All, '/all')
api.add_resource(Recent, '/recent')

if __name__ == '__main__':
    app.run(debug=True)
