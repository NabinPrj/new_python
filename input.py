'''a = input ("enter a number")



a = [1,3, [1,3,]]'''

info = {
            "name":"nabin",
            "surname":"prajapati"
}

print(type(info))

print(info['name'])


#Create dictionary inside list.

ls = [{

    "Item name" : "Meat",
    "Payment" : "Cash",
    'Rate/kg' : 100,
    'Weight in KG' : 2.750,
    'Total Amount' : 275

}]
print(type(ls))
print(ls)

ds = {
    "Delivery" : "Yes",
    "Payment" : "Done"
    }

ls.append(ds)

print(ls)