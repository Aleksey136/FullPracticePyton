import math


def function(xFunc, yFunc):
    return math.sqrt(xFunc ** 6 / 2 + 70 * xFunc ** 7) + math.sqrt(yFunc ** 2 - 97 * yFunc ** 7) + math.sqrt(
        (math.exp(xFunc) - 13 * yFunc ** 4) / (xFunc - yFunc ** 5))


if __name__ == "__main__":
    x = float(input("Введите число x: "))
    y = float(input("Введите число y: "))
    print("f(" + str(x) + ", " + str(y) + ") = {:.2e}".format(function(x, y)))
