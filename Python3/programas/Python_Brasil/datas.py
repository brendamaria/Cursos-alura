from datetime import datetime

class Datas:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.data_formatada()

    def mes_cadastro(self):
        mes_do_ano = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
        mes_cadastro = self.momento_cadastro.month -1
        return mes_do_ano[mes_cadastro]

    def dia_semana(self):
        dia_semana_lista = ["Segunda","Terça","Quarta","Quinta","Sexta"]
        dia_cadastro = self.momento_cadastro.weekday()
        return dia_semana_lista[dia_cadastro]

    def data_formatada(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%y %H:%M")
        return data_formatada