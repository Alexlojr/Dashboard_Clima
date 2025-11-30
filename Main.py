import requests
import tkinter as tk
from Classes_Functions import *

def botaopesquisar():

    # ==== buscar cordenadas ====

    cidadenome= barradebusca.get()

    urlgeo = (
        f"https://api.openweathermap.org/geo/1.0/direct?"
        f"q={cidadenome}&limit=1&appid=19e5b3f3a7ba81f1e8734ada48104bcc"
    )

    respostageo = requests.get(urlgeo)
    cidade = respostageo.json()

    if len(cidade) == 0:
        print("Cidade não encontrada")
        return

    lat = cidade[0]["lat"]
    lon = cidade[0]["lon"]

    # ==== buscar clima ====

    url_clima = (
        f"https://api.openweathermap.org/data/2.5/weather?"
        f"lat={lat}&lon={lon}&appid=19e5b3f3a7ba81f1e8734ada48104bcc"
    )

    resposta = requests.get(url_clima)
    dados = Dados(resposta.json())

    # ==== exibir ====

    condicaoresquestlabel = tk.Label(root, text=dados.condicao, font=("Arial", 11), bg='#17517E', fg='#FFFFFF')
    condicaoresquestlabel.place(x=200, y=200)

    descricaoresquestlabel = tk.Label(root, text=dados.descricao, font=("Arial", 11), bg='#17517E', fg='#FFFFFF')
    descricaoresquestlabel.place(x=225, y=230)

    temperaturarequestlabel = tk.Label(root, text=f"{dados.temperatura}°C", font=("Arial", 11), bg='#17517E', fg='#FFFFFF')
    temperaturarequestlabel.place(x=250, y=260)


    umidaderequestlabel = tk.Label(root, text=f"{dados.umidade}%", font=("Arial", 11), bg='#17517E', fg='#FFFFFF')
    umidaderequestlabel.place(x=225, y=290)


# ========= Instanciar Janela =========
root = tk.Tk()
root.geometry('1400x700')
root.title('DashBoard Clima')
root.resizable(False, False)
root.configure(bg='#17517E')



# ===== Entry =====
barradebusca = tk.Entry(root, width=50, bd=0, font=('arial',15))
barradebusca.place(x=120, y=50)


# ===== Botão =====
botaopesquisar = tk.Button(root, text='Buscar',command=botaopesquisar,bd=0)
botaopesquisar.place(x=70, y=50)


# ===== Labels =====
textobarradebuscalabel = tk.Label(root,text='Insira o nome da Cidade que deseja buscar',font=("Arial", 11), bg='#17517E', fg='#FFFFFF')
textobarradebuscalabel.place(x=120, y=25)

Condicaolabel = tk.Label(root,text="Clima Atual: ",font=("Arial", 11),bg='#17517E', fg='#FFFFFF')
Condicaolabel.place(x=120, y=200)

descricaolabel = tk.Label(root,text="Condição Atual: ",font=("Arial", 11),bg='#17517E', fg='#FFFFFF')
descricaolabel.place(x=120, y=230)

temperaturalabel = tk.Label(root,text="Temperatura Atual: ",font=("Arial", 11),bg='#17517E', fg='#FFFFFF')
temperaturalabel.place(x=120, y=260)

umidadelabel = tk.Label(root,text="Umidade Atual: ",font=("Arial", 11),bg='#17517E', fg='#FFFFFF')
umidadelabel.place(x=120, y=290)


root.mainloop()
