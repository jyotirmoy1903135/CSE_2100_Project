#Base conversion among Decimal, Binary, Octal and Hexadecimal number systems.
print("Enter 1 to convert from decimal to binary.")
print("Enter 2 to convert from decimal to octal.")
print("Enter 3 to convert from decimal to hexadecimal.")
print("Enter 4 to convert from binary to decimal.")
print("Enter 5 to convert from binary to octal.")
print("Enter 6 to convert from binary to hexadecimal.")
print("Enter 7 to convert from octal to decimal.")
print("Enter 8 to convert from octal to binary.")
print("Enter 9 to convert from octal to hexadecimal.")
print("Enter 10 to convert from hexadecimal to decimal.")
print("Enter 11 to convert from hexadecimal to binary.")
print("Enter 12 to convert from hexadecimal to octal.")
print('Enter 0 to exit.\n\n')

while True:
    print("Enter your input: ", end="")
    option = int(input())

    if option == 1:
        print("Enter your decimal number: ", end="")
        n = int(input())
        n1 = n
        ans = ""
        while n1 != 0:
            p = n1 % 2
            ans = ans + str(p)
            n1 = n1 // 2

        ans = ans[::-1]
        ans = int(ans)
        print(f"The binary form of {n} is: {ans}\n")


    elif option == 2:
        print("Enter your decimal number: ", end="")
        n = int(input())
        n1 = n
        ans = ""
        while n1 != 0:
            p = n1 % 8
            ans = ans + str(p)
            n1 = n1 // 8

        ans = ans[::-1]
        print(f"The octal form of {n} is: {ans}\n")


    elif option == 3:
        print("Enter your decimal number: ", end="")
        n = int(input())
        n1 = n
        ans = ""
        while n1 != 0:
            p = n1 % 16

            if p <= 9:
                ans = ans + str(p)
            else:
                diction = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
                for key, value in diction.items():
                    if p == key: ans = ans + value

            n1 = n1 // 16

        ans = ans[::-1]
        print(f"The hexadecimal form of {n} is: {ans}\n")


    elif option == 4:
        print("Enter your binary number: ", end="")
        n = int(input())
        n1 = n
        ans = 0
        power = 0
        while n1 != 0:
            p = n1 % 10
            ans = ans + p * (2 ** power)
            n1 = n1 // 10
            power = power + 1

        print(f"The decimal form of {n} is: {ans}\n")


    elif option == 5:
        print("Enter your binary number: ", end="")
        n = input()
        n1 = n
        while len(n1)%3 != 0: n1 = '0' + n1
        ans = ""
        position = len(n1) - 1
        for i in range(len(n1) // 3):
            temp = ""
            for i in range(3):
                temp = temp + n1[position]
                position = position - 1
            temp = temp[::-1]

            diction = {'000':'0', '001':'1', '010':'2', '011':'3', '100':'4', '101':'5', '110':'6', '111':'7'}
            for key, value in diction.items():
                if temp == key: ans = ans + value

        ans = ans[::-1]
        print(f"The octal form of {n} is: {ans}\n")


    elif option == 6:
        print("Enter your binary number: ", end="")
        n = input()
        n1 = n
        while len(n1)%4 != 0: n1 = '0' + n1
        ans = ""
        position = len(n1) - 1
        for i in range(len(n1) // 4):
            temp = ""
            for i in range(4):
                temp = temp + n1[position]
                position = position - 1
            temp = temp[::-1]

            diction = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5',
                       '0110': '6', '0111': '7', '1000':'8', '1001':'9', '1010':'A',
                       '1011':'B', '1100':'C', '1101':'D', '1110':'E', '1111':'F',}
            for key, value in diction.items():
                if temp == key: ans = ans + value

        ans = ans[::-1]
        print(f"The hexadecimal form of {n} is: {ans}\n")


    elif option == 7:
        print("Enter your octal number: ", end="")
        n = int(input())
        n1 = n
        ans = 0
        power = 0
        while n1 != 0:
            p = n1 % 10
            ans = ans + p * (8 ** power)
            n1 = n1 // 10
            power = power + 1

        print(f"The decimal form of {n} is: {ans}\n")


    elif option == 8:
        print("Enter your octal number: ", end="")
        n = input()
        n1 = n[::-1]
        ans = ""
        position = len(n1) - 1

        for i in range(len(n1)):
            diction = {'0':'000', '1':'001', '2':'010', '3':'011', '4':'100', '5':'101', '6':'110', '7':'111'}
            for key, value in diction.items():
                if n1[position] == key: ans = ans + value

            position = position - 1

        print(f"The binary form of {n} is: {ans}\n")


    elif option == 9:
        print("Enter your octal number: ", end="")
        n = input()
        n1 = n[::-1]
        bin = ""
        position = len(n1) - 1

        for i in range(len(n1)):
            diction = {'0': '000', '1': '001', '2': '010', '3': '011', '4': '100', '5': '101', '6': '110', '7': '111'}
            for key, value in diction.items():
                if n1[position] == key: bin = bin + value

            position = position - 1

        bin1 = bin
        while len(bin1) % 4 != 0: bin1 = '0' + bin1
        ans = ""
        position = len(bin1) - 1
        for i in range(len(bin1) // 4):
            temp = ""
            for i in range(4):
                temp = temp + bin1[position]
                position = position - 1
            temp = temp[::-1]

            diction = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5',
                       '0110': '6', '0111': '7', '1000': '8', '1001': '9', '1010': 'A',
                       '1011': 'B', '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F', }
            for key, value in diction.items():
                if temp == key: ans = ans + value

        ans = ans[::-1]
        print(f"The hexadecimal form of {n} is: {ans}\n")


    elif option == 10:
        print("Enter your hexadecimal number: ", end="")
        n = input()
        position = len(n) - 1
        ans = 0
        power = 0
        while position >= 0:
            flag = 0

            diction = {'A':10, 'B':11, 'C': 12, 'D':13, 'E':14, 'F':15}
            for key, value in diction.items():
                if n[position] == key:
                    ans = ans + value * (16 ** power)
                    flag = 1
            if flag == 0: ans = ans + int(n[position]) * (16 ** power)

            power = power + 1
            position = position - 1

        print(f"The decimal form of {n} is: {ans}\n")


    elif option == 11:
        print("Enter your hexadecimal number: ", end="")
        n = input()
        n1 = n[::-1]
        ans = ""
        position = len(n1) - 1

        for i in range(len(n1)):
            diction = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101',
                       '6': '0110', '7': '0111', '8':'1000', '9':'1001', 'A':'1010',
                       'B':'1011', 'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}
            for key, value in diction.items():
                if n1[position] == key: ans = ans + value

            position = position - 1

        print(f"The binary form of {n} is: {ans}\n")


    elif option == 12:
        print("Enter your hexadecimal number: ", end="")
        n = input()
        n1 = n[::-1]
        bin = ""
        position = len(n1) - 1

        for i in range(len(n1)):
            diction = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101',
                       '6': '0110', '7': '0111', '8':'1000', '9':'1001', 'A':'1010',
                       'B':'1011', 'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}
            for key, value in diction.items():
                if n1[position] == key: bin = bin + value

            position = position - 1

        bin1 = bin
        while len(bin1) % 3 != 0: bin1 = '0' + bin1
        ans = ""
        position = len(bin1) - 1
        for i in range(len(bin1) // 3):
            temp = ""
            for i in range(3):
                temp = temp + bin1[position]
                position = position - 1
            temp = temp[::-1]

            diction = {'000': '0', '001': '1', '010': '2', '011': '3', '100': '4', '101': '5', '110': '6', '111': '7'}
            for key, value in diction.items():
                if temp == key: ans = ans + value

        ans = ans[::-1]
        print(f"The octal form of {n} is: {ans}\n")


    else: break
