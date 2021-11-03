import gspread
from datetime import datetime

def getCell(machine):

    rowNum = datetime.now()
    strNum = machine + 1
    strNum.__str__()
    cell = 'B'+str(strNum)
    return cell

def get
gc = gspread.service_account(filename='test1-330905-670f39e71bf8.json') #авторизация в гугл через данные в файле

sh = gc.open("test1") # открываем нужную таблицу

a = input()
b = a.split(' ')
machine = int(b[0])
#strNum = b[0]+1
#rowNum = datetime.date
cell = getCell(machine)
cellRange = cell +":"+cell
note = b[1]
sh.sheet1.format(cellRange,{"backgroundColor": {"red": 1, "green": 0, "blue": 0} }) # изменение цвета ячейки
sh.sheet1.insert_note(cell,note) #добавление комментария к ячейке "ячейка","коммент"

#print(sh.sheet1.get('A1'))
