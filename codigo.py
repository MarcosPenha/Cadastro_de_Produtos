# Passo a passo do projeto

# 1. Abrir o sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

# para instalar o pyautogui (SERVE PARA AUTOMATIZAR ALGUMA COISA): pip install pyautogui - "NO TERMINAL - CLICAR NA SETA - COMMAND PROMPT"

import pyautogui
import time

#pyautogui.PAUSE - Serve para dar um pause entre dois comandos
pyautogui.PAUSE = 0.5

#pyautogui.click - serve para clicar alguma coisa EX. MOUSE
#pyautogui.write - serve para escrever alguma coisa EX. TEXTO
#pyautogui.press - serve para precionar alguma coisa EX. TECLADO - BOTÂO
#pyautogui.hotkey - serve para apertar um conjunto de teclar EX. Ctrl C, Ctrl V

# Abrir o navegador (Chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Entrar no site do sistema
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# aqui pode ser que ele demora alguns seguntos para carregar o site
# esse comando serve para esperar o site carregar inteiro. (PONTUAL)
time.sleep(3)

# 2. Fazer o login
pyautogui.click(x=2846, y=506)
pyautogui.write("penha173@gmail.com")

pyautogui.press("tab") # passou para o campo de senha
pyautogui.write("246810") # colocar senha aqui

pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)

# 3. Abrir/importar a base de produtos para cadastrar
# pip install pandas numpy openpyxl - "NO TERMINAL - CLICAR NA SETA - COMMAND PROMPT"
import pandas as pd

# tabela = VARIÁVEL
tabela = pd.read_csv("produtos.csv")

# 4. Cadastrar um produto
# str = string = texo

for linha in tabela.index:

    codigo = str(tabela.loc[linha, "codigo"])
    # clicar no campo do código do produto
    pyautogui.click(x=2859, y=366)

    # preencher o campo do produto
    pyautogui.write(codigo)
    # passa para o próximo campo
    pyautogui.press("tab")

    # preencher a marca do produto
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    # passa para o próximo campo
    pyautogui.press("tab")

    # preencher o tipo do produto
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    # passa para o próximo campo
    pyautogui.press("tab")

    # preencher a categoria do produto
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    # passa para o próximo campo
    pyautogui.press("tab")

    # preencher o preço unitário do produto
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    # passa para o próximo campo
    pyautogui.press("tab")

    # preencher o custo do produto
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    # passa para o próximo campo
    pyautogui.press("tab")

    # preencher a observação preço do produto
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    # passa para o próximo campo
    pyautogui.press("tab")

    # aperta o botão
    pyautogui.press("enter")
    
    
# 5. Repetir isso tudo até acabar a lista de produtos
    pyautogui.scroll(5000)