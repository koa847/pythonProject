conditions = [57.8, 46.51, 97, 7.15, 12, 5.39, 98.5, 76, 58.3, 55.8, 48.51, 17, 27.15, 12.8, 4.89, 98.6, 76.3, 58.5, 89.5, 49.3]
def list_format (array):
    msg = ''
    for el in array:
        el = str(el)
        el = el.split('.')
        if len(el) == 1:
            el.append('00')
        elif len(el[1]) < 2:
            el[1] = '0' + el[1]
        msg += el[0] + 'руб. ' + el[1] + 'коп., '
    return msg
messag = list_format(conditions)
print(messag)

print(f'id первоночального списка: {id(conditions)}')
conditions.sort()
messag = list_format(conditions)
print(messag)
print(f'id отсортированого списка: {id(conditions)}')

list_s = sorted(conditions, reverse=True)
list_s = list_s[:5]
messag = list_format(list_s)
print(messag)