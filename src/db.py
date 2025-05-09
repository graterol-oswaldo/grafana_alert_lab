from influxdb import InfluxDBClient
from datetime import datetime
import utils

env_vars = utils.tools.load_env('.env')

db_host = env_vars['DB_HOST']
db_port = env_vars['DB_PORT']
db_username = env_vars['DB_USERNAME']
db_password = env_vars['DB_PASSWORD']
db_database = env_vars['DB_DATABASE']

client = InfluxDBClient(db_host,db_port,db_username,db_password,db_database)

client.create_database(db_database)

def insert_data(value:float) -> None:
    point = []
    point.append({
        "measurement": "temperature",
        "time": datetime.now().isoformat(),
        "tags": {
            "sensor_type": "thermometer",
        },
        "fields": {
            "value": value
        }
    })

    client.write_points(point)

