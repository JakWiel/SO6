num1 = input('Wpisz pierwsza liczbe: ')
num2 = input('Wpisz druga liczbe: ')
op = input('Wpisz operacje ( +, -, /, * ): ')

match op:
    case "+":
        print(int(num1) + int(num2))
    case "-":
        print(int(num1) - int(num2))
    case "/":
        print(float(num1) / float(num2))
    case "*":
        print(int(num1) * int(num2))
    case _:
        print('Niepoprawna operacja')