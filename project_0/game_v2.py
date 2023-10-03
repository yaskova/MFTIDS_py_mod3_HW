"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    nums_list = range(1, 101) # список значений, которые может принять число: по условию от 1 до 100

    while True:
        count += 1
        predict_number = np.random.choice(nums_list) # предполагаемое число случайно выбираем из списка возможных значений
        
        if number == predict_number:
            # выход из цикла если угадали
            break  
        elif number < predict_number:
            # если загаданное число меньше предполагаемого, отрезаем от списка возможных значений все числа, которые больше предполагаемого
            nums_list = nums_list[0:nums_list.index(predict_number)] 
        else: 
            # если загаданное число больше предполагаемого, отрезаем от списка возможных значений все числа, которые меньше предполагаемого
            nums_list = nums_list[nums_list.index(predict_number)+1:]
        
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
