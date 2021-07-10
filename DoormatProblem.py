N,M = map(int,input().split(" "))    #Taking the input
for i in range(1,N,2):   #Loop for upper design
    print((i * ".|.").center(M, "-"))  
print("WELCOME".center(M,"-"))  #Printing the middle design
for i in range(N-2,-1,-2):    #Loop for lower design
    print((i * ".|.").center(M, "-"))    
