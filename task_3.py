conditions = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
str_list = []
i = 0
while i < len(conditions):
    cond = conditions[i]
    if cond.isdigit():
        if len(cond) < 2:
            cond = "0" + cond
        conditions.pop(i)
        conditions.insert(i, ['"', cond, '"'])
        i += 1
    else:
        s = ""
        for a in cond:
            if a.isdigit():
                s = s + a
                cond = cond.replace(a, "", 1)
                if 0 < len(s) < 2 and len(cond) == 1:
                    s = "0" + s
                    cond = cond + s
                    conditions.pop(i)
                    conditions.insert(i, ['"', cond, '"'])
                    cond = None
                    i += 1
                    break
                elif 0 < len(s) <= 2 and len(cond) == 1:
                    cond = cond + s
                    conditions.insert(i, ['"', cond, '"'])
                    cond = None
                    i += 1
                    break
        if cond is not None:
            cond = cond + s
            conditions.pop(i)
            conditions.insert(i, cond)
            i += 1
n = 0
while n < len(conditions):
    if type(conditions[n]) == list:
        for el in conditions[n]:
            conditions.insert(n, el)
            n += 1
        del conditions[n]
    else: n += 1
print(' '.join(conditions))