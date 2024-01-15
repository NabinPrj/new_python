#Take 5 input from user and store it in a list. Print each index value using f string command. Also input the user info and store in dict.


Name = input("Enter your first name: ")
Surname = input("Enter your second name: ")
Location = input("Enter your address: ")
Contact_no = input("Enter your mobile number: ")
Address = input("Enter your house number: ")

info = []

info.append(Name)
info.append(Surname)
info.append(Location)
info.append(Contact_no)
info.append(Address)

result = print(f'The entered information is as follows \n Name: {info[0]} \n Surname: {info[1]} \n  Location: {info[2]}  \n Mobile: {info[3]} \n Address: {info[4]}')

