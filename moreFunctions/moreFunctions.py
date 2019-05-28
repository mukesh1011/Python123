def parabola(x):
    y = x * x
    return y

myvar = 10
if __name__ == "__main__":
    for x in range(-100, 100):
        y = parabola(x)
        print(y)

