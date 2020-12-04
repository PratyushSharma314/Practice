if __name__ == '__main__':
    n = int(input())
    arr = set(map(int, input().split()))

    """arr = list(arr)
    
    largest, larger = arr[0], arr[0]

    for n in arr:
        if n > largest:
            largest, larger = n, largest
        elif n > larger:
            larger = n
    
    print(larger)"""

    arr = list(arr)

    largest = max(arr)

    larger = max(n for n in arr if n != largest)
    print(larger)

