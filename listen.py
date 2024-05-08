liste = [1,4,5,9,6] 
del liste[2]
x = liste[-1]
#len(liste)
#print(x)

liste.append(3)
liste.insert(3, 8)
#print(liste)

#for c in liste:
    #print(c)

mix = [12, 15.4, "Brot", False, print, [1, 2, 3 ] ]

print(liste)


# Listen sind bei Reference und nicht bei Value übergeben
liste1 = [1,2,99, 61,6,7,8]
liste2 = liste1
liste2 = liste1[:]
liste1[0] = 9
print(liste2[0])

# Um eine die Werte einer Liste zu kopieren benutzen wir den Slice
liste3 = liste1[:]
print(liste3)

# Beim for Loop definieren die Range wie folge range(start, end, step)
# Dasselbe gilt auch für den slice
start=0
end=len(liste1)
step=1

for i in range(start, end, step):
    v = liste1[i]

liste4 = liste[start,end, step]

# Mit dem Keyword in können wir überprüfen ob ein Element in einer Liste ist
b = 5 not in liste2
print(b)


l = liste1[5:3:1]
print(y)

input("Done")