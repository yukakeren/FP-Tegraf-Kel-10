class LMISFinder:
    def __init__(self, input_list):
        self.arr = input_list
        self.max_len = 0
        self.all_best = []

    def dfs(self, index, current, depth):
        COLORS = [
            "\033[91m", "\033[92m", "\033[93m", "\033[94m",
            "\033[95m", "\033[96m", "\033[97m"
        ]
        RESET = "\033[0m"

        color = COLORS[depth % len(COLORS)]
        print("  " * depth + color + f"{current}" + RESET)

        if len(current) > self.max_len:
            self.max_len = len(current)
            self.all_best = [current[:]]
        elif len(current) == self.max_len:
            self.all_best.append(current[:])

        for i in range(index, len(self.arr)):
            if not current or self.arr[i] > current[-1]:
                self.dfs(i + 1, current + [self.arr[i]], depth + 1)

    def find_all_lis(self):
        self.dfs(0, [], 0)
        return self.all_best, self.max_len


if __name__ == "__main__":
    input_angka = [4, 1, 13, 7, 0, 2, 8, 11, 3]

    finder = LMISFinder(input_angka)
    all_lis, panjang = finder.find_all_lis()

    print("\n============================")
    print("Jumlah semua LMIS dengan panjang maksimum =", panjang)
    for lis in all_lis:
        print(lis)
