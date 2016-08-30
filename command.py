from weather import get_hamilton_weather
from basicfunction import get_name, get_favourite_food, get_favourite_sports
from sharemoney import get_shared_money
# command dict
command_dict = {
    "name": get_name,
    "food": get_favourite_food,
    "sports": get_favourite_sports,
    "weather": get_hamilton_weather,
    "money": get_shared_money,
}
