from pythonping import ping
import datetime


for i in range(1,999999999999999,1):

    #crane1
    crane1 = ping('10.95.58.113', verbose=False, interval=0.1, timeout=1)

    if crane1.success():
        print('polaczenie ok z cranem 1, licznik:', i)
    else:
        with open('Cranes_logs.txt', 'a+') as log_file:
            now = datetime.datetime.now()
            datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)
            print('stracilem polaczenie crane 1, licznik:', i)
            log_file.write("crane 1 stracil polaczenie licznik {} czas: {} \n".format(i, now))


    #crane2
    crane2 = ping('10.95.58.123', verbose=False, interval=0.1, timeout=1)

    if crane2.success():
        print('polaczenie ok z cranem 2, licznik:', i)
    else:
        with open('Cranes_logs.txt', 'a+') as log_file:
            now = datetime.datetime.now()
            datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)
            print('stracilem polaczenie crane 2, licznik:', i)
            log_file.write("crane 2 stracil polaczenie licznik {} czas: {} \n".format(i, now))

    #crane3
    crane3 = ping('10.95.58.133', verbose=False, interval=0.1, timeout=1)

    if crane3.success():
        print('polaczenie ok z cranem 3, licznik:',i)
    else:
        with open('Cranes_logs.txt', 'a+') as log_file:
            now = datetime.datetime.now()
            datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)
            print('stracilem polaczenie crane 3, licznik:', i)
            log_file.write("crane 3 stracil polaczenie licznik {} czas: {} \n".format(i,now))


    #crane4
    crane4 = ping('10.95.58.143', verbose=False, interval=0.1, timeout=1)

    if crane4.success():
        print('polaczenie ok z cranem 4, licznik:',i)
    else:
        with open('Cranes_logs.txt', 'a+') as log_file:
            now = datetime.datetime.now()
            datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)
            print('stracilem polaczenie crane 4, licznik:', i)
            log_file.write("crane 4 stracil polaczenie licznik {} czas: {} \n".format(i,now))


    #crane5
    crane5 = ping('10.95.58.153', verbose=False, interval=0.1, timeout=1)

    if crane5.success():
        print('polaczenie ok z cranem 5, licznik:', i)
    else:
        with open('Cranes_logs.txt', 'a+') as log_file:
            now = datetime.datetime.now()
            datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)
            print('stracilem polaczenie crane 5, licznik:', i)
            log_file.write("crane 5 stracil polaczenie licznik {} czas: {} \n".format(i, now))


    #crane6
    crane6 = ping('10.95.58.163', verbose=False, interval=0.1, timeout=1)

    if crane6.success():
        print('polaczenie ok z cranem 6, licznik:', i)
    else:
        with open('Cranes_logs.txt', 'a+') as log_file:
            now = datetime.datetime.now()
            datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)
            print('stracilem polaczenie crane 6, licznik:', i)
            log_file.write("crane 6 stracil polaczenie licznik {} czas: {} \n".format(i, now))


    # crane7
    crane7 = ping('10.95.58.173', verbose=False, interval=0.1, timeout=1)

    if crane7.success():
        print('polaczenie ok z cranem 7, licznik:', i)
    else:
        with open('Cranes_logs.txt', 'a+') as log_file:
            now = datetime.datetime.now()
            datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)
            print('stracilem polaczenie crane 7, licznik:', i)
            log_file.write("crane 7 stracil polaczenie licznik {} czas: {} \n".format(i, now))

    # crane8
    crane8 = ping('10.95.58.183', verbose=False, interval=0.1, timeout=1)

    if crane8.success():
        print('polaczenie ok z cranem 8, licznik:', i)
    else:
        with open('Cranes_logs.txt', 'a+') as log_file:
            now = datetime.datetime.now()
            datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)
            print('stracilem polaczenie crane 8, licznik:', i)
            log_file.write("crane 8 stracil polaczenie licznik {} czas: {} \n".format(i, now))

    # crane9
    crane9 = ping('10.95.58.193', verbose=False, interval=0.1, timeout=1)

    if crane9.success():
        print('polaczenie ok z cranem 9, licznik:', i)
    else:
        with open('Cranes_logs.txt', 'a+') as log_file:
            now = datetime.datetime.now()
            datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)
            print('stracilem polaczenie crane 9, licznik:', i)
            log_file.write("crane 9 stracil polaczenie licznik {} czas: {} \n".format(i, now))

    # crane10
    crane10 = ping('10.95.58.203', verbose=False, interval=0.1, timeout=1)

    if crane10.success():
        print('polaczenie ok z cranem 10, licznik:', i)
    else:
        with open('Cranes_logs.txt', 'a+') as log_file:
            now = datetime.datetime.now()
            datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)
            print('stracilem polaczenie crane 10, licznik:', i)
            log_file.write("crane 10 stracil polaczenie licznik {} czas: {} \n".format(i, now))

    # crane11
    crane11 = ping('10.95.58.213', verbose=False, interval=0.1, timeout=1)

    if crane11.success():
        print('polaczenie ok z cranem 11, licznik:', i)
    else:
        with open('Cranes_logs.txt', 'a+') as log_file:
            now = datetime.datetime.now()
            datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)
            print('stracilem polaczenie crane 11, licznik:', i)
            log_file.write("crane 11 stracil polaczenie licznik {} czas: {} \n".format(i, now))

    # crane12
    crane12 = ping('10.95.58.223', verbose=False, interval=0.1, timeout=1)

    if crane12.success():
        print('polaczenie ok z cranem 12, licznik:', i)
    else:
        with open('Cranes_logs.txt', 'a+') as log_file:
            now = datetime.datetime.now()
            datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)
            print('stracilem polaczenie crane 12, licznik:', i)
            log_file.write("crane 12 stracil polaczenie licznik {} czas: {} \n".format(i, now))



