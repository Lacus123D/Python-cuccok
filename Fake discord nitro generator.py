import random
import time

szamok2 = []
url = "https://discord.gift/"




kérdés = int(input("Hány számjegyű legyen a discord nitro?: "))

time.sleep(5)

print("Discord nitrod készül...")


érték = int(kérdés)

if érték >= 3:

    for x in range(érték):
        szamok = random.randint(0, 9)
        szam = str(szamok)
        szamok2.append(szam)
    szamok3 = "".join(szamok2)
    nitro_url = url + szamok3
    time.sleep(5)

    print("Nitrod hamarosan kész lesz!")

    time.sleep(2)
    print(f"A nitrod kész | Nitro linkje: {nitro_url}")
else:
    print("Nem jó mert a nitro hossza nem lehet kisebb mint három!")










