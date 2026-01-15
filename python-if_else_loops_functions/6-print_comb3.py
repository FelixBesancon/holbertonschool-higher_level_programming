#!/usr/bin/python3
for number in range(100):
    if (number == 89):
        print("{}".format(number))
        break
    elif ((number // 10) == (number % 10) or (number // 10) > (number % 10)):
        continue
    print("{:02d},".format(number), end=" ")
