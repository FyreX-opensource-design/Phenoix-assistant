#imports
from datetime import datetime, date
from playaudio import playaudio 
import pyttsx3, whatnow

# globals
global temp_unit
global wind_speed_unit
read_weather_cfg = False
global time_format
time_format = 24
global date_format
date_format = "mdy"
# date functions

def day_of_week():
    dt = datetime.now()
    day_of_week_int = dt.weekday()
    if day_of_week_int == 0:
        day_of_week_name = "monday"
    elif day_of_week_int == 1:
        day_of_week_name = "tuesday"
    elif day_of_week_int == 2:
        day_of_week_name = "wendsday"
    elif day_of_week_int == 3:
        day_of_week_name = "thursday"
    elif day_of_week_int == 4:
        day_of_week_name = "friday"
    elif day_of_week_int == 5:
        day_of_week_name = "saturday"
    elif day_of_week_int == 6:
        day_of_week_name = "sunday"
    return day_of_week_name

def month_of_year():
    month_text = date.today().strftime("%B")
    return month_text

def _date():
    _date = int(date.today().month)
    if _date == 1:
        day = "first"
    elif _date == 2:
        day = "second"
    elif _date == 3:
        day = "third"
    elif _date == 4:
        day = "fourth"
    elif _date == 5:
        day = "fifth"
    elif _date == 6:
        day = "sixth"
    elif _date == 7:
        day = "seventh"
    elif _date == 8:
        day = "eighth"
    elif _date == 9:
        day = "ninth"
    elif _date == 10:
        day = "tenth"
    elif _date == 11:
        day == "eleventh"
    elif _date == 12:
        day == "twelfth"
    elif _date == 13:
        day == "thirteenth"
    elif _date == 14:
        day == "fourteenth"
    elif _date == 15:
        day = "fifteenth"
    elif _date == 16:
        day = "sixteenth"
    elif _date == 17:
        day = "seventeenth"
    elif _date == 18:
        day = "eightteenth"
    elif _date == 19:
        day = "nineteenth"
    elif _date == 20:
        day = "twentyieth"
    elif _date == 21:
        day = "twenty first"
    elif _date == 22:
        day = "twenty second"
    elif _date == 23:
        day = "twenty third"
    elif _date == 24:
        day = "twenty fourth"
    elif _date == 25:
        day = "twenty fifth"
    elif _date == 26:
        day = "twenty sixth"
    elif _date == 27:
        day = "twenty seventh"
    elif _date == 28:
        day = "twenty eighth"
    elif _date == 29:
        day = "twenty ninth"
    elif _date == 30:
        day = "thirtyieth"
    elif _date == 31:
        day = "thirty first"
    return day

def get_time_hour():
    now = datetime.now()
    time_hour = now.strftime("%H")
    return time_hour

def get_time_min():
    now = datetime.now()
    time_minite = now.strftime("%M")
    return time_minite

def say_date():
    pyttsx3.speak("today is " + day_of_week() + ", " + month_of_year() + " " + _date)

def say_time():
    read_data()
    if time_format == 24:
        pyttsx3.speak("it is currently " + get_time_hour() + " " + get_time_min())
    elif time_format == 12:
        if int(get_time_hour()) > 0 and int(get_time_hour()) < 12:
            pyttsx3.speak("it is currently " + get_time_hour() + " " + get_time_min() + " A M")
        elif int(get_time_hour()) > 12:
            pyttsx3.speak("it is currently " +  str(int(get_time_hour()) - 12) + " " + get_time_min() + " P M")
        elif int(get_time_hour()) == 0:
            pyttsx3.speak("it is currently 12 " +  get_time_min() + " A M")
        elif int(get_time_hour) == 12:
            pyttsx3.speak("it is currently 12 " +  get_time_min() + " P M")

def say_full_time():
    read_data()
    if time_format == 24:
        if date_format == "mdy":
            pyttsx3.speak("it is currently " + day_of_week() + ", " + month_of_year() + " " + _date() + " at " + get_time_hour() + " " + get_time_min())
        elif date_format == "dmy":
            pyttsx3.speak("it is " + day_of_week() + ", " + _date() + " of " + month_of_year() + " at " + get_time_hour() + " " + get_time_min())

# read cfg data
def read_data():
    with open("base_cfg.txt", "r") as file:
        for line in file.readline():
            if line == "## Temp Unit":
                temp_unit_read = True
            if temp_unit_read == True:
                if line == "C":
                    change_units_temp("C")
                    temp_unit_read = False
                elif line == "F":
                    change_units_temp("F")
                    temp_unit_read = False
                else:
                    raise SyntaxWarning("Temp units need to be in Celsius, \"C\" or Fahrenheit, \"F\"")
            if line == "## Wind Speed Unit":
                wind_speed_read_unit = True
            if wind_speed_read_unit == True:
                if line == "kph":
                    change_units_wind_speed("kph")
                    wind_speed_read_unit = False
                elif line == "mph":
                    change_units_wind_speed("mph")
                    wind_speed_read_unit = False
                else:
                    raise SyntaxWarning("Wind speed units need to be in mph or kph")
            if line == "## Time Format":
                time_format_read = True
            if time_format_read == True:
                if line == "12":
                    time_format = 12
                    time_format_read = False
                elif line == 24:
                    time_format = 24
                    time_format_read = False
                else:
                    raise SyntaxWarning("Time format must be 12 or 24")
            if line == "## date format":
                date_format_read = True
            if date_format_read == True:
                if line == "mdy":
                    date_format = "mdy"
                elif line == "dmy":
                    date_format = "dmy"
                else:
                    raise SyntaxWarning("date formats are mdy or dmy")
                    

# write cfg data
def write_data(cmd):
    with open("base_cfg.txt", "r") as file:
        data = file.readlines()
    if cmd == "unit_c":
        data[1] = "C\n"
    elif cmd == "unit_f":
        data[1] = "F\n"
    elif cmd == "wind_mph":
        data[3] = "mph\n"
    elif cmd == "wind_kph":
        data[3] = "kph\n"
    elif cmd == "12h":
        data[5] = "12\n"
    elif cmd == "24h":
        data[5] = "24\n"
    elif cmd == "mdy" or "dmy":
        data[7] = cmd
    with open("base_cfg.txt", "w"):
        file.writelines(data)
# weather functions

def change_units_temp(unit):
    if unit == "C":
        temp_unit = "C"
    elif unit == "F":
        temp_unit = "F"

def change_units_wind_speed(unit):
    if unit == "mph":
        wind_speed_unit = "mph"
    elif unit == "kph":
        wind_speed_unit = "kph"

def get_weather(request):
    with open("OpenWeatherMap_API_key.txt", "r") as file:
        key = file.readline()
    weather = whatnow.get_weather_details(whatnow.extract_city(whatnow.get_location()), key)
    if request == "city":
        return weather["City"]
    elif request == "temp":
        return weather["Temperature"][0:-2]
    elif request == "humid":
        return weather["Humidity"][0:-1]
    elif request == "wind":
        return weather["Wind Speed"][0:-5]
    
def convert_temp(temp_c):
    return round(temp_c * 1.8 + 32, 1)

def convert_to_mph(speed_ms):
    return round(speed_ms / 0.44704, 1)

def convert_to_kph(speed_ms):
    return round(speed_ms * 3.6, 1)

def say_wind_speed():
    if wind_speed_unit == "mph":
        pyttsx3.speak("The current wind speed is " + str(convert_to_mph(int(get_weather("wind")))) + " miles per hour")
    elif wind_speed_unit == "kph":
        pyttsx3.speak("The current wind speed is " + str(convert_to_kph(int(get_weather("wind")))) + " kilometers per hour")

# help cmd function

def say_help(cmd):
    if cmd == "time":
        pyttsx3.speak("gives you today's date")
    elif cmd == "wind":
        pyttsx3.speak("Give you the current wind speed in the area")

#bare minimum commands

def say_help_enabled():
    pyttsx3.speak("command help enabled")

def listen():
    playaudio("assets/ding-80828.mp3")
        