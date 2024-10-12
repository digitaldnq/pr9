def getNumbers():
    numbers = [] 
    while True:
        userInput = input("Введите число (или end для завершения): ")
        if userInput.lower() == 'end':
            break
        try:
            number = int(userinput)
            numbers.append(number)
        except ValueError:
            print("Ошибка! Введите корректное число.")
    return numbers

def countEvenOdd(numbers):
    evenCount = sum(1 for num in numbers if num % 2 == 0)
    oddCount = sum(1 for num in numbers if num % 2 != 0)
    return evenCount, oddCount

numbers = getNumbers()
evenCount, oddCount = countEvenOdd(numbers)

print("Количество четных чисел:", evenCount)
print("Количество нечетных чисел:", oddCount)
