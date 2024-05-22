# Es gibt viele Arten von Collections
empty_liste = []
empty_tuple = ()
empty_dictionary = {}

# Tuple sind dabei immutable & sequential
on_element_tuple = (1,)
tuple1 = ( 1, 2, 3 , 5, 8)
tuple2 = 1 , 2 ,3 ,5 , 8
crazy_tuple = (1, 5 , "String", True, 6.5 )

# Wir können innerhalb dieser Elemente selektieren 
# oder sie mit einem Slice bearbeiten
var = tuple1[2]
var = tuple1[1:]
# Das geht jedoch nicht! tuple1[0] = 5

# Wir können tuple addieren um neue Tuppel zu erzeugen
# Wir können auch tuple multiplizieren
t1 = tuple1 + (13,21)
t2 = tuple1 * 3

# Besonders spannend ist wie wir mit tuple Werte tauschen können
t1, t2 = t2 , t1
print(t2)

# tuple sind iterierbar
for t in tuple1:
    print(t)

# Wir können zwar nicht einen einzeln Wert ändern, 
# aber wir können einen neuen Tupel anlegen
possible_tuple = tuple1[:2] + (4,) + tuple1[3:]

# Dictionaries sind dabei mutable & nicht sequential
dictionary1 = { "Hund" : "dog" , 
                "Katze": "cat", 
                "Huhn" : "Chicken" }

# Wir können Werte hinzufügen, löschen, ausgeben und ändern über den Key
var = dictionary1["Hund"]
dictionary1["Katze"] = "kitten"
dictionary1["Maus"] = "mice" 
del dictionary1["Huhn"]
print(dictionary1)

# Wir können nicht direkt durch ein dictionary durch iterieren
# jedoch können wir uns "listen" dazu ausgben lassen
collection = dictionary1.keys()
collection = dictionary1.items()
collection = dictionary1.values()
for something  in collection:
    print(something)

# Ohne Slice brauchen wir eine andere Methode zum kopieren
dictionary2 = dictionary1.copy() 

# Folgendes funktioniert in jedem dieser drei Datentypen
7 in tuple1 # False
len(tuple1) # 5
len(dictionary1) # 3
"Katze" in dictionary1 # True

input("Done")