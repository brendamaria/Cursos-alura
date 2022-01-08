from datetime import datetime, timedelta


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
        dia_semana_lista = ["Segunda","Terça","Quarta","Quinta","Sexta","Sabado","Domingo"]
        dia_cadastro = self.momento_cadastro.weekday()
        return dia_semana_lista[dia_cadastro]

    def data_formatada(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%y %H:%M")
        return data_formatada

    def tempo_cadastro(self):
        agora = datetime.today() + timedelta(days=15, minutes=20,seconds=30) #teste
        return agora - self.momento_cadastro
