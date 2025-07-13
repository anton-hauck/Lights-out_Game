import light_manager
import questionary

def main():
    light_manager_object = light_manager.light_manager(4,4)
    table = light_manager_object.return_table()
    #print(light_manager_object.lights[2].neighbours)
    #light_manager_object.lights[2].switched()
    #print(light_manager_object.lights[2].neighbours)
    for row in table:
        row_print = []
        for light in row:
            if light.on:
                row_print.append("X")
            else:
                row_print.append("O")
        print(row_print)

    while True:
        #hier weitermachen mit questionary



if __name__ == '__main__':
    main()