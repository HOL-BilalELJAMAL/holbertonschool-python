#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        operator = sys.argv[2]
        operand1 = int(sys.argv[1])
        operand2 = int(sys.argv[3])
        if operator == "+":
            print("{} + {} = {}".format(operand1, operand2,
                                        add(operand1, operand2)))
        elif operator == "-":
            print("{} + {} = {}".format(operand1, operand2,
                                        sub(operand1, operand2)))
        elif operator == "*":
            print("{} + {} = {}".format(operand1, operand2,
                                        mul(operand1, operand2)))
        elif operator == "/":
            print("{} + {} = {}".format(operand1, operand2,
                                        div(operand1, operand2)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
