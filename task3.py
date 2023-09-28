Dictionary = {}
with open("task3.txt", "r", encoding="utf-8") as F4:
    key = "0"
    line = F4.readline().strip()
    while line:
        value = 0
        parts = line.split()
        key = parts[0]
        for chislo in parts[1:]:
            value += int(chislo)
        Dictionary[key] = value
        line = F4.readline().strip()
print(f"Словарь: {Dictionary}")