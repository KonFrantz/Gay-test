from random import randint
from time import sleep

def input_name(name):
    print('Добро пожаловать в тест на гея!\n')
    name = input('Введите своё имя: ')
    return name


def design():
    for i in range(15):
        print('#', end = '')
        sleep(0.3)
    print('\n')


def main():
    print('Добро пожаловать в тест на гея!\n')
    name = input('Введите своё имя: ')
    if (name == 'Костя') or (name == "Константин") or (name == 'Константин Васильев') or name == ('Константин Васильев Евгеньевич'):
        design()
        print("Вы гей на 100%. Поздравляем!")
    else:
        design()
        print("Вы гей на", randint(1, 100), end = '')
        print('%. Поздравляем!')

if __name__ == "__main__":
    main()