text = "python"
i = 0

while i < len(text):
    if text[i] == "h":
        i += 1
        continue
    print(text[i])
    i += 1
