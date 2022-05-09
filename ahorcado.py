import random

class Ahorcado:
    def __init__(self):
        
        palabras = "hamburguesa pizza camioneta motocicleta supermercado caballo perro televisor computadora laptop cumpleaños fiesta pasapalos cerveza colchon".split()
        self.palabra = palabras[random.randint(0, len(palabras)-1)]
        self.palabra_= "_" * len(self.palabra)
        self.palabra=list(self.palabra)
        self.palabra_=list(self.palabra_)
        self.vidas=6 #El dibujo del ahorcado son 5 palitos y el redondito de la cabeza
        
    def intento(self,letra):
        acierto=0
        for i,c in enumerate(self.palabra):
            if c==letra:
                self.palabra_[i]=letra
                acierto=1
        if acierto==0:
            self.vidas-=1

        if self.vidas==0:
            print("Perdiste")
            return -1
        if "_" not in self.palabra_:
            print("Ganaste")
            print(self.palabra_)
            return -1
        
        return "".join(self.palabra_)

    def jugar(self):
        while True:
            letra=input("Ingrese letra: ")
            res= self.intento(letra)

            if(res==-1):
                break
            print(res)
    




new=Ahorcado()
new.jugar()
# while True:
#     intento=input("Ingrese letra: ")
#     new.intento(intento)
#     if intento=='xxx':
#         break

# print(palabra_)
# print(palabra)








# '''

#    +---+
#    |   |
#        |
#        |
#        |
#        |

# ========='''