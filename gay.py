from random import randint
from time import sleep


count = 0


def input_name(name):
    print('Добро пожаловать в тест на гея!\n')
    name = input('Введите своё имя: ')
    return name


def design():
    for i in range(15):
        print('#', end = '')
        sleep(0.3)
    print('\n')


def first_question():
    global count
    answer = input('Вы когда-нибудь думали о том, чтобы стать геем? ')
    if (answer == 'Yes') or (answer == 'yes') or (answer == 'Да') or (answer == 'да') or (answer == 'Yep'):
        count += 1
    elif (answer == 'No') or (answer == 'no') or (answer == 'Нет') or (answer == 'нет') or (answer == 'Nope'):
        pass
    else:
        print('Вы ввели ответ в неверном формате. Попробуй ещё раз. У тебя всё получится!')
        first_question()


def second_question():
    global count
    answer = input('Не хотели бы вы засунуть свой палец in your ass (или вашего друга)? ')
    if (answer == 'Yes') or (answer == 'yes') or (answer == 'Да') or (answer == 'да') or (answer == 'Yep'):
        count += 1
    elif (answer == 'No') or (answer == 'no') or (answer == 'Нет') or (answer == 'нет') or (answer == 'Nope'):
        pass
    else:
        print('Вы ввели ответ в неверном формате. Попробуй ещё раз. У тебя всё получится!')
        second_question()


def third_question():
    global count
    answer = input('Кто вы по знаку зодиака (пиво или рыба)? ')
    if (answer == 'Рыба') or (answer == 'рыба'):
        count += 1
    elif (answer == 'Пиво') or (answer == 'пиво'):
        pass
    else:
        print('Вы ввели ответ в неверном формате. Попробуй ещё раз. У тебя всё получится!')
        third_question()


def questions():

    n1 = randint(1,3)
    if (n1 == 1):
        first_question()
    if (n1 == 2):
        second_question()
    if (n1 == 3):
        third_question()

    n2 = randint(1,3)
    while(n2 == n1):
        n2 = randint(1, 3)
    if (n2 == 1) and (n2 != n1):
        first_question()
    if (n2 == 2) and (n2 != n1):
        second_question()
    if (n2 == 3) and (n2 != n1):
        third_question()

    n3 = randint(1,3)
    while (n3 == n1) or (n3 == n2):
        n3 = randint(1, 3)
    if (n3 == 1) and (n3 != n1) and (n3 != n2):
        first_question()
    if (n3 == 2) and (n3 != n1) and (n3 != n2):
        second_question()
    if (n3 == 3) and (n3 != n1) and (n3 != n2):
        third_question()


def main():
    global count
    print('Добро пожаловать в тест на гея!\n')
    name = input('Введите своё имя: ')
    questions()
    if (count == 3):
        design()
        print(f'Поздравляем, {name}! Вы гей на 100%!')
    else:
        design()
        print(f'Поздравляем, {name}! Вы не гей на 100%!')

if __name__ == "__main__":
    main()
