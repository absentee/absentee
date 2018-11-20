import random


target = (100, 62.137)
ratio = random.random()
alpha = 0.00001
for i in range(100):
    x, y = target[0], target[1]
    print(ratio)
    derivative = 2 * ratio * x ** 2 - 2 * x * y
    delta_ratio = - alpha * derivative
    ratio = ratio + delta_ratio



