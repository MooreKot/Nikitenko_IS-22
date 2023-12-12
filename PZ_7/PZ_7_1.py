# Дано целое число N (>0) и строка S. Преобразовать строку S в строку длины N
# следующим образом: если длина строки S больше N, то отбросить первые символы,
# если длина строки S меньше N, то в ее начало добавить символы «.» (точка).

def transform(N, S):
    if len(S) > N:
        return S[len(S)-N:]
    elif len(S) < N:
        return '.' * (N - len(S)) + S
    else:
        return S
while True:
    try:
        N = int(input("Введите целое число: "))
        S = input("Введите сообщение: ")

        result = transform(N, S)
        print(result)
        break
    except ValueError:
        print('Ошибка! Введите целое число.')
