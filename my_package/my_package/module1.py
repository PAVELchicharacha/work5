import random
filename_f = 'file_f.txt'#запись
filename_g = 'file_g.txt'#запись отредактированная
num_numbers = 5
m = 3
n = 5
# Заполнение f
with open(filename_f, 'w') as file_f:
    for _ in range(num_numbers):
        number = random.randint(1, 1000)
        file_f.write(f"{number}\n")
# запись в g
with open(filename_f, 'r') as file_f, open(filename_g, 'w') as file_g:
    for line in file_f:
        number = int(line.strip())
        if number % m == 0 and number % n != 0:
            file_g.write(f"{number}\n")

print(f"Процесс завершен. Проверяйте файл {filename_g} для результатов.")
