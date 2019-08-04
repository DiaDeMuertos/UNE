from time import sleep
from datetime import datetime
import requests


def is_not_max(x):
    return x != 8640


if __name__ == "__main__":
    print('LOOP')

    url = 'http://bussonora.in/api/v1/ubicaciones/1703?format=json'
    counter = 0

    while is_not_max(counter):

        try:
            r = requests.get(url)
            buses = r.json()['ubicaciones']
            date_time = datetime.now().strftime('%H:%M:%S')

            for bus in buses:
                values = (bus['vehiculo_id'], bus['direccion'],
                          bus['velocidad'], bus['fecha'], date_time)

                if bus['vehiculo_id'] == str(302):
                    print('%s %s %s %s %s' % values)
        except:
            print('Something went wrong')
            print(sys.exc_info())
        finally:
            counter += 1
            sleep(10)
