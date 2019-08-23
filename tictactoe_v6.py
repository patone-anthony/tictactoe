###### tictactoe

# todo - error handle for repeat choice position

locations = [i for i in range(1, 10)]
winconditions = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6), (0, 3, 6), (1, 4, 7), (2, 5, 8))

count = 0

print('Welcome to my TicTacToe Game')


def tictactoe():
    global count
    count += 1
    if count % 2 == 0:
        print()
        print('Player 2\'s turn:')
        printboard()
        turn()
        checkwin()
        tictactoe()
    else:
        print()
        print('Player 1\'s turn:')
        printboard()
        turn()
        checkwin()
        tictactoe()


def checkwin():
    for a in winconditions:
        if locations[a[0]] == locations[a[1]] == locations[a[2]] == 'X':
            printboard()
            print('Player 1 Wins!')
            exit()
        elif locations[a[0]] == locations[a[1]] == locations[a[2]] == 'O':
            printboard()
            print('Player 2 Wins!')
            exit()
        elif count == 9:
            printboard()
            print('It\'s a draw!')
            exit()


def turn():
    while True:
        try:
            turn = int(input('Enter your number here: '))
            if turn in locations and count % 2 == 0:  # p2
                locations[(turn) - 1] = "O"
                break
            elif turn in locations and count % 2 == 1:  # p1
                locations[(turn) - 1] = "X"
                break
            elif turn not in locations and turn in range(1, 10):
                print('That spot is alrady taken, choose another:')
            else:
                raise ValueError
        except (ValueError, TypeError):
            print('This isn\'t rocket science - try again!')


def printboard():
    print()
    print(f'{locations[6]} | {locations[7]} | {locations[8]}')
    print('---------')
    print(f'{locations[3]} | {locations[4]} | {locations[5]}')
    print('---------')
    print(f'{locations[0]} | {locations[1]} | {locations[2]}')
    print()

tictactoe()
