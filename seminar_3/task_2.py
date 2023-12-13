# num_list = list(input("Введи цифры: "))
num_list = [_ for _ in range(10)]
k = int(input("Введи k: "))

print(num_list[-k:] + num_list[:-k])
print(num_list)
