number_of_rows = 4
seats_per_row = 5

seats = []

for i in range(number_of_rows):
    row = ["."] * seats_per_row
    seats.append(row)
while True:
    for i in range(number_of_rows):
        print(f"Row {i + 1}:", end=" ")
        for j in range(seats_per_row):
            print(seats[i][j], end=" ")
        print()
    row_number = int(input("Row (0 to stop): "))
    if row_number == 0:
        break
    seat_number = int(input("Seat: "))

    if row_number < 1 or row_number > number_of_rows or seat_number < 1 or seat_number > seats_per_row:
        print("Invalid seat.")
    elif seats[row_number - 1][seat_number - 1] == "X":
        print("Seat already taken.")
    else:
        seats[row_number - 1][seat_number - 1] = "X"
        print("Seat booked.")
taken = 0

for i in range(number_of_rows):
    for j in range(seats_per_row):
        if seats[i][j] == "X":
            taken = taken + 1
print("Seats taken:", taken)