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
    apellido = ""

    def __init__(self, local_name, local_apellido):         #La manera de crear un constructor en una clase
        self.nombre = local_name
        self.apellido = local_apellido

    def geeting(self):
        return "Hola mi nombre es {} {}".format(self.nombre, self.apellido)

    def __str__(self):                      #Es para mandar un mensaje en vez de un error 
       return "{} {}".format(self.nombre, self.apellido)

    def __eq__(self, otro_inombramble):
        return self.nombre == otro_inombramble.nombre and self.apellido == otro_inombramble.apellido

print("Esto es una cadena")
#print(__name__)
if  __name__ == "__main__":
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
    leo = Inombrambles("Leo", "Gonzalez")
    leo2 = Inombrambles("Leo", "Lopez")
    #leo2 = leo
    #leo.nombre = "leo"
    #leo.nombre = "leo"
    jonathan = Inombrambles("jonathan", "Duran")
    norma = Inombrambles("norma", "Mendoza")
    print(leo.geeting())
    print(jonathan.geeting())
    print(norma.geeting())
    print(leo)
    print(jonathan)
    print(norma)
    print("Los 2 leos son iguales {}".format(leo == leo2))
    #print(leo.cosa)
    print("Esta cadena esta dentro del if")