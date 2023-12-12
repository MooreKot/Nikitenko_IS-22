# Даны строки S, S1 и S2. Заменить в строке S последнее вхождение строки S1 на строку S2.

S = "abc def ghi abc jkl abc asdsa adsasd"
S1 = "abc"
S2 = "123"
index_last = S.rfind(S1)
S = S[:index_last] + S2 + S[index_last + len(S2):]
print(S)