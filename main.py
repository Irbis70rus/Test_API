import requests
import json
import pandas as pd
import xlsxwriter

Namelist = ['Bifur', 'Bofur', 'Bombur', 'Oin', 'Gloin', 'Balin', 'Dvalin', 'Dori', 'Nori', 'Ori', 'Fili', 'Kili', 'Torin']
PersonalData = []

#Задаю цикл по элементам списка
for i in Namelist:
#Отправляю заппрос декодирую и преобразовываю его в JSON словарь
    res = json.loads(
        requests.get(
            'https://api.agify.io/?',
            params={'name': i}
        ).content.decode('utf-8')
    )
#Наполнение финального списка
    PersonalData.append(res)

#Создаю DataFrame
a = pd.DataFrame(d for d in PersonalData)
#Записываю в файл .xlsx
writer = pd.ExcelWriter('example.xlsx', engine='xlsxwriter')
a.to_excel(writer, 'Sheet1')
writer.save()