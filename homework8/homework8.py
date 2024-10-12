import random

def getUserChoice(ticket):
    user_choices = []
    print("Выберите по одному числу из каждой строки:")
    for row in ticket:
        while True:
            try:
                user_choice = int(input(f"Введите число из {row}: "))
                if user_choice in row:
                    user_choices.append(user_choice)
                    break
                else:
                    print(f"Число должно быть одним из: {row}")
            except ValueError:
                print("Введите корректное целое число.")
    return user_choices

def getPcChoices(ticket):
    pc_choices = [random.choice(row) for row in ticket]
    return pc_choices

def calculateStat(user_choices, pc_choices):
    matches = set(user_choices) & set(pc_choices)
    match_count = len(matches)
    return match_count, matches

def main():
    ticket = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25],
    ]

    user_choices = getUserChoice(ticket)
    print("Ваш выбор:", user_choices)

    pc_choices = getPcChoices(ticket)
    print("Выбор компьютера:", pc_choices)

    match_count, matches = calculateStat(user_choices, pc_choices)
    print(f"Количество совпадений: {match_count}")
    if matches:
        print(f"Совпавшие числа: {sorted(matches)}")
    else:
        print("Нет совпавших чисел.")

if __name__ == "__main__":
    main()
