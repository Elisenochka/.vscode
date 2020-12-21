def greet():
    print("HI there")
    print("Welcome abroad")

greet()

def greet(first_name, last_name):
    print(f"HI there {first_name} {last_name}")
    print("Welcome abroad")

greet("Mosh", "Hamedani")

# 1-Perform a task
# 2-Return a value

round(1.9)

def greet(name):
    print(f"Hi {name}")

def get_greeting(name):
    return f"Hi {name}"

message = get_greeting("Mosh")

file = open("content.txt", "w")
file.write(message)

print(greet("Elina"))

def increment(number, by):
    return number + by

print(increment(2,1))


def increment(number, by=1):
    return number + by

print(increment(2))