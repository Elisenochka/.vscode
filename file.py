try:
    file = open("file.py")
    age = int(input("Age:"))
    xfactor = 10/age
except (ValueError, ZeroDIcisionError) as e:
    print("You didn't enter a valid age")
    print(e)
    print(type(e))
    
else:
    print("No exceptions wer thrown")
finally:
    file.close()
print("Execution continues.")


try:
    with open("file.py") as file, open("another.txt") as target:
        print("File opened:")
        file.__exit
    age = int(input("Age:"))
    xfactor = 10/age
except (ValueError, ZeroDIcisionError) as e:
    print("You didn't enter a valid age")
    print(e)
    print(type(e))
    
else:
    print("No exceptions wer thrown")
finally:
    file.close()
print("Execution continues.")