try:
    n = float(input("Introduce un número: "))
    5/n
except TypeError:
    print("No se puede dividir el número por una cadena")
except ValueError:
    print("Debes introducir un número")
except ZeroDivisionError:
    print("Debes introducir un número distinto a 0")
except Exception as e:
    print(type(e).__name__)