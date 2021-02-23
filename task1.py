import math


def f11(x, y, z):
    return math.sqrt(math.pow(x, 8) + (math.pow(x, 5) / 23)) + (
            (math.cos(x) + math.tan(x)) / (math.pow(z, 7) - abs(x))) + math.sqrt(
        math.pow(y, 7) + math.exp(y))


def f12(x):
    if x < 61:
        f = math.pow((73 * math.pow(x, 4) + math.sin(x)), 6) - math.pow(x, 3)
    elif x < 115:
        f = x - 46 * math.pow(x, 4)
    elif x < 169:
        f = abs(math.exp(x) - (math.pow(x, 5) / 53)) + (x / 17)
    else:
        f = math.exp(math.pow(x, 2) + 8 * math.pow(x, 5) + 25) - math.pow(x, 4) - 75
    return f


def f13(n, m):
    r1 = 0
    r2 = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            r1 += i ** 6 + 17 * j ** 2
    for i in range(1, n + 1):
        r2 += 58 * i ** 7 - 22 * i
    return 62 * r1 - 98 * r2


def f14(n):
    if n == 0:
        return 6
    else:
        return math.cos(f14(n - 1)) + (1 / 9) * f14(n - 1) - 25


"""(f11(-62, 84, 38))
print(f11(34, 55, -26))
print("")
print(f12(52))
print(f12(36))
print("")
print(f13(75, 56))
print(f13(76, 61))
print("")
print(f14(5))
print(f14(13))"""
