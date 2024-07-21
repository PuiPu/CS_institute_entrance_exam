while True:
    N = int(input())

    if N == 0:
        break
    
    first = 0

    while True:
        first = input()
        if first == 0:
            break
        train = []
        train.append(first)
        # push N-1 times
        for i in range(1, N):
            train.append(input())
        # print
        print(f"train: {train}")
        