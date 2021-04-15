def thesaurus(*arg):
    lib = {}
    for name in arg:
        if name[0] in lib:
            lib[name[0]].append(name)
        else: lib[name[0]] = [name]
    return lib


lib_name = thesaurus("Ярослав", "Иван", "Мария", "Петр", "Илья", "Михаил", "Инна", "Анна", "Алексей")
print(lib_name)

print("Отсортированный, по ключам, словарь:")

key_list = list(lib_name.keys())
key_list.sort()
lib_name_s = {}
for i in key_list:
    lib_name_s[i] = lib_name[i]
print(lib_name_s)