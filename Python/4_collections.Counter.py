from collections import Counter

if __name__ == "__main__":
    shoes_numbers = int(input())
    shoes_sizes = Counter(map(int, input().split()))
    customers_number = int(input())

    total = 0

    for _ in range(customers_number):
        size, price = map(int, input().split())
        if shoes_sizes[size] > 0:
            total += price
            shoes_sizes[size] -= 1

    print(total)
