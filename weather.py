import requests
import datetime
import consolemenu
import settings


def get_json_weather():
    headers = {
        'Authorization': 'Token {}'.format(settings.api_key)
    }

    request = 'https://api.meteo.pl/api/v1/model/coamps/grid/2a/coordinates/130,111/field/' \
              'airtmp_zht_fcstfld/level/000002_000000/date/2018-05-15T00/forecast/'
    response = requests.post(request, headers=headers)

    return response.json()


def get_temp(time):
    date = get_json_weather()
    index = date['times'].index(time)
    return date['data'][index]


def kelwin_to_celsius(temp):
    return temp - 273.15


def always_two_digit(number):
    if number < 10:
        return '0' + str(number)
    else:
        return str(number)


def get_time(hour):
    now = datetime.datetime.now()
    return str(now.year) + '-' + always_two_digit(now.month) + '-' + always_two_digit(now.day) + 'T' + \
        always_two_digit(hour) + ':00:00Z'


def weather_main():
    print('Today weather in Poland(near Białowieża) from meteo.pl\n\n')
    hour = 5

    for x in range(0, 10):
        temp = kelwin_to_celsius(get_temp(get_time(hour)))
        print('Temperature: %8.1f Celsius \ttime: %d:00' % (temp, hour))
        hour += 3
        if hour >= 24:
            break

    print('\n\n *must be near Białowieża because this location is free')
    print('  Other location cost very much -> 1gr for one request :(')

    consolemenu.Screen().input('Press [Enter] to continue')
