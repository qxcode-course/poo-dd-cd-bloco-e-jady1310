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
    
def apresentar(animal:Animal):
    animal.apresentar_nome()
    animal.fazer_som()
    animal.mover()
    print(f"tipo:" ,type(animal).__name__ )

    