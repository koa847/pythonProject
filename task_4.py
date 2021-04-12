conditions = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for el in conditions:
    el = el.split()
    el = el.pop()
    el = el.capitalize()
    print(f'Привет, {el}!')