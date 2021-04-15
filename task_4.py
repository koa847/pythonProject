def thesaurus_adv(*args):
    lib = {}
    for str in args:
        name = str.split(' ')[0]
        lst_name = str.split(' ')[1]
        if lst_name[0] in lib:
            if name[0] in lib[lst_name[0]]:
                lib[lst_name[0]][name[0]].append(str)
            else: lib[lst_name[0]][name[0]] = [str]
        else:
            if lst_name[0] in lib and name[0] in lib[lst_name[0]]:
                lib[lst_name[0]][name[0]].append(str)
            else:
                lib[lst_name[0]] = {name[0]: [str]}
    return lib

def print_lib(lib):
    for first_letter in lib:
        print(f'"{first_letter}":')
        for second_letter in lib[first_letter]:
            arr = ", ".join(lib[first_letter][second_letter])
            str = '"' + second_letter + '": ' + arr
            print(str.rjust(len(str)+4))


lib_adv = thesaurus_adv("Ярослав Игнатьев", "Александр Самойлов", "Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Борис Солодов")
print_lib(lib_adv)
print("\nСписок после сортировки:")
lib_adv_s = {}
key_list = list(lib_adv.keys())
key_list.sort()
for i in key_list:
    lib_adv_s[i] = lib_adv[i]
lib_adv = lib_adv_s
lib_adv_s = {}
lib_adv_ss = {}
for fst_name in lib_adv:
    key_list = list(lib_adv[fst_name].keys())
    key_list.sort()
    for s in key_list:
        lib_adv_s[s] = lib_adv[fst_name][s]
    lib_adv_ss[fst_name] = lib_adv_s
    lib_adv_s = {}
lib_adv = lib_adv_ss
del lib_adv_s
del lib_adv_ss
del key_list
print_lib(lib_adv)