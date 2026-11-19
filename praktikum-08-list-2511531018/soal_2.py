playlist = ["Lagu A", "Lagu B", "Lagu C", "Lagu D"]
playlist.append("Lagu E")
playlist.insert(1, "Lagu F")
played = playlist.pop(0)
playlist.remove("Lagu C")
print(playlist)
print(played)



notifications = ["chat", "promo", "promo", "email"]
for item in notifications:
    if item == "promo":
        notifications.remove(item)
print(notifications)



notes = ["intro", "list", "tuple"]
shared = notes
my_copy = notes.copy()
shared[0] = "INTRO"
my_copy[1] = "LIST"
notes = ["new"]
print(notes)
print(shared)
print(my_copy)
print(shared == my_copy, shared is my_copy)
