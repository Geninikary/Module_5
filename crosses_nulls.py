# 1 bord поле игры
# 2 ходы крестиков и ноликов
# 3 определение победителя и нечьи
# 4 цикл игры
# доска
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# количество клеток 3
# вывод игрового поля
def output_board():
    print('_' * 4 * 3)
    for i in range(3):
        print((' ' * 3 + '|') * 3)
        print('', board[i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
        print(('_' * 3 + '|') * 3)

# проверка хода
def step_on_game(index, char):
    if index > 9 or index < 1 or board[index - 1] in ('X', 'O'):
        return False

    board[index - 1] = char
    return True

# комбинации размещения знаков
def check_win():
    win = False

    win_combination = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # победа по дгоризонтали
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # победа по вертикали
        (0, 4, 8), (2, 4, 6)
    ]

    for i in win_combination:
        if board[i[0]] == board[i[1]] and board[i[1]] == board[i[2]]:
            win = board[i[0]]

    return win

# Цикл игры
def start_game():
    # текущий игрок
    current_player = 'X'
    # номер шага
    step = 1
    output_board()
    # ввод числа играком
    while step < 10 and check_win() is False:
        index = (input('Ходит игрок ' + current_player + '. Введите номер: (0 -для выхода)): '))
        if index == "0":
            print('выход')
            break

    # Очередность ходов
        if step_on_game(int(index), current_player):
            print('Удачный ход')
            if current_player == 'X':
                current_player = 'O'
            else:
                current_player = 'X'

                output_board()
                # Увеличен номер шага
                step += 1
        else:
            print('Неверный номер, повторите')
    if step == 10:
        print('Нечья')
    else:
        print('Выйграл ' + check_win())


print("Кресты-нули")
(start_game())