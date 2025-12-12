input_angka = [4, 1, 13, 7, 0, 2, 8, 11, 3]

semuaBest_list = []      
semuaBest_len = 0       

def dfs(index, current, depth):
    global semuaBest_len, semuaBest_list

    print("  " * depth + f"{current}")

    # Update LIS terbaik
    if len(current) > semuaBest_len:
        semuaBest_len = len(current)
        semuaBest_list = [current[:]]     
    elif len(current) == semuaBest_len:
        semuaBest_list.append(current[:]) 

    for i in range(index, len(input_angka)):
        if not current or input_angka[i] > current[-1]:
            dfs(i + 1, current + [input_angka[i]], depth + 1)


dfs(0, [], 0)

print("\n============================")
print("Jumlah semua LIS dengan panjang maksimum =", semuaBest_len)
for lis in semuaBest_list:
    print(lis)