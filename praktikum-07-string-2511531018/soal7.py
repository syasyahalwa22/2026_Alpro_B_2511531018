# Name: Syasya Halwa Gazwani
# NIM: 2511531018

name = "syasya halwa gazwani"
nim = "2511531018"

clean = name.strip()
space = clean.find(" ")

if space == -1:
    first_name = clean
else:
    first_name = clean[:space]

username = first_name.lower() + nim[-3:]

print("=" * 30)
print(f"{'STUDENT CARD' :^30}")
print("=" * 30)
print(f"{'Name' :<10}: {name.title()}")
print(f"{'NIM' :<10}: {nim}")
print(f"{'Username' :<10}: {username}")
print(f"{'Intake' :<10}: 20{nim[:2]}")
print("=" * 30)