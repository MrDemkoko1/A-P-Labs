import math as m

# Task_1

# 1.
# Range: [3, 6]
# Step: 0,3
# Function-1-1: 1/(sin(1/x)+4)
# Condition-1: x < 4
# Function-2: 1/(x**2 + ln(x))
# Condition-2: 4 <= x < 5
# Function-3: tg((x-3)**3)
# Condition-3: x >= 5

step = 0.3

def func1(x):
    print('Function: 1/(sin(1/x)+4)')
    return 1 / (m.sin(1/x) + 4)

def func2(x):
    print('Function: 1/(x**2 + ln(x))')
    return 1 / (x**2 + m.log(x))

def func3(x):
    print('Function: tg((x-3)**3)')
    return m.tan((x-3) ** 3)

for i in range(11):
    x = 3 + round(i * step, 1)
    print(f'x = {x}')
    if x <= 4:
        print(func1(x))
    elif x < 5:
        print(func2(x))
    else:
        print(func3(x))