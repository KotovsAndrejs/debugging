
# Mērķis: 
# iespēja konvertēt USD uz EUR un otrādi pēc 1.08 kursa

eur_to_usd_rate = 1.08

print("Choose command")
while True:
    print("=======")
    print("1 - convert USD into EUR")
    print("2 - convert EUR into USD")
    print("3 - exit")
    command = input("")
    if command == "1":
        usd = float(input("Enter USD:"))
        eur = usd / eur_to_usd_rate
        print(usd, "USD equals EUR", eur)
    elif command == "2":
        eur = float(input("Enter EUR:"))
        usd = eur * eur_to_usd_rate
        print(eur, "EUR equals USD", usd)
    else:
        break

# Kādas kļūdas izdevies atrast?
# samainīt kursu
# samainīt 1.08 ar mainīgo eur_to_usd_rate
# 2 komandā samainīt mainīgo nosaukumus (usd to eur, eur to usd)
#


