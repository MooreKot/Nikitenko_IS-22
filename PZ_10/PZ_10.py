# Туристические агентства предлагают следующие туры. Вояж – Мексика,Канада,Израиль,
# Италия . РейнаТур – Англия,Япония,Канада,ЮАР. Определить:
# 1. какие туры из Вояж, отсутствуют в РейнаТур.
# 2. какие товары из РейнаТур, отсутствуют в Вояж
# 3. перечень одинаковых туров.
# 4. равны ли перечни туров
Voyazh = {'Мексика', 'Канада', 'Израиль', 'Италия'}

ReinaTur = {'Англия', 'Япония', 'Канада', 'ЮАР'}
R_no = Voyazh - ReinaTur
print(f'В РейнаТур отсутствуют туры: {Voyazh - ReinaTur}')
print(f'В Вояж отсутствуют туры: {ReinaTur - Voyazh}')
print(f'В двух агентствах есть тур в: {Voyazh & ReinaTur}')

if Voyazh == ReinaTur:
    print('Перечень туров одинаковый')
else:
    print('Перечень туров разный')
