import random


cosa = 1


def name_string():
    return "El nombre del archivo structure es:  {}".format(__name__)


def concat_suma(val1, val2):
    cosa = 5
    result = "{} + {} = {}".format(value, value2, value+value2)
    return result

class Inombrambles:
    nombre = ""

    def _init_(self, local_name):         #La manera de crear un constructor en una clase
        self.nombre = local_name

    def geeting(self):
        return "Hola mi nombre es {}".format(self.nombre)

    def _str_(self):                      #Es para mandar un mensaje en vez de un error 
        return self.nombre

    def _eq_(self, otro_inombramble):
        return self.nombre == otro_inombramble.nombre

print("Esto es una cadena")
#print(_name_)
if  __name__ == "_main_":
    value = 5
    value2 = 10
    #print("El valor es: ", value)
    #strConcact = "El primer valor es {} y el segundo valor es {}"
    strConcact = "{} + {} = {}"
    #strConcact = strConcact.format(value, value2, value+value2)
    #cosa = 3
    #cosa = concat_suma(5,10)
    #print(cosa)
    #print(concat_suma(5, 10))
    if random.random() > 0.5:
        value_inside_if = 10
    #print(value_inside_if)
    leo = Inombrambles("Leo")
    leo2 = Inombrambles("Leo")
    #leo2 = leo
    #leo.nombre = "leo"
    leo.nombre = "Leo"
    jonathan = Inombrambles("jonathan")
    norma = Inombrambles("norma")
    print(leo.geeting())
    print(jonathan.geeting())
    print(norma.geeting())
    print(leo)
    print(jonathan)
    print(norma)
    print("Los 2 leos son iguales {}".format(leo == leo2))
    #print(leo.cosa)
    print("Esta cadena esta dentro del if")