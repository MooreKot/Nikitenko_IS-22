# Даны строки S, S1 и S2. Заменить в строке S последнее вхождение строки S1 на строку S2.

S = "abc def ghi abc jkl abc asdsa adsasd"
S1 = "abc"
S2 = "123"
S = S[::-1].replace(S1[::-1], S2[::-1], 1)[::-1]
print(S)