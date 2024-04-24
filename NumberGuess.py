guess=-1
geheim=77

print("Errate die Geheimzahl")
while guess != geheim:
    temp=input("Deine Versuch: ")
    if temp.isnumeric():
        guess=int(temp)
        if guess>geheim:
            print("Die gesuchte Zahl ist kleiner")
        if guess<geheim:
            print("Die gesuchte Zahl ist größer")
    else:
        print("Das war keine Zahl")
    
print("GG")
input("Done")

