units_consumed = int(input("How many units you have consumed..."))


if units_consumed<100:
    amount = units_consumed*2
    surcharge = 20
elif units_consumed<=200:
    amount = units_consumed*3
    surcharge = 20
elif units_consumed<=300:
    amount = units_consumed*4
    surcharge = 20
elif units_consumed<=400:
    amount = units_consumed*5
    surcharge = 20
elif units_consumed<=500:
    amount = units_consumed*6
    surcharge = 20
elif units_consumed<=600:
    amount = units_consumed*7
    surcharge = 20
else:
    amount = units_consumed*15
total = amount+surcharge
print(total)
    