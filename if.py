'''if 3>4 or 5<6:
    print(True)
elif 3>4 and 5<6:
    print("test")
else:
    print("yo")'''

a = int(input(f"Enter your percentage: \t"))

if(a>=80 and a<=100):
    print('Distinction')
elif(a<80 and a>59):
    print('1st Division')
elif(a<60 and a>=50):
    print('2nd Division')
elif(a<50 and a>=40):
    print('3rd Division')
elif(a>100 or a<0):
    print('Not Available')
else:
    print('Fail')
