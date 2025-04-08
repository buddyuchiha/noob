import sys
import time

N = int(sys.stdin.readline())
string_list = []

for _ in range(N):
    string_input = sys.stdin.readline().strip()  
    string_list.append(string_input)
start_time = time.time()
impressive_string = ""
impressive_string_length = 0
old_impressive_string_length = 0
visited = set()

for string in string_list:
    if not string in visited:
        initial_length = len(visited)
        visited.update(string)
        impressive_string_length = len(visited) - initial_length
    if impressive_string_length > old_impressive_string_length:
        impressive_string = string
        old_impressive_string_length = impressive_string_length
end_time = time.time()  # Записываем время окончания

elapsed_time_ms = (end_time - start_time) * 1000  # Вычисляем прошедшее время в миллисекундах

print(f"Время выполнения: {elapsed_time_ms:.2f} мс")
print(f"Length: {len(impressive_string)}, Letters: {''.join(string for string in impressive_string)}")

# 5
# eeeeee
# jjjjjjjj
# eww
# abc
# rty

            