masdate = []
with open("Кинотеатр.txt", "r", encoding="utf-8") as F3:
    line = F3.readline().strip()
    maxAudience = 0
    bestFilm = "0"
    ind = 0
    while line:
        parts = line.split()
        if len(parts) == 4:
            filmName = parts[0]
            date = parts[1]
            price = int(parts[2])
            Audience = int(parts[3])
            if maxAudience < Audience:
                maxAudience = Audience
                bestFilm = filmName
            if date not in masdate:
                masdate.append(date)
        line = F3.readline().strip()
    print(f"Самый посещаемый фильм: {bestFilm}")
while 1:
    ind = 0
    print("\t Доступные даты:")
    print(masdate)
    vvod = input("Введите интересующую дату которые представлены на экране: ")
    with open("Кинотеатр.txt", "r", encoding="utf-8") as F3:
        line2 = F3.readline().strip()
        while line2:
            parts = line2.split()
            filmName = parts[0]
            date = parts[1]
            if date == vvod:
                ind = 1
                print(f"Фильм за дату: {date}: {filmName}")
            line2 = F3.readline().strip()
    if ind == 1:
        break
