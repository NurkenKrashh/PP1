text = "nurken"
i = 0

while i < len(text):
    if text[i] == 'r':
        i += 1
        continue
    print(text[i])
    i += 1

