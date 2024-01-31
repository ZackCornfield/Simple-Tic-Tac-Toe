def print_grid(cells):
    print("---------")
    for i in range(0, 9, 3):
        print(f"| {' '.join(cells[i:i + 3])} |")
    print("---------")


def check_state(cells):
    x_wins = check_winner(cells, 'X')
    o_wins = check_winner(cells, 'O')

    if x_wins and o_wins or abs(cells.count('X') - cells.count('O')) >= 2:
        return "Impossible"
    elif x_wins:
        return "X wins"
    elif o_wins:
        return "O wins"
    elif '_' not in cells:
        return "Draw"
    else:
        return "Game not finished"


def check_winner(cells, player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
    for combo in winning_combinations:
        if all(cells[i] == player for i in combo):
            return True
    return False


def is_valid_input(coordinates):
    if not coordinates[0].isdigit() or not coordinates[1].isdigit():
        print("You should enter numbers!")
        return False
    elif not (1 <= int(coordinates[0]) <= 3) or not (1 <= int(coordinates[1]) <= 3):
        print("Coordinates should be from 1 to 3!")
        return False
    else:
        return True


def main():
    cells = ['_' for _ in range(9)]
    print_grid(cells)

    while True:
        while True:
            coordinates = input("Enter the coordinates: ").split()

            if len(coordinates) != 2:
                print("Enter two coordinates separated by a space.")
                continue

            row, col = coordinates
            if not is_valid_input(coordinates):
                continue

            row = int(row) - 1
            col = int(col) - 1
            index = row * 3 + col

            if cells[index] != '_':
                print("This cell is occupied! Choose another one!")
                continue

            cells[index] = 'X'
            print_grid(cells)
            state = check_state(cells)
            if state != "Game not finished":
                print(state)
                return

            break

        while True:
            coordinates = input("Enter the coordinates: ").split()

            if len(coordinates) != 2:
                print("Enter two coordinates separated by a space.")
                continue

            row, col = coordinates
            if not is_valid_input(coordinates):
                continue

            row = int(row) - 1
            col = int(col) - 1
            index = row * 3 + col

            if cells[index] != '_':
                print("This cell is occupied! Choose another one!")
                continue

            cells[index] = 'O'
            print_grid(cells)
            state = check_state(cells)
            if state != "Game not finished":
                print(state)
                return

            break


if __name__ == "__main__":
    main()
