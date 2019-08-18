from time import sleep
from datetime import datetime
import sys
import requests
from pymongo import MongoClient

MAX_COUNTER = 1


def is_not_max(value):
    return value < MAX_COUNTER


if __name__ == "__main__":
    print('LOOP')

    forever = True
    counter = 0
    routes = [
        'http://bussonora.in/api/v1/ubicaciones/101?format=json',
        'http://bussonora.in/api/v1/ubicaciones/102?format=json',
        'http://bussonora.in/api/v1/ubicaciones/201?format=json',
        'http://bussonora.in/api/v1/ubicaciones/202?format=json',
        'http://bussonora.in/api/v1/ubicaciones/301?format=json',
        'http://bussonora.in/api/v1/ubicaciones/301?format=json',
        'http://bussonora.in/api/v1/ubicaciones/302?format=json',
        'http://bussonora.in/api/v1/ubicaciones/401?format=json',
        'http://bussonora.in/api/v1/ubicaciones/402?format=json',
        'http://bussonora.in/api/v1/ubicaciones/501?format=json',
        'http://bussonora.in/api/v1/ubicaciones/601?format=json',
        'http://bussonora.in/api/v1/ubicaciones/700?format=json',
        'http://bussonora.in/api/v1/ubicaciones/701?format=json',
        'http://bussonora.in/api/v1/ubicaciones/801?format=json',
        'http://bussonora.in/api/v1/ubicaciones/901?format=json',
        'http://bussonora.in/api/v1/ubicaciones/902?format=json',
        'http://bussonora.in/api/v1/ubicaciones/1001?format=json',
        'http://bussonora.in/api/v1/ubicaciones/1002?format=json',
        'http://bussonora.in/api/v1/ubicaciones/1101?format=json',
        'http://bussonora.in/api/v1/ubicaciones/1201?format=json',
        'http://bussonora.in/api/v1/ubicaciones/1301?format=json',
        'http://bussonora.in/api/v1/ubicaciones/1400?format=json',
        'http://bussonora.in/api/v1/ubicaciones/1501?format=json',
        'http://bussonora.in/api/v1/ubicaciones/1502?format=json',
        'http://bussonora.in/api/v1/ubicaciones/1601?format=json',
        'http://bussonora.in/api/v1/ubicaciones/1602?format=json',
        'http://bussonora.in/api/v1/ubicaciones/1701?format=json',
        'http://bussonora.in/api/v1/ubicaciones/1702?format=json',
        'http://bussonora.in/api/v1/ubicaciones/1703?format=json',
        'http://bussonora.in/api/v1/ubicaciones/1801?format=json',
        'http://bussonora.in/api/v1/ubicaciones/1802?format=json',
        'http://bussonora.in/api/v1/ubicaciones/1901?format=json',
        'http://bussonora.in/api/v1/ubicaciones/1902?format=json',
    ]

    while is_not_max(counter) or forever is not False:
        for route in routes:
            file_error = open('error.txt', 'a+')
            client = MongoClient('mongodb://admin:123@localhost:27017')
            db = client["une"]
            buses_collection = db["buses"]
            db.command("serverStatus")

            try:

                r = requests.get(route)
                buses = r.json()['ubicaciones']
                date_time = datetime.now().strftime('%H:%M:%S')

                for bus in buses:
                    vehiculo_id = bus['vehiculo_id']
                    fecha = bus['fecha']
                    pattern = {'vehiculo_id': vehiculo_id, 'fecha': fecha}

                    r = buses_collection.find_one(pattern)
                    if r is None:
                        buses_collection.insert_one(bus)

                print(route, len(buses), date_time)
            except:
                error_info = str(sys.exc_info())
                date_time = datetime.now().strftime('%Y-%m-%D %H:%M:%S')

                print('Something went wrong')
                print(error_info)

                file_error.write('%s %s\n' % (date_time, error_info))
            finally:
                file_error.close()
                client.close()
        counter += 1
        print('PAUSE 10 SECONDS')
        sleep(10)
