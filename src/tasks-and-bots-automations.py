from pyautogui import hotkey, scroll, click, press, typewrite
from pandas import read_csv

email = 'jou@gmail.com'
senha = 'senha'
site = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
# Abrir site
press('win')
typewrite('brave web browser')
press('enter')
typewrite(site)

# Login
typewrite(email)
press('tab')
typewrite(senha)
press('enter')


# Pegar dados do .csv
table = read_csv('src/produtos.csv')

# Inserir dados
for line in table.index:
    click(x=630, y=450)

    code = table.loc[line, 'código']
    typewrite(code)
    press('tab')

    brand = table.loc[line, 'marca']
    typewrite(brand)
    press('tab')

    ptype = table.loc[line, 'tipo']
    typewrite(ptype)
    press('tab')

    category = table.loc[line, 'categoria']
    typewrite(category)
    press('tab')

    price = table.loc[line, 'preço']
    typewrite(price)
    press('tab')

    cost = table.loc[line, 'custo']
    typewrite(cost)
    press('tab')

    obs = table.loc[line, 'obs']
    typewrite(obs)
    press('enter')

    scroll(5000)