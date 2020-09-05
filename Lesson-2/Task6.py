#6.Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]

# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например название, а значение — список значений-характеристик,
# например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

constName = 'название'
constPrice = 'цена'
constCnt = 'количество'
constIzm = 'ед'

lstTovars = []

while True:
    num = int(input("Укажите номер товара = "))

    name = input("Укажите название товара = ")
    price = float(input("Укажите цену товара = "))
    cnt = int(input("Укажите количество товара = "))
    izm = input("Укажите единицу измерения товара = ")

    ldict = dict()
    ldict.update({constName: name});
    ldict.update({constPrice: price})
    ldict.update({constCnt: cnt})
    ldict.update({constIzm: izm})

    lTovar = (num, ldict)
    lstTovars.append(lTovar)

    str = input("Продолжить ввод? (y, yes, да - ДА, иначе - НЕТ) = ")
    if not str.lower() in ['y', 'yes', 'да']:
        break

#print('\nВведенные товары:')
#print(lstTovars)

lstNames = []
lstPrices = []
lstCnts = []
lstIzms = []

for i in lstTovars:
    tmp = tuple(i);
#    print(int(tmp[0]))
    lTmpDict = dict(tmp[1])
#    print(lTmpDict)

    if lstNames.count(lTmpDict.get(constName)) == 0:
        lstNames.append(lTmpDict.get(constName))

    if lstPrices.count(lTmpDict.get(constPrice)) == 0:
        lstPrices.append(lTmpDict.get(constPrice))

    if lstCnts.count(lTmpDict.get(constCnt)) == 0:
        lstCnts.append(lTmpDict.get(constCnt))

    if lstIzms.count(lTmpDict.get(constIzm)) == 0:
        lstIzms.append(lTmpDict.get(constIzm))


lstItog = dict()

lstItog.update({constName: lstNames})
lstItog.update({constPrice: lstPrices})
lstItog.update({constCnt: lstCnts})
lstItog.update({constIzm: lstIzms})


print('\nАналитика:')
print(lstItog)

#print('\nАналитика:')
#for i in lstItog.keys():
#  print(f"{i}: {lstItog.get(i)}")
