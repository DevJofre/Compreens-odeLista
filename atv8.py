from datetime import date, timedelta


def eh_bissexto(ano):
    return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)


ano = 2024

datas_janeiro = [date(ano, 1, dia) for dia in range(1, 32)]

print(datas_janeiro)
