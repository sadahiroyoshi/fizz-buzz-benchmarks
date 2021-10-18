import sys
# import time

if __name__ == '__main__':
    n = int(sys.argv[1])

    fizzbuzz = 0
    fizz = 0
    buzz = 0
    none = 0

    # start = time.time()
    for i in range(1, n + 1):
        if i % 15 == 0:
            fizzbuzz += 1
        elif i % 3 == 0:
            fizz += 1
        elif i % 5 == 0:
            buzz += 1
        else:
            none += 1
    # print("elapsed_time:{0}".format(time.time()) + "[sec]")
    print("fizzbuzz:{0}".format(fizzbuzz))
    print("fizz:{0}".format(fizz))
    print("buzz:{0}".format(buzz))
    print("none:{0}".format(none))
