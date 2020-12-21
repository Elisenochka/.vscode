numbers = [1,2]
#print(numbers[3])

try:
    age = int(input("age: "))
    xfactor = 10/age
except ValueError as e:
    print("You didn't enter a valid age")
    print(e)
    print(type(e))
except ZeroDIcisionError:
    print("wou didn't enter a valid age")
else:
    print("No exceptions wer thrown")
print("Execution continues.")

