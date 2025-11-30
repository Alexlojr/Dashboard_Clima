class Dados:
    def __init__(self, dados_json):
        # Clima
        self.condicao = dados_json["weather"][0]["main"]
        self.descricao = dados_json["weather"][0]["description"]

        # Coordenadas
        self.latitude = dados_json["coord"]["lat"]
        self.longitude = dados_json["coord"]["lon"]

        temperatura_kelvin = dados_json["main"]["temp"]
        self.temperatura = round(temperatura_kelvin - 273.15)

        self.umidade = dados_json["main"]["humidity"]




