import random

#Задание 1
def guess_the_number():
    secret_number = random.randint(1, 100)
    attempts = 0
    guess = None

    print("загадано число от 1 до 100")

    while guess != secret_number:
        try:
            guess_str = input("число: ")
            guess = int(guess_str)
        except ValueError:
            print("введи целое число")
            continue

        attempts += 1

        if guess < secret_number:
            print("загаданное число больше")
        elif guess > secret_number:
            print("загаданное число меньше")

    print(f"ты угадал число {secret_number} за {attempts} попыток.")

print('ЗАДАНИЕ 1:')
guess_the_number()

#Задание 2
def group_characters(input_string):

    symbols = input_string.split()
    if not symbols:
        return []

    result = []
    current_group = [symbols[0]]

    for i in range(1, len(symbols)):
        if symbols[i] == current_group[-1]:
            current_group.append(symbols[i])
        else:
            result.append(current_group)
            current_group = [symbols[i]]

    result.append(current_group)
    return result


print('ЗАДАНИЕ 2:')
input_str = input("введите строку символов, разделенных пробелами: ")
grouped_list = group_characters(input_str)
print(grouped_list)

#Задание 3
def blackjack():
    cards = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4
    random.shuffle(cards)

    user_points = 0

    print("добро пожаловать в игру 'Блекджек'!")

    while True:
        take_card = input("Хотите взять карту? (y/n): ").lower()

        if take_card == "n":
            print(f"ваши очки: {user_points}")
            print("спасибо за игру")
            break
        elif take_card == "y":
            if not cards:
                print("в колоде закончились карты, игра завершена")
                print(f"ваши очки: {user_points}.")
                break
            card = cards.pop()
            user_points += card

            print(f"вы вытянули карту номиналом {card}. ваши очки: {user_points}")

            if user_points > 21:
                print("перебор! вы проиграли")
                print(f"ваши очки: {user_points}")
                break
            elif user_points == 21:
                print("блекджек! вы выиграли")
                print(f"ваши очки: {user_points}")
                break
        else:
            print("некорректный ввод")

print('ЗАДАНИЕ 3:')
blackjack()