# n = int(input("Enter the time in seconds:"))
# def countdown_time(n):
#     while n>0:
#         m = int(n/60)
#         s = int(n%60)
#         timer = f'{m}:{s}'
#         print(timer)
#         n-=1
#     print("Time up!")
# countdown_time(n)
import random

while True:
    n = random.randint(1,6)
    if n == 1:
        print("[---------]")
        print("[         ]")
        print("[    0    ]")
        print("[         ]")
        print("[---------]")
    elif n == 2:
        print("[---------]")
        print("[      0  ]")
        print("[         ]")
        print("[  0      ]")
        print("[---------]")
    elif n == 3:
        print("[---------]")
        print("[         ]")
        print("[ 0  0  0 ]")
        print("[         ]")
        print("[---------]")
    elif n == 4:
        print("[---------]")
        print("[  0   0  ]")
        print("[         ]")
        print("[  0   0  ]")
        print("[---------]")
    elif n == 5:
        print("[---------]")
        print("[  0   0  ]")
        print("[    0    ]")
        print("[  0   0  ]")
        print("[---------]")
    elif n == 6:
        print("[---------]")
        print("[ 0  0  0 ]")
        print("[         ]")
        print("[ 0  0  0 ]")
        print("[---------]")
    yn = input("Enter y/n to continue/stop: ")
    if yn == 'y':
        continue
    elif yn == 'n':
        break