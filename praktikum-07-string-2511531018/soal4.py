# Name: Syasya Halwa Gazwani
# NIM: 2511531018

phone = "081234567890"
masked = phone[:4] + "*" * (len(phone) - 7) + phone[-3:]
print(masked)

phone = "08123456789"
masked = phone[:4] + "*" * (len(phone) - 7) + phone[-3:]
print(masked)

phone = "0812345678"
masked = phone[:4] + "*" * (len(phone) - 7) + phone[-3:]
print(masked)

phone = "082511531018"
masked = phone[:4] + "*" * (len(phone) - 7) + phone[-3:]
print(masked)