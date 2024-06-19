def funcname():
    print("Hello World")

# Function mit Parametern und einem Standardwert für Variable3
def OutputTest(variable1, variable2, variable3="!"):
    print(variable1, variable2, variable3)

def standardString():
    return "Hello World"

# Keyword Parameter
OutputTest(variable2= " hi ", variable1="welt")

# Positionelle Parameter
OutputTest(" hi ", "welt")

# Kombination Parameter
OutputTest(" hi ",  variable3="?", variable2 ="welt" )


s = standardString()
r = funcname()
#print(s, r)




def listenTest(parameterliste):
    parameterliste[0] = 0

localeListe = [1,2,3,4,5]

print(localeListe)
listenTest(localeListe)
print(localeListe)



def test2():
    var1 = 5
    






input("Done")