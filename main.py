import light_manager

def main():
    light_manager_object = light_manager.light_manager(4,4)
    table = light_manager_object.return_table()
    for row in table:
        print(row)
    print(light_manager_object.lights[5].neighbours)
    light_manager_object.lights[5].switched()
    print(light_manager_object.lights[5].neighbours)
    for row in table:
        print(row)



if __name__ == '__main__':
    main()