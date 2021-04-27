f_name = "nginx_logs.txt"
with open(f_name,"r", encoding="utf-8") as f:
    f_list = []
    for row in f:
        remote_addr = row.split(" - - ")[0]
        request_type =row.split('] "')[1].split(' ')[0]
        requested_resource = row.split('] "')[1].split(' ')[1].split(' ')[0]
        f_line_tuple = (remote_addr, request_type, requested_resource)
        f_list.append(f_line_tuple)

addr_dict = {}
for line in f_list:
    if line[0] in addr_dict:
        addr_dict[line[0]] += 1
    else:addr_dict[line[0]] = 1

addr_dict = {k: addr_dict[k] for k in sorted(addr_dict, key=addr_dict.get, reverse = True)}
addr_list = list(addr_dict.keys())
print(f'IP адрес спамера: {list(addr_dict.keys())[0]}, с данного адреса поступило - {list(addr_dict.values())[0]} запросов')