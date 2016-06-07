import pyowm
import os


def get_hamilton_weather():
    # obtain OWM api key from local environment
    owm_key_id = os.environ.get("OWM")
    # create an OWM object
    owm = pyowm.OWM(owm_key_id)
    # obtain forecaster object
    fc = owm.daily_forecast("Hamilton,ca", limit=3)
    # obtain a forecast object which contains multiple weather objects.
    f = fc.get_forecast()
    result = 'Three days forecast: \n'
    for weather in f:
         time, status, temp = (weather.get_reference_time('iso')[:10], weather.get_status(), weather.get_temperature(unit='celsius'))
         result += "Data: {0}, Weather: {1}, Temperature: {2:.0f}-{3:.0f} C\n".format(time, status, temp[u"min"], temp[u"max"])
    # print result
    return result


if __name__ == "__main__":
    get_hamilton_weather()
# obs = owm.weather_at_place('Toronto,ca')
# w = obs.get_weather()
# result = w.get_temperature(unit='celsius')
# print result
