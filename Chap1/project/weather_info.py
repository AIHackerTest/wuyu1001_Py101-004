#!/usr/bin/env python3
    
def city_weather_info():
    """Reads lines from a file and builds a dict."""
    
    weather_dict = {}
    with open('weather_info.txt') as f:
        for line in f.readlines():
            word = line.strip().split(',')
            weather_dict[word[0]] = word[1]
            
    return weather_dict
    
def help_doc():
    """docstring for help"""
    print("""
        输入城市名你可以查询当地天气情况
        输入help或者 ?,可以寻求帮助
        输入history,可以查询搜索历史
        输入quit或者q，能够退出程序
        """)
    
           
def main():
    """docstring for main"""
    history = []
    weather_dict = city_weather_info()
    while True:
        user_input = input("请输入要查询的城市：")
        if user_input in weather_dict:
            weather = weather_dict[user_input]
            history.append(user_input)
            print(weather)
        
        elif user_input == 'his':
            
            print("查询过的城市：{}".format(history))
        
               
        elif user_input in ['quit', 'q']:
            break
            
        elif user_input in ['help', 'h', '?']:
            help_doc()
               
        else:
            pass
         
           
        

            
        
if __name__ == '__main__':
    main()       

    
