from pymongo.mongo_client import MongoClient
from datetime import date, timedelta
from time import sleep
import threading

class Reservas:
    def __init__(self):
        self.clientedb = MongoClient("mongodb://localhost:27017")
        self.gerenciador = self.clientedb["gerenciador"]
        self.reservas = self.gerenciador["reservas"]
        verificador = threading.Thread(target=self.Verificador)


    def ReservarQuarto(self, numero_quarto:int, dias:int):
        if self.reservas.find_one({"numero_quarto": numero_quarto}):
            return "Quarto já reservado!"
        else:
            data_reserva = date.today()
            data_vencimento = data_reserva + timedelta(dias)
            reserva = {"numero_quarto": numero_quarto, "dias": dias, "data_reserva": {"dia": data_reserva.day, "mes": data_reserva.month, "ano": data_reserva.year},"data_vencimento": {"dia": data_vencimento.day, "mes": data_vencimento.month, "ano": data_vencimento.year}}
            self.reservas.insert_one(reserva)
    
    def VerReservas(self):
        return self.reservas.find()

    def Verificador(self):
        while True:
            data_atual = date.today()
            for reserva in self.reservas.find():
                if reserva["data_vencimento"]["dia"] <= data_atual.day and reserva["data_vencimento"] <= data_atual.month and reserva["data_vencimento"] <= data_atual.year:
                    self.reservas.delete_one({"numero_quarto": reserva["numero_quarto"]})
            sleep(86400)
    
