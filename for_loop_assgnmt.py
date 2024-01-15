# numbers_list = [1,3,5,7,9]
usr_input = int(input("Enter the digits to generate the multiplication table of: "))

numbers = []

if usr_input>5:
    print("Invalid")

else:
    for i in range(1,usr_input+1,1):
        digit = int(input(f'Enter the numbers to generate tables of: '))
        numbers.append(digit)


    print(f'The multiplication tables are as follows :')
    for x in numbers:
        print("\n")
        for i in range(1,11):
            print(f'{x} x {i}= {x*i}')

    else:
        print("for loop ended")
