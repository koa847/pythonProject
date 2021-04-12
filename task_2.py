conditions = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

str_list = []
for arr in conditions:
    if arr.isdigit():
        if len(arr) < 2:
            arr = "0" + arr
        str_list.extend(('"', arr, '"'))
    else:
        s = ""
        for a in arr:
            if a.isdigit():
                s = s + a
                arr = arr.replace(a, "", 1)
                if 0 < len(s) < 2 and len(arr) == 1:
                    s = "0" + s
                    arr = arr + s
                    str_list.extend(('"', arr, '"'))
                    arr = None
                    break
                elif 0 < len(s) <= 2 and len(arr) == 1:
                    arr = arr + s
                    str_list.extend(('"', arr, '"'))
                    arr = None
                    break
        if arr is not None:
            arr = arr + s
            str_list.append(arr)
print(' '.join(str_list))