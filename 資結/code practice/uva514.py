while True:
    N = int(input())

    if N == 0:
        break
    
    while True:
        first = int(input())
        print(f"first={first}")
        if first == 0:
            print("break inside")
            break
        train = []
        train.append(first)
        # push N-1 times
        for i in range(1, N):
            t = int(input())
            train.append(t)
            # print
            print(f"train: {train}")
        
        
        