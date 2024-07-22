while True:
    N = int(input())
    if N == 0:
        break
    
    while True:
        station = input().split()
        station = [int(t) for t in station] # to int array
        
        first = station[0]
        if first == 0:
            print() # null line
            break
        
        pass_or_not = True
        
        for i in range (2, len(station)-1):
            if station[i-1] > station[i] and station[i] < station[i+1]:
                pass_or_not = False
                break
        
        if pass_or_not:
            print("Yes")
        else:
            print("No")
            