import random

def cyclicToRight(numbers):
    if not numbers:
        print("Список пуст.")
        return numbers

    last_element = numbers.pop()
    numbers.insert(0, last_element)

    return numbers


def game (numbers):
    pc_choice = random.choice(numbers)

    print("Угадайте число)")

    while True:
        try:
            user_choice = int(input("Введите ваше число: "))

            if user_choice not in numbers:
                print("Число должно быть из списка:", numbers)
                continue

            if user_choice == pc_choice:
                print("Поздравляем! Вы угадали число.")
                break
            else:
                print("Неверно! Выполняется циклический сдвиг списка.")
                numbers = cyclicToRight(numbers)
                print("Список после сдвига:", numbers)

        except ValueError:
            print("Введите корректное целое число.")

    return numbers

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    print("Исходный список:", numbers)

    numbers = game(numbers)
    print("Итоговый список:", numbers)
