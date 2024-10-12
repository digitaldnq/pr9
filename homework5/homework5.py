import random

def findGreaterElemThanPrevious(numbers):
    def greaterCheck():
        return [numbers[i] for i in range(1, len(numbers)) if numbers[i] > numbers[i - 1]]
    return greaterCheck()


if __name__ == "__main__":

    numbers = [random.randint(1, 100) for _ in range(10)]  
    print("Сгенерированный список чисел:", numbers)

    greaterElem = findGreaterElemThanPrevious(numbers)
    print("Элементы из сгенерированного списка, которые больше предыдущего элемента:", greaterElem)
