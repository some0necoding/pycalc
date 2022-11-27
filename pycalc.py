def get_numbers():

    numbers_list = input("Insert numbers [Back = B]: ").split()

    if (numbers_list[0] == 'E' or numbers_list[0] == 'e'):
        exit()
    elif (numbers_list[0] == 'B' or numbers_list[0] == 'b'):
        main_calculator()
    elif (len(numbers_list) < 2):
        print("You have to provide at least 2 numbers")
        main_calculator()
    else:
        return numbers_list


def operation(op_type):

    numbers_list = get_numbers()

    try:
        result = float(numbers_list[0])

        for number in numbers_list[1:]:
            num = float(number)
            
            if (op_type == '1'):
                result += num
            elif (op_type == '2'):
                result -= num
            elif (op_type == '3'):
                result /= num
            elif (op_type == '4'):
                result *= num

        return result
    except:
        print("You can only insert numbers")
        main_calculator()

def main_calculator():        

    op_type = input("\n"
                    "· Sum              [1]\n"
                    "· Subtraction      [2]\n"
                    "· Division         [3]\n"
                    "· Multiplication   [4]\n"
                    "· Exit             [E]\n"
                    "\n"
                    "Choose the operation: ")

    if (op_type == 'E' or op_type == 'e'):
        exit()
    elif (op_type != '1' and op_type != '2' and op_type != '3' and op_type != '4'):
        print("Invalid operation")
        main_calculator()

    print(operation(op_type))
    main_calculator()

main_calculator()