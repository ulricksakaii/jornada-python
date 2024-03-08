
import pyautogui #automação de tarefas python
import time #temporizador para parar o programa
import pandas #leitura de base de dados


# Passo a Passo do projeto
# Passo 1: Entrar no sistema da empresa
  #https://dlp.hashtagtreinamentos.com/python/intensivao/login

pyautogui.PAUSE =0.5

pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")
time.sleep(1)
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# Passo 2: Fazer login

pyautogui.press("f11")

time.sleep(3)
email = "ulrick.bh@gmail.com"
senha = "UlrickSakai123"
pyautogui.click(x=405, y=287)
pyautogui.write(email)


pyautogui.click(x=419, y=385)
pyautogui.write(senha)
pyautogui.press("enter")

# Passo 3: Importar a base de dados
time.sleep(3)
tabela = pandas.read_csv("produtos.csv")


for linha in tabela.index: 
  # Passo 4: Cadastrar 1 produto
  pyautogui.click(x=401, y=174)
  #
  # código do produto
  pyautogui.write(tabela.loc[linha,"codigo"])
  pyautogui.press("tab")
  
  # marca do produto
  pyautogui.write(tabela.loc[linha,"marca"])
  pyautogui.press("tab")
 
  # tipo do produto
  pyautogui.write(tabela.loc[linha,"tipo"])
  pyautogui.press("tab")
 
  # categoria do produto
  pyautogui.write(str(tabela.loc[linha,"categoria"]))
  pyautogui.press("tab")
 
  # Preço do produto
  pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
  pyautogui.press("tab")
 
  # Custo do produto
  pyautogui.write(str(tabela.loc[linha,"custo"]))
  pyautogui.press("tab")
  obs = tabela.loc[linha, "obs"]
  if not pandas.isna(obs):
  # Observação do produto
    pyautogui.write(obs)
    # Concluir o cadastro do produto
    pyautogui.press("tab")
    pyautogui.press("enter")
  else : 
    pyautogui.press("tab")
    pyautogui.press("enter")
 
  pyautogui.scroll(5000)

# Passo 5: Repetir o processo de cadastro até acabar

#pyautogui.click -> clicar em algum lugar da tela
#pyautogui.write -> escrever um texto 
#pyautogui.press -> pressionar 1 tecla do teclado
#pyautogui.hotkey("alt", "shift") -> combinação de teclas
