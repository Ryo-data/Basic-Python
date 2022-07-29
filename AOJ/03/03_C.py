while True:
    x,y= map(int,input().split())
    if x == 0 and y == 0:
        break
    list = [x,y]
    list.sort()
    print(list[0],list[1])
    
   


