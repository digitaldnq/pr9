def intInput(s1):
    while True:
        try:
            return float(input(s1))
        except ValueError:
            print("Некорректный ввод, введите целое число.")

def squaresBetween(a, b):
    start = int(min(a, b)) + 1
    end = int(max(a, b)) + 1
    squares = [i**2 for i in range(start, end)]
    return squares

def differentNum():
    while True:
        a = intInput("Введите число (a): ")
        b = intInput("Введите число (b): ")
        if a != b:
            return a, b
        else:
            print("Числа не должны быть одинаковыми. Введите, разные числа.")

a, b = differentNum()

squares = squaresBetween(a, b)
if squares:
    print("Квадраты чисел между", a, "и", b, ":", squares)
else:
    print("Между числами", a, "и", b, "нет целых чисел для возведения в квадрат.")
