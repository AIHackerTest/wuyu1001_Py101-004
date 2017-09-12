# cording: utf-8
from random import randint
import string
from sys import exit



num = randint(0, 20)
print("ready go!")
print("你有十次机会猜测")

for i in range(10):
    input_num = int(input("请输入数字：" ))
    print("你还有%d次机会" % (9-i))


    if input_num > num:
        print("大了")

    elif input_num < num:
        print("小了")

    else:
        print("you are right! good job")
        break
