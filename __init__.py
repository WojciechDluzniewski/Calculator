import operations

calculator = operations.Calculator(None, None)


def get_the_operation_answer():
    """
    Method gets the operation selected by the user
    :return:
    """
    print("What mathematical operation would you like to perform?")
    print("1. Add")
    print("2. Subtract")
    print("3. Divide")
    print("4. Multiply")
    operation_chosen = input(f"Please choose and type number from 1 to 4: ")
    match operation_chosen:
        case "1":
            add = operations.Add(None, None)
            print(add.make_calculation(calculator.get_first_number(), calculator.get_second_number()))
        case "2":
            subtract = operations.Subtract(None, None)
            print(subtract.make_calculation(calculator.get_first_number(), calculator.get_second_number()))
        case "3":
            divide = operations.Divide(None, None)
            print(divide.make_calculation(calculator.get_first_number(), calculator.get_second_number()))
        case "4":
            multiply = operations.Multiply(None, None)
            print(multiply.make_calculation(calculator.get_first_number(), calculator.get_second_number()))

