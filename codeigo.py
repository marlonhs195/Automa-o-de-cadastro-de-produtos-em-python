import pyautogui as gui
import pandas as pd
import time

############# caminho do csv ###########
## D:\Projeto\hastag\code_aula01\produtos.csv
########################################

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

gui.PAUSE = 0.5

gui.press("win")
gui.write("chrome")
gui.press("enter")
time.sleep(1)
gui.click(x=785, y=607)
time.sleep(0.5)
gui.hotkey("ctrl", "t")
time.sleep(0.5)
gui.write(link)
time.sleep(1)
gui.press("enter")
gui.sleep(2)
gui.click(x=729, y=377)
gui.write("automaçãoemteste@euconsigo.com")
gui.press("tab")
gui.write("sim vc consegue!")
gui.press("tab")
gui.press("enter")
############### LOGADO COM SUCESSO ###################
gui.sleep(2)
tabela = pd.read_csv("D:\Projeto\hastag\code_aula01\produtos.csv")

for linha in tabela.index:
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    categoria = str(tabela.loc[linha, "categoria"])
    codigo = str(tabela.loc[linha, "codigo"])
    custo = str(tabela.loc[linha, "custo"])
    marca = str(tabela.loc[linha, "marca"])
    tipo = str(tabela.loc[linha, "tipo"])
    obs = str(tabela.loc[linha, "obs"])

    gui.click(x=730, y=261)
    gui.write(codigo)
    gui.press("tab")
    gui.write(marca)
    gui.press("tab")
    gui.write(tipo)
    gui.press("tab")
    gui.write(categoria)
    gui.press("tab")
    gui.write(preco_unitario)
    gui.press("tab")
    gui.write(custo)
    gui.press("tab")
    if obs != "nan":
        gui.write(obs)
    gui.press("tab")
    gui.press("enter")
