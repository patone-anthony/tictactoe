###### tictactoe

locations = [i for i in range(1, 10)]
winconditions = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6), (0, 3, 6), (1, 4, 7), (2, 5, 8))

count = 0

print('Welcome to my TicTacToe Game')


def gameplay():
    global count
    count += 1
    if count == 1:
        print('Player 1\'s turn, enter the number to mark your spot:')
        printboard()
        p1()
        checkwin()
    elif count % 2 == 0:
        print()
        print('Player 2\'s turn:')
        printboard()
        p2()
        checkwin()
    elif count % 2 == 1:
        print()
        print('Player 1\'s turn:')
        printboard()
        p1()
        checkwin()


def checkwin():
    for a in winconditions:
        if locations[a[0]] == locations[a[1]] == locations[a[2]] == 'X':
            print('Player 1 Wins!')
            endgame()
        elif locations[a[0]] == locations[a[1]] == locations[a[2]] == 'O':
            print('Player 2 Wins!')
            endgame()
        elif count == 9:
            print('It\'s a draw!')
            endgame()
        else:
            gameplay()


def p1():
    player1turn = int(input())
    locations[int(player1turn) - 1] = "X"


def p2():
    player2turn = int(input())
    locations[int(player2turn) - 1] = "O"


def printboard():
    print()
    print(f'{locations[6]} | {locations[7]} | {locations[8]}')
    print('---------')
    print(f'{locations[3]} | {locations[4]} | {locations[5]}')
    print('---------')
    print(f'{locations[0]} | {locations[1]} | {locations[2]}')
    print()
    print(locations)


def endgame():
    exit()


gameplay()

#test

