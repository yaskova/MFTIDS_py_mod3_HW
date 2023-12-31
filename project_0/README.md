# Проект 0. Угадай число

## Оглавление  
[1. Описание проекта](.README.md#Описание-проекта)  
[2. Какой кейс решаем?](.README.md#Какой-кейс-решаем)  
[3. Краткая информация о данных](.README.md#Краткая-информация-о-данных)  
[4. Этапы работы над проектом](.README.md#Этапы-работы-над-проектом)  
[5. Результат](.README.md#Результат)    
[6. Выводы](.README.md#Выводы) 

### Описание проекта    
Угадать загаданное компьютером число за минимальное число попыток.

:arrow_up:[к оглавлению](_)


### Какой кейс решаем?    
Нужно написать программу, которая угадывает число за минимальное число попыток

**Условия соревнования:**  
- Компьютер загадывает целое число от 0 до 100, и нам его нужно угадать. Под «угадать», подразумевается «написать программу, которая угадывает число».
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.

**Метрика качества**     
Результаты оцениваются по среднему количеству попыток при 1000 повторений

**Что практикуем**     
Учимся писать хороший код на Python


### Этапы работы над проектом  
1. Создание game.py — программы, которая загадывает случайное число от 1 до 100, затем запрашивает у пользователя ввод числа до тех пор, пока он его не угадает. После угадывания выводит число потребовавшихся попыток. 
2. Создание game_v2 — варианта игры, в которой компьютер играет сам с собой и ведет статистику по среднему числу потребовавшихся попыток.
3. Оптимизация game_v2 — внедрение алгоритма бинарного поиска для снижение числа попыток, которые требуются для угадывания числа.

:arrow_up:[к оглавлению](.README.md#Оглавление)


### Результаты:  
Среднее количество попыток при 1000 повторений сокращено до 7.

:arrow_up:[к оглавлению](.README.md#Оглавление)


### Выводы:  
Убедились в эффективности бинарного поиска для задачи угадывания числа за минимальное количество попыток.

:arrow_up:[к оглавлению](.README.md#Оглавление)

