def getNumbers():
    numbers = []
    while True:
        user_input = input("Введите целое число (или end для завершения): ")
        if user_input.lower() == 'end':
            break  # Завершаем ввод при введении 'end'
        try:
            number = int(user_input)
            numbers.append(number)
        except ValueError:
            print("Ошибка! Введите корректное целое число.")
    return numbers

def filtrOddNumbers(numbers):
    return [num for num in numbers if num % 2 != 0]

numbers = getNumbers()
odd_numbers = filtrOddNumbers(numbers)
print("Нечётные числа из введённого списка:", odd_numbers)
