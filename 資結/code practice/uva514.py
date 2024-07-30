while True:
    N = int(input())
    if N == 0:
        break
    
    while True:
        # origin train
        train = [int(t) for t in range(1, N+1)]
        # destination
        station = input().split()
        station = [int(t) for t in station] # to int array
        first = station[0]
        if first == 0:
            print() # null line
            break
        
    
        print(f"train: {train}")
        print(f"station : {station}")
        
        # logic part
        stack = []
        idx = 0 # pointer of "train"
        for t in train:
            stack.append(t)
            
            if (t == station[idx]):
                print(f"    t={t}")
                idx += 1
                stack.pop()
        while len(stack) != 0 and 

        # print(f"stack={stack}")   
        # if len(stack) == 0:
        #     print("yes")
        # else:
        #     print("no")            
        # print
               
        