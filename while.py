
number = 100
while number > 0:
    print(number)
    number //= 2


command = ""
while command.lower() !="quit":
    command = input(">")
    print("ECHO", command)


#while True:
#    command = input(">")
#   print("ECHO", command)
#    if command.lower() !="quit":
#        break

x = 2
while x < 10:
    print(x)
    x += 2


for x in range(2,10,2):
    print(x)

count = 0
for number in range(1,10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"We have {count} even numbers")

def greet(first_name, last_name):
    print(f"Hi there {first_name} {last_name}")
    print("Welcome abroad")

greet("Mosh", "Hamedani")

# 1 - Perform a task
# 2 - Return a value

round (1.9)

def get_greeting(name):
    #print(f"Hi {name}")
    return name


print(greet("Mosh"))


