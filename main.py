from operator import truediv

import light_manager
import questionary

def display_game(table):
    for row in table:
        row_print = []
        for light in row:
            if light.on:
                row_print.append("X")
            else:
                row_print.append("O")
        print(row_print)

def validate_dimension(text):
    if not text.isnumeric():
        return "Please enter a number."
    if int(text) <= 0:
        return "Please enter a number greater than 0."
    return True


def main():
    height = int(questionary.text("Please enter the height", validate=validate_dimension).ask())
    width = int(questionary.text("Please enter the width", validate=validate_dimension).ask())
    light_manager_object = light_manager.light_manager(height, width)
    table = light_manager_object.return_table()
    #print(light_manager_object.lights[2].neighbours)
    #light_manager_object.lights[2].switched()
    #print(light_manager_object.lights[2].neighbours)
    display_game(table)



if __name__ == '__main__':
    main()