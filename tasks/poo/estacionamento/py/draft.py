from abc import ABC, abstractmethod
class Veiculo(ABC):
    def __init__(self, id: str, tipo: str, entrada: int):
        self.id = id
        self.tipo = tipo
        self.entrada = entrada
    def setEntrada(self, horaEntrada: int):
        self.entrada = horaEntrada
    @abstractmethod
    def calcularValor(self, horaSaida: int):
        pass
    def __str__(self):
        tip = self.tipo.rjust(10, "_")
        idt = self.id.rjust(10, "_")
        return f"{tip} : {idt} : {self.entrada}"
class Estacionamento:
    def __init__(self, horaAtual: int):
        self.horaAtual = horaAtual
        self.veiculos: list[Veiculo] = []
    def estacionar(self, tipo: str, id: str):
        if tipo == "bike":
            v = Bike(id, self.horaAtual)
        if tipo == "moto":
            v = Moto(id, self.horaAtual)
        if tipo =="carro":
            v= Carro(id,self.horaAtual)
        self.veiculos.append(v)
    def passarTempo(self, tempo: int):
        self.horaAtual += tempo
    def __str__(self):
        out = ""
        for i in self.veiculos:
            out += str(i) + "\n"
        out += f"Hora atual: {self.horaAtual}"
        return out
    def pagar(self,id:str):
        for i  in range (len(self.veiculos)):
            v=self.veiculos[i]
            if v.id==id:
                valor=v.calcularValor(self.horaAtual)
                print (f"{v.tipo} chegou {v.entrada} saiu {self.horaAtual}. Pagar R$ {valor:.2f}")
                self.veiculos.pop(i)
                return
            
class Bike(Veiculo):
    def __init__(self, id: str, entrada: int):
        super().__init__(id, "Bike", entrada)
    def calcularValor(self, horaSaida: int):
        return 3
class Moto(Veiculo):
    def __init__(self, id: str, entrada: int):
        super().__init__(id, "Moto", entrada)
    def calcularValor(self, horaSaida: int):
        minutos = horaSaida - self.entrada
        return minutos / 20

class Carro(Veiculo):
    def __init__(self,id:str, entrada:int):
        super().__init__(id,"Carro",entrada)
    def calcularValor(self, horaSaida:int):
        minutos = horaSaida-self.entrada
        return max(5,minutos/10)
    
def main():
    estacion = Estacionamento(0)
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(estacion)
        elif args[0] == "tempo":
            time = int(args[1])
            estacion.passarTempo(time)
        elif args[0] == "estacionar":
            tip = args[1]
            idt = args[2]
            estacion.estacionar(tip, idt)
        elif args[0] =="pagar":
            estacion.pagar(args[1])
main()