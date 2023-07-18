from pymongo.mongo_client import MongoClient

class Quartos:
    def __init__(self, teste = False):
        self.clientedb = MongoClient("mongodb://localhost:27017")
        self.gerenciador = self.clientedb["gerenciador"]
        self.quartos = self.gerenciador["quartos"]
        if teste:
            self.quartos.insert_many([
                {
                    "numero_quarto": 1,
                    "tamanho_quarto": 5,
                    "diaria_preco": 700.00
                },
                {
                    "numero_quarto": 2,
                    "tamanho_quarto": 3,
                    "diaria_preco": 1200.00
                },
                {
                    "numero_quarto": 3,
                    "tamanho_quarto": 4,
                    "diaria_preco": 2100.00
                }
            ])

    def AdicionarQuarto(self, numero_quarto:int, tamanho_quarto:float, diaria_preco:float):
        quarto = {"numero_quarto": numero_quarto, "tamanho_quarto": tamanho_quarto, "diaria_preco": diaria_preco}
        if list(self.quartos.find()):
            if quarto["numero_quarto"] in [quarto["numero_quarto"] for quarto in list(self.quartos.find())]:
                return "Quarto já existe!"
            else:
                self.quartos.insert_one(quarto)
                return "Quarto adicionado!"
        else:
            self.quartos.insert_one(quarto)
            return "Quarto adicionado!"
    
    def RemoverQuarto(self, numero_quarto:int):
        if self.quartos.find():
            if numero_quarto in [quarto["numero_quarto"] for quarto in list(self.quartos.find())]:
                self.quartos.delete_one({"numero_quarto": numero_quarto})
                return "Quarto removido com sucesso!"
            else:
                return "Quarto não existe!"
        else:
            return "Nenhum quarto existente!"
    
    def VerQuartos(self):
        return list(self.quartos.find())

if __name__ == "__main__":
    quartos = Quartos()
    print(quartos.AdicionarQuarto(1, 8, 2500))
    print(quartos.AdicionarQuarto(1, 6, 2000))
    print(quartos.AdicionarQuarto(2, 10, 3000))
    print(quartos.RemoverQuarto(2))
    print(quartos.VerQuartos())
    print(quartos.RemoverQuarto(1))