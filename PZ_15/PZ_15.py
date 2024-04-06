# Приложение ПЛАТНАЯ ПОЛИКЛИНИКА для некоторой организации. БД
# должна содержать таблицу Пациент со следующей структурой записи: ФИО пациента,
# ФИО врача, диагноз, стоимость лечение.

import sqlite3 as sq
from data_patient import info_patient

with sq.connect('klinika.db') as con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS patient")
    cur.execute("""CREATE TABLE IF NOT EXISTS patient(
    id_patient INTEGER PRIMARY KEY AUTOINCREMENT,
    fio_patient TEXT NOT NULL,
    fio_doctor TEXT NOT NULL,
    diagnoz TEXT NOT NULL,
    stoimost INTEGER NOT NULL
    )""")

with sq.connect('klinika.db') as con:
    cur = con.cursor()
    cur.executemany("INSERT INTO patient VALUES (?, ?, ?, ?, ?)", info_patient)

with sq.connect('klinika.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM patient")
    result = cur.fetchall()
    print(result)

with sq.connect('klinika.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM patient WHERE fio_doctor = 'Андреев Елисей Юрьевич'")
    result1 = cur.fetchall()
    print(result1)

with sq.connect('klinika.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM patient WHERE diagnoz = 'сколиоз'")
    result2 = cur.fetchall()
    print(result2)

with sq.connect('klinika.db') as con:
    cur = con.cursor()
    cur.execute("UPDATE patient SET stoimost = stoimost + 300")
    result6 = cur.fetchall()
    print(result6)

with sq.connect('klinika.db') as con:
    cur = con.cursor()
    cur.execute("UPDATE patient SET fio_patient = 'Сидорова Алиса Тимуровна' WHERE fio_patient = 'Котова Алиса Тимуровна'")
    result7 = cur.fetchall()
    print(result7)

with sq.connect('klinika.db') as con:
    cur = con.cursor()
    cur.execute("UPDATE patient SET stoimost = stoimost - 500 WHERE fio_patient = 'Щербаков Алексей Давидович'")
    result8 = cur.fetchall()
    print(result8)

with sq.connect('klinika.db') as con:
    cur = con.cursor()
    cur.execute("DELETE FROM patient WHERE id_patient = 5")
    result3 = cur.fetchall()
    print(result3)

with sq.connect('klinika.db') as con:
    cur = con.cursor()
    cur.execute("DELETE FROM patient WHERE stoimost = 1800")
    result4 = cur.fetchall()
    print(result4)

with sq.connect('klinika.db') as con:
    cur = con.cursor()
    cur.execute("DELETE FROM patient WHERE diagnoz = 'артрит'")
    result5 = cur.fetchall()
    print(result5)
