total = 0

while True:
    number = int(input("Enter a number: "))

    if number < 0:
        break
    elif number == 0:
        continue
    else:
        print("Positive number:", number)
        total += number

print("Total:", total)