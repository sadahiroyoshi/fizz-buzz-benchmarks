import sys
# import time

if __name__ == '__main__':
    n = int(sys.argv[1])

    # start = time.time()
    for i in range(1, n + 1):
        if i % 15 == 0:
            print('fizzbuzz')
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else:
            print(i)
    # print("elapsed_time:{0}".format(time.time()) + "[sec]")
