
temperature = 30
if temperature > 30:
    print("It's warm")
    print("Drink water")
elif temperature > 20:
    print("It's nice")
else:
    print("It's cold")
print("Done")


age = 22
if age >=18:
    message = "Eligible"
else:
    message = "Not eligible"
message = "Eligible" if age >=18 else "Not eligible"
print(message)

high_income = True
good_credit = True
student = False

if high_income and good_credit and not student:
    print("Eligible")
else:
    print("Not eligible")


age = 22
if 18 <= age < 65:
    print("eligible")

if 10 == "10":
    print("a")
elif "bag" > "apple" and "bag" > "cat":
    print("b")
else:
    print("c")


successful = True
for number in range(1,10,2):
    print("Attempt", number + 1, (number + 1) * ".")
    if successful:
        print("Successful")
        break
else:
    print("Attempted", int(10/2), "times and failed")


for x in range(5):
    for y in range(3):
        print(f"({x},{y})")

print(type(5))
print(type(range(5)))

for x in range(5):
    print(x)


for x in "Python":
    print(x)

for x in [1,2,3,4]:
    print(x)

for item in shopping_cart:
    print(item)

