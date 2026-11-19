menus = ["Nasi Goreng", "Mie Ayam", "Soto"]
number_of_days = 3
sales = []

for i in range(number_of_days):
    row = []
    for j in range(len(menus)):
        amount = int(input(f"Day {i + 1}, {menus[j]}: "))
        row.append(amount)
    sales.append(row)
print("Total per day:")

for i in range(number_of_days):
    daily_total = 0
    for j in range(len(menus)):
        daily_total = daily_total + sales[i][j]
    print(f"Day {i + 1}: {daily_total}")
menu_totals = []

for j in range(len(menus)):
    menu_total = 0
    for i in range(number_of_days):
        menu_total = menu_total + sales[i][j]
    menu_totals.append((menus[j], menu_total))
print("Total per menu:", menu_totals)
best_name = menu_totals[0][0]
best_total = menu_totals[0][1]

for name, total in menu_totals:
    if total > best_total:
        best_name = name
        best_total = total
print(f"Best seller: {best_name} ({best_total})")