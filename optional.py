try: 
    try:
        var1 = "hello World"
        float(var1)
        prin("Hello World")
        v = int(input())
        x = 5 / v
        print(x)
        liste = []
        liste["4"]
    except ValueError:
        print("Was machst du?")
    except ZeroDivisionError:
        print("Sie können nicht durch 0 teilen!")
    except IndexError:
        print("Listen fehler")
    except TypeError:
        print("Warum?")
    except SyntaxError:
        print("prin gibt es nicht?")
    except AttributeError:
        print("prin gibt es immernoch nicht?")
    except Exception as error:
        print(type(error))
    except:
        print("Something")

    var2 = "2"
    varbool = type(var2) is int
    print(varbool)
    x=5
    y=3

    #y= not y    

    #if x and y:
        #print("Beide wahr")
    #elif x or y:
        #print("Mindenstens eines ist wahr")
    
    if x | y:
        print(x | y)
    if x or y:
        print("Fall 2")
    


except:
    print("Fehler im Code")

input("Done")