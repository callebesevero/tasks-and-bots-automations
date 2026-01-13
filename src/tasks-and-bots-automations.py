from pyautogui import hotkey, scroll, click, press, write, PAUSE
from pandas import read_csv
from time import sleep

site = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
email = 'jou@gmail.com'
senha = 'senha'

PAUSE = 1.2

# Abrir site
press('win')

sleep(1)

write('brave web browser')

sleep(0.1)

press('enter')

sleep(2)

hotkey('ctrl', 'l')
write(site)
press('enter')

sleep(1)

# Login
press('tab')
write(email)
press('tab')
write(senha)
press('enter')


# Pegar dados do .csv
table = read_csv('src/produtos.csv')

sleep(2)

# Inserir dados
for line in table.index:
    click(x=521, y=245)

    code = str(table.loc[line, 'codigo'])
    write(code)
    press('tab')

    brand = str(table.loc[line, 'marca'])
    write(brand)
    press('tab')

    ptype = str(table.loc[line, 'tipo'])
    write(ptype)
    press('tab')

    category = str(table.loc[line, 'categoria'])
    write(category)
    press('tab')

    price = str(table.loc[line, 'preco_unitario'])
    write(price)
    press('tab')

    cost = str(table.loc[line, 'custo'])
    write(cost)
    press('tab')

    obs = str(table.loc[line, 'obs'])
    if obs != 'nan':
        write(obs)

    press('enter')

    scroll(2000)
