eingabe = float(input("Gib eine Minutenzahl an: "))
h=int(eingabe//60)
m=int(eingabe%60)
s=int((eingabe%1)*60)
print(h, "h ", m, "m ", s, "s ", sep="")

input("Done")