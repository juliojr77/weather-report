import requests
import json
import pprint
import time
from datetime import datetime
import os
import sys
# import location
# import webbrowser
# import BaseHTTPServer

#  for x in city.headers:
# ...     print(x+' :'+city.headers[x])



def print_there(x, y, text):
     sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
     sys.stdout.flush()




#------------------------
def catch_invalid_input(user_input_1, user_input_2):

    if user_input_1 != 0:
        if not user_input_1.isdigit() or int(user_input_1) > 4:
            input("Invalid input. Press enter to continue!... " )
            return True
        else:
            return False

    if user_input_2.isdigit():
        return user_input_2
    else:
        print('\n')
        input('Invalid entry..!!')
        return False

#--------------------



def get_zip_code():
    return input('Enter city Zip code:')


def get_ulr_current_solar(city_z_code):

    return 'http://api.wunderground.com/api/87867c89f62fc574/conditions/astronomy/q/%s.json' % city_z_code


def collect_data(url_condition):

    c = requests.get(url_condition)
    if c.status_code ==
    current = c.json()['current_observation']
    current2 = c.json()['sun_phase']

    current.update(current2)

    # Turn sun rise and set times into datetimes.
    rise = '%s:%s' % (current['sunrise']['hour'], current['sunrise']['minute'])

    set_ = '%s:%s' % (current['sunset']['hour'], current['sunset']['minute'])


    sunrise = datetime.strptime(rise, '%H:%M')
    sunset = datetime.strptime(set_, '%H:%M')



    wudata = {'local_time' : current['local_time_rfc822'],
                'city' : current['display_location']['city'],
                'state' : current['display_location']['state_name'],
                'zip': current['display_location']['zip'],
                'country' : current['display_location']['country'],
                'current_' : current['weather'],
                'temperature' : current['temperature_string'],
                'heat_index_string' : current['heat_index_string'],
                'feelslike_string' : current['feelslike_string'],
                'sunrise': sunrise,
                'sunset': sunset,
                'relative_humidity': current['relative_humidity'],
                'wind_degrees': str(current['wind_degrees']),
                'wind_string': current['wind_string']}
    return wudata



def get_menu_choices(choice):

    if catch_invalid_input(choice, 0):
        return 0

    elif int(choice) == 1:


        data = collect_data(get_ulr_current_solar(get_zip_code()))


        print_there(6,47,'-----------------------------------------------------------')
        print_there(7,49,'LOCAL TIME:')
        print_there(8,49, data['local_time'])
        print_there(9,49,'CITY:')
        print_there(10,49, data['city']+', '+ data['state']+', '+ data['zip'])
        print_there(11,47,'----------------------------------------------------------')
        print_there(12,62, 'CURRENT CONDITIONS: '+  data['current_'])
        print_there(13,63, '- Temperature...:'+  data['temperature'])
        print_there(14,63, '- Heat index....:'+  data['heat_index_string'])
        print_there(15,63, '- Feels Like....:'+  data['feelslike_string'])
        print_there(16,63, '- Rltv humidity :'+  data['relative_humidity'])
        print_there(17,63, '- Wind Degrees. :'+  data['wind_degrees'])
        print_there(18,63, '- Winds.........:'+  data['wind_string'])
        print_there(19,63, '- Winds Degrees.:'+  data['wind_degrees'])
        input()
        return 0





#-----------------------------------
def main():

    while True:

        os.system('clear')
        print('WELCOME TO  WEATHER DATA')
        print('\n\n')
        print('MAIN MENU:\n')
        print('1.) Current Conditions\n')
        print('2.) 10 day forecast\n')
        print('3.) Weather alerts\n')
        print('4.) Quit Program\n\n\n')

        user_menu_choice = input("Choose a number option and press enter: ")

        if catch_invalid_input(user_menu_choice,0):
            continue
        else:
            if get_menu_choices(user_menu_choice) == 0:
                continue
            else:
                print('\n\n')
                print("Bye... Have a Nice Day!")
                print('\n\n')
                sys.exit()




if __name__ == '__main__':
    main()
