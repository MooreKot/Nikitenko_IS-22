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
