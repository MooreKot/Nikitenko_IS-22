# Составить генератор (yield), который выводит из строки только цифры.
st = "abc123def456"
def only_digits(st):
    for i in st:
        if i.isdigit():
            yield i

digits = "".join(only_digits(st))
print(digits)