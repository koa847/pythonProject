def result_dict (users_list, hobby_list):
    i = 0
    rt_dict = {}
    for lst_name in users_list:
        if i + 1 > len(hobby_list):
            rt_dict[lst_name.split(',')[0]] = None
        else: rt_dict[lst_name.split(',')[0]] = hobby_list[i]
        i += 1
    if i < len(hobby_list):
        sys.exit(1)
    return rt_dict

def read_file(name):
    with open(name, "r", encoding="utf-8") as f:
        return f.read().splitlines()

f_users = "users.csv"
f_hobby = "hobby.csv"
f_result = "users_hobby.txt"

with open(f_users, 'r', encoding="utf-8") as f_r, open(f_hobby, 'r', encoding="utf-8") as f_r2, open(f_result, 'w', encoding="utf-8") as f_w:
    for el in f_r:
        name = el.replace("\n", '')
        hy = f_r2.readline()
        f_w.write(f'{name}: {hy}\n')
