from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome:str):
        self.nome= nome
    
    def apresentar_nome(self):
        print (f"Eu sou um(a) {self.nome}!")
    
    @abstractmethod
    def fazer_som(self):
        pass
    
    def mover(self):
        pass
    
class Leao(Animal):
    def __init__(self, nome):
        super().__init__(nome)
    
    def fazer_som(self):
        print(f"AAAAAAAAAAR")
    def mover(self):
        print(f"correndo")

class Cobra(Animal):
    def __init__(self, nome):
        super().__init__(nome)
    
    def fazer_som(self):
        print(f"sssssssssss")
    def mover(self):
        print("rastejando")

class Elefante(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def fazer_som(self):
        print(f"Duum-duum, Duum-duum")
    def mover(self):
        print("correndo")

def apresentar(animal:Animal):
    animal.apresentar_nome()
    animal.fazer_som()
    animal.mover()
    print(f"tipo:" ,type(animal).__name__ )

print("=== teste 01 ===")
leao=Leao("Simba")
apresentar(leao)

print("=== teste 02 ===")
cobra=Cobra("sucuri")
apresentar(cobra)

print("=== teste 03 ===")
elefante=Elefante("Dumbo")
apresentar(elefante)