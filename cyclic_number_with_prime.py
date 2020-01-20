# cyclic
# Obito
from colorama import Fore

#       colors

g = Fore.GREEN
r = Fore.RED
b = Fore.BLUE
rs = Fore.RESET
y = Fore.YELLOW
c = Fore.CYAN


# #################prime generator#######################
def prime(n):
    divisor = [2, 3, 5, 7]
    fix = [2, 3, 5, 7]
    for i in range(n):
        switch = True
        for items in divisor:
            if int(i % items) == 0:
                switch = False
                break
        if i != 1 and switch == True:
            if i < 9:
                fix.append(i)
            if 9 < i < 100:
                Y = True
                ff = f2(i)
                for i2 in divisor:
                     if int(ff % i2) == 0:
                        Y = False
                        break
                if Y:
                    fix.append(i)
                    if ff not in fix:
                        fix.append(ff)
            if 99 < i < 1000:
                T = True
                for ff2 in f3(str(i)):
                    for i3 in divisor:
                        if int(int(ff2)%i3) == 0:
                                T = False
                                break
                    if not T:
                        break
                if T:
                    fix.append(i)
                    for ff2 in f3(str(i)):
                        if int(ff2) not in fix:
                            fix.append(int(ff2))
            elif 999< i < 10000:
                T = True
                for ff3 in f4(str(i)):
                    for i4 in divisor:
                        if int(int(ff3)%i4) == 0:
                                T = False
                                break
                    if not T:
                        break
                if T:
                    fix.append(i)
                    for ff3 in f4(str(i)):
                        if int(ff3) not in fix:
                            fix.append(int(ff3))
            elif 9999< i < 100000:
                T = True
                for ff4 in f5(str(i)):
                    for i5 in divisor:
                        if int(int(ff4)%i5) == 0:
                                T = False
                                break
                    if not T:
                        break
                if T:
                    fix.append(i)
                    for ff4 in f5(str(i)):
                        if int(ff4) not in fix:
                            fix.append(int(ff4))
            elif 99999< i < 1000000:
                T = True
                for ff5 in f6(str(i)):
                    for i6 in divisor:
                        if int(int(ff5)%i6) == 0:
                                T = False
                                break
                    if not T:
                        break
                if T:
                    fix.append(i)
                    for ff5 in f6(str(i)):
                        if int(ff5) not in fix:
                            fix.append(int(ff5))
            elif 999999< i < 10000000:
                T = True
                for ff6 in f7(str(i)):
                    for i7 in divisor:
                        if int(int(ff6)%i7) == 0:
                                T = False
                                break
                    if not T:
                        break
                if T:
                    fix.append(i)
                    for ff6 in f7(str(i)):
                        if int(ff6) not in fix:
                            fix.append(int(ff6))
            divisor.append(i)
    return fix

# #####################Function###########################

def f2(number):
    number = str(number)
    number = number[::-1]
    return int(number)

def f3(number):
    numlist = [number]
    l = len(number)
    k = list(number)
    maxnum = facto(l)
    i = 0
    T = False
    for item in range(1,maxnum):
        num = [ k[ii] for ii in range(l)]
        if T:
            numlist.append(''.join(num))
            T = False
        if item%2 == 0:
            te = k[len(k)-3]
            k[len(k)-3] =  k[len(k)-1-i]
            k[len(k)-1-i] = te
            i += 1
            T = True
            continue
        temp = num[2]
        num[2] = num[1]
        num[1] = temp
        numlist.append(''.join(num))
    return numlist

def f4(number):
    numlist = []
    for i in range(4):
        klist = list(number)
        num = klist.pop(i)
        lis = f3(''.join(klist))
        for item in lis:
            numlist.append(num + str(item))
    return numlist

def f5(number):
    numlist = []
    for i in range(5):
        klist = list(number)
        num = klist.pop(i)
        lis = f4(''.join(klist))
        for item in lis:
            numlist.append(num + str(item))
    return numlist

def f6(number):
    numlist = []
    for i in range(6):
        klist = list(number)
        num = klist.pop(i)
        lis = f5(''.join(klist))
        for item in lis:
            numlist.append(num + str(item))
    return numlist

def f7(number):
    numlist = []
    for i in range(7):
        klist = list(number)
        num = klist.pop(i)
        lis = f6(''.join(klist))
        for item in lis:
            numlist.append(num + str(item))
    return numlist

def facto(m):
    m = int(m)

    def factorial(k):
        if k == 0:
            return 1
        else:
            return k * (factorial(k - 1))

    if type(m) == float:
        print('Type error')
    elif m < 0:
        return factorial(m * (-1)) * (-1)
    else:
        return factorial(m)

def pro():
    # #################variables##############################
    action = 'y'
    de = g + '+--------------------------------+' + rs
    message = ''

    # ################# main action ############################

    while action == 'y':
        try:
            print('\n' * 10)
            print('                           [' + g + 'Cyclic Prime Number' + rs + ']                                  ')
            print('+-----------------------------------------------------------------------+')
            print(
                ' |   1  |   ' + y + '2' + rs + '  |   ' + y + '3' + rs + '  |   4  |   ' + y + '5' + rs + '  |   6  |   ' + y + '7' + rs + '  |   8  |   9  |  10  |')
            print(
                ' |  ' + y + '11' + rs + '  |  12  |  ' + y + '13' + rs + '  |  14  |  15  |  16  |  ' + y + '17' + rs + '  |  18  |  ' + y + '19' + rs + '  |  20  |')
            print(
                ' |  21  |  22  |  ' + y + '23' + rs + '  |  24  |  25  |  26  |  27  |  28  |  ' + y + '29' + rs + '  |  30  |')
            print(
                ' |  ' + y + '31' + rs + '  |  32  |  33  |  34  |  35  |  36  |  ' + y + '37' + rs + '  |  38  |  39  |  40  |')
            print(
                ' |  ' + y + '41' + rs + '  |  42  |  ' + y + '43' + rs + '  |  44  |  45  |  46  |  ' + y + '47' + rs + '  |  48  |  49  |  50  |')
            print(
                ' |  51  |  52  |  ' + y + '53' + rs + '  |  54  |  55  |  56  |  57  |  58  |  ' + y + '59' + rs + '  |  60  |')
            print(
                ' |  ' + y + '61' + rs + '  |  62  |  63  |  64  |  65  |  66  |  ' + y + '67' + rs + '  |  68  |  69  |  70  |')
            print(
                ' |  ' + y + '71' + rs + '  |  72  |  ' + y + '73' + rs + '  |  74  |  75  |  76  |  77  |  78  |  ' + y + '79' + rs + '  |  80  |')
            print(
                ' |  81  |  82  |  ' + y + '83' + rs + '  |  84  |  85  |  86  |  87  |  88  |  ' + y + '89' + rs + '  |  90  |')
            print(' |  91  |  92  |  93  |  94  |  95  |  96  |  ' + y + '97' + rs + '  |  98  |  99  |  100 |')
            print('+-----------------------------------------------------------------------+')
            print('\n' * 5)
            print(g + 'That generate cyclic prime numbers between zero and maximum\n\n')
            number = int(input(b + 'Enter the max number' + c
                               + f'{message}' + ': '))

        except:
            message = r + '(only whole number)' + rs
            continue
        if number < 0:
            message = r + '(only whole number)' + rs
            continue
        # print('\n' * 10)

        result = open('result.txt', 'w')
        result.seek(0)
        result.write(' ')
        counter = 1
        for item in prime(number):
            if counter % 10 == 0:
                result.write('\n')
            result.write(str(item) + ' , ')
            print(r + '-' * 30 + '~ ' + g + str(item) + rs)
            counter += 1
        counter -= 1
        print(c + 'The numbers of prime between zero and maximum: ' + g + str(counter))

        print('\n\n')
        print(de)
        action = input(y + '\n\t"Save to result.txt"\n\n\tDo again?\n\t{-y-} to do again or\n\tPress enter to exit\n'
                       + de + '\n|-> ')
        message = ''


pro()
