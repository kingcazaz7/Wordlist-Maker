import random

words = ["Somalia", "Somaali", "Muqdisho", "Hargeisa",
         "Mogadishu", "Baraawaaqo", "Geel", "Daljir",
         "Nabad", "Horumar", "Aqoon", "Wadan",
         "Xidig", "Hodan", "Ayaan", "Sahal",
         "Ifiye", "Guuleed", "Liban", "maxamed",
         "hamza", "ahmed", "cabdirahman", "abdirahman",
         "deeqo", "hodan", "luul", "nimco", "Warsame",
         "HOOYO.MACAN", "hooyomacaan"]

numbers = ["123", "2026", "1234", "2025", "2027", "1"]
symbols = ["!", "@", "#", "_"]

with open("somali_wordlist.txt", "w") as file:
    for i in range(10000):
        word =   random.choice(words)
        number = random.choice(numbers)
        symbol = random.choice(symbols)

        password = word + number + symbol
        file.write(password + "\n")

        if (i + 1) % 10000 == 0:
            print(f"{i + 1} passwords generated")

print("Done!")