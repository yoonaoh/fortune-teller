"""
Simple Terminal Fortune Teller Game
05/30/22
"""

colors = ['red', 'blue', 'yellow', 'green']
group_1_nums = [1, 2, 5, 6]
group_2_nums = [3, 4, 7, 8]
fortunes = [
    "you're going to get a message from an old friend",
    "something will happen that will inspire you to take action",
    "you're going to remember what you've been missing",
    "you're going to have new energy come into your life",
    "you're going to get extra rest tonight",
    "something will happen that will fill your heart with joy",
    "you will get a well-deserved break soon",
    "you will go on an adventure today"
]
counter = 0


def fold_color(color: str):
    for char in color:
        print(char)


def fold_number(number: int):
    for i in range(1, number + 1):
        print(i)


def validate_input(choice, options):
    if choice not in options:
        first_options = ', '.join(map(lambda x: str(x), options[:len(options) - 1]))
        last_option = str(options[len(options) - 1])
        print(str(choice)+" is not a valid selection. Please enter either "+first_options+", or "+last_option+".")
        return False
    else:
        return True


def pick_color():
    global counter
    valid_color = False
    print("Pick a color: [red, blue, yellow, green]")
    while not valid_color:
        color_choice = input("Enter color: ")
        valid_color = validate_input(color_choice.lower(), colors)
        if valid_color:
            fold_color(color_choice.lower())
            counter += len(color_choice)
            break


def pick_number():
    global counter
    valid_number = False
    if counter % 2 == 0:
        print("Pick a number: [1, 2, 5, 6]")
        while not valid_number:
            number_choice = input("Enter number: ")
            valid_number = number_choice.isdigit() and validate_input(int(number_choice), group_1_nums)
            if valid_number:
                number = int(number_choice)
                fold_number(number)
                counter += number
                return number
    else:
        print("Pick a number: [3, 4, 7, 8]")
        while not valid_number:
            number_choice = input("Enter number: ")
            valid_number = number_choice.isdigit() and validate_input(int(number_choice), group_2_nums)
            if valid_number:
                number = int(number_choice)
                fold_number(number)
                counter += number
                return number


def pick_fortune(number: int):
    print(fortunes[number - 1])


def end_game():
    valid_end_game = False
    print("Do you want to play again? Type y for yes and n for no")
    while not valid_end_game:
        end_game_choice = input("Enter y or n: ")
        valid_end_game = validate_input(end_game_choice, ['y', 'n'])
        if valid_end_game and end_game_choice == 'n':
            return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while True:
        counter = 0

        pick_color()
        pick_number()
        final_num = pick_number()
        pick_fortune(final_num)

        if end_game():
            print('End of the game')
            break
