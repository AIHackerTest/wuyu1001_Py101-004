# coding: utf-8
#!/usr/bin/env python3
import random

def random_num():
    """random of production four-digit via random Modules """
    my_list = [i for i in range(10)]
    num_list = random.sample(my_list, 4)
    while num_list[0] == 0:
        num_list = random.sample(my_list, 4)
       
    return num_list
    
def user_input():
    """set a user interface, and production a list"""
    guess_num = int(input("please type four-digit: "))
    guess_list = list(str(guess_num))
    return guess_list
    
def check_num(guess_list, num_list):
    count_a = 0
    count_b = 0
    for i in range(4):
        if int(guess_list[i]) == num_list[i]:
            count_a += 1
        if int(guess_list[i]) in num_list and int(guess_list[i]) != num_list[i]:
            count_b += 1
    return count_a, count_b
     
    
def main():
        print("这是一个猜数字游戏，你需要输入四位数字，")
        print("当你输入的数字和位置都正确系统会用A提示，\n数字正确但是位置不对会用B提示")
        num_list = random_num() # 不要循环的变量一定要放在循环外
        time = 0
        while time < 10:
            try:
                guess_list = user_input()
            except ValueError:
                print("请确认输入的是数字")
                continue # 可以避免当错误发生时跳出程序，保证程序继续运转
            count_a, count_b = check_num(guess_list, num_list)
            print("%dA%dB" % (count_a, count_b))
            print("你还有%d次机会" % (9-time))
            time += 1
            
            if count_a == 4:
                print("you're right! Good job")
                break
        print("正確數字是：")
        print(''.join(str(v) for v in num_list))
    
    
    
if __name__ == '__main__':
    main()