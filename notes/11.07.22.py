# Rounding
num1 = 105.65
num2 = 99.3524816
print(round(num1, 0))
print(round(num2, 2))

#Try/catch
number = "float"
try:
    asNumber = int(number)
    print(asNumber)
except:
    print("unable to convert " + number + " to an integer")