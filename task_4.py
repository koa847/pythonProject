from time import perf_counter
from sys import getsizeof

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

# print('Включение списка')
# start = perf_counter()
# result = [src[i] for i in range(1, len(src)) if src[i-1] < src[i]]
# print(result)
# print(getsizeof(result))
# print(f'{perf_counter() - start}\n')

print('Генератор')
start = perf_counter()
result = (src[i] for i in range(1, len(src)) if src[i-1] < src[i])
print(*result)
print(getsizeof(result))
print(f'{perf_counter() - start}\n')

# print('Включение множества')
# start = perf_counter()
# result = {src[i] for i in range(1, len(src)) if src[i-1] < src[i]}
# print(result)
# print(getsizeof(result))
# print(f'{perf_counter() - start}\n')