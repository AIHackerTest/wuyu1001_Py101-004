import requests
import json
from utils.const_value import API, KEY, UNIT, LANGUAGE
from utils.helper import getLocation

def fetchWeather(location):
    try:
        result = requests.get(API, params={
                'key': KEY,
                'location': location,
                'language': LANGUAGE,
                'unit' : UNIT
               }, timeout=20)
        return result.text
    except ValueError:
        print("没有找到需要查询的城市，请重新输入")

def help_doc():
    print(
        """
        输入help,h,?可以获得帮助
        输入history可以得到查询历史
        输入quit,q退出程序
        输入城市名可以查询当地实时天气情况

        """
    )

def parse_data(data):
    data = json.loads(data)
    weather_info = data['results'][0]
    weather_now = weather_info['now']
    get_text = weather_now.get('text')
    temperature = weather_now.get('temperature')
    weather_location = weather_info['location']
    get_name = weather_location.get('name')
    return get_text, temperature, get_name 

def get_user():
    user_input = input("请输入要查询的城市：")
    return user_input

def main():
    history = []
    while True:
        user_input = get_user()
        history.append(user_input)
        if user_input in ['quit', 'q']:
            break

        elif user_input in ['help', 'h', '?']:
            help_doc()

        elif user_input == 'history':
            print("查询历史记录为:{}".format(history))

        else:
            data = fetchWeather(user_input)
            get_text, temperature, get_name = parse_data(data)
            print("{}城市天气{}，当前温度{}".format(get_name, get_text, temperature))


if __name__ == '__main__':
    main()
