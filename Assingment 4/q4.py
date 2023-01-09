
for c in range(200):
    if (c % 5 != 2):
        continue
    if (c % 6 != 3):
        continue
    if (c % 7 != 2):
        continue

    print(str(c) + " is the answer!")
    break