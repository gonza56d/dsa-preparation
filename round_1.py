nums = [1, 2, 3, 2, 3]
k = 5


def main() -> int:
    count = 0
    for i, x in enumerate(nums):
        for j, y in enumerate(nums):
            if j != i:
                if x < y and x + y == k:
                    count += 1
    return count


if __name__ == '__main__':
    result = main()
    print(result)
