class Polystation:
    nombre1 = "Erick Fernando Siqueiros Zúñiga"
    nombre2 = "Paulina Ixchel Arreguin Ruiz"
    nombre3 = ""

class WebHeros:
    nombre1 = "Jesus Manuel Arellano Merendon "
    nombre2 = "Axel Felipe Reyes Valadez"
    nombre3 = "Luis Daniel Delgado Enriquez"

class Los_3_Mosqueteros:
    nombre1 = "Dania Denisse Benavides Figueroa"
    nombre2 = "Erick Lozano Duarte"
    nombre3 = "Ana Cristina Valenzuela Ruiz"

class PinguinosGalacticos:
    nombre1 = "Yahir Antonio Monje Ochoa"
    nombre2 = "Yesica Cristina Rodriguez Renteria"
    nombre3 = ""

class ToyotaLegacy:
    nombre1 = "Israel Chacon Rojo"
    nombre2 = "Dilan Mauricio Garcia Hernandez"
    nombre3 = "Jesus Elias Sierra Ruiz"

class UwU:
    nombre1 = "Leonardo Alberto Gonzáles Carmona"
    nombre2 = "Norma Graciela Mendoza Ruiz"
    nombre3 = "Jonathan Durán Mendoza"


class FS3:
    equipos = [
        Polystation(),
        WebHeros(),
        Los_3_Mosqueteros(),
        PinguinosGalacticos(),
        ToyotaLegacy(),
        UwU()
    ]

    def __str__(self):
        resultado = ""
        for equipo in self.equipos:
           # el type.__main__ regresa el nombre de la clase, para ahorrarme en escribir otro atributo de los nombres de cada equipo :))))))
            resultado += "\n Equipo: {}\n Integrantes: \n- {}\n- {}\n- {}".format(type(equipo).__name__, equipo.nombre1, equipo.nombre2,equipo.nombre3) +"\n---------------------------------------------------\n"
        return resultado

if __name__ == "__main__":
    print(FS3())