import os
import time
import math

exit = False
while exit == False:
    print('ax**2 + bx + c = 0')
    try:
        a = float(input('Vui lòng nhập 1 số cho a: '))
        time.sleep(0.25)
        b = float(input('Vui lòng nhập 1 số cho b: '))
        time.sleep(0.25)
        c = float(input('Vui lòng nhập 1 số cho c: '))
        time.sleep(0.25)
        os.system('cls')
        print('Loading~~~')
        time.sleep(1)
        os.system('cls')
        e = 4*a*c
        f = pow(b, 2)
        delta = f - e
        if delta < 0:
            print('Phương trình vô nghiệm')
        elif delta == 0:
            print('Phương trình có nghiệm kép')
            x = -b / (2*a)
            x = round(x, 2)
            print(str(x))
        elif delta > 0:
            print('Phương trình có 2 nghiệm')
            xFirst = (-b + math.sqrt(delta)) / (2*a)
            xFirst = round(xFirst, 2)
            xSecond = (-b - math.sqrt(delta)) / (2*a)
            xSecond = round(xSecond, 2)
            print('1. x = (-b + (căn)delta) / (2*a) = ' + '( ' + str(-b) + ' (căn)' +
                  str(delta) + ')' + ' / ' + '(2*' + str(a)+')' + ' = ' + str(xFirst))
            print( str(xSecond))
        userInput = input('Nhấn enter để tiếp tục làm lại, nhấn q để thoát: ')
        if userInput == 'q' or userInput == 'Q':
            exit = True
    except:
        os.system('cls')
        d = input('Không hợp lệ vui lòng thử lại')
        os.system('cls')
os.system('cls')
print ('Thanks for using this program!!!')
time.sleep(3)
