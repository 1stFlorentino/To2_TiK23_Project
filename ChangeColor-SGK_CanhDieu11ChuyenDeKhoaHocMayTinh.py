def doimau (M,N,magic,r,c,m,n): 
    magic[r] [c]=m
    if (c + 1 <= N) and (magic [r][c + 1] ==n) :
        doimau (M, N, magic,r,c+1,m,n)
    if (c - 1 >= 0) and (magic [r] [c-1]==n):
        doimau (M, N, magic,r,c-1,m,n)
    if (r + 1 <= M) and (magic [r+1] [c]==n):
        doimau (M, N, magic,r+1,c,m,n)
    if (r - 1 >= 0) and (magic [r - 1][c] ==n) :
        doimau (M,N,magic,r-1,c,m,n)
        
M, N=map(int, input().split()) 
magic=[]
for i in range(M):
    x=[int(i) for i in input().split()]
    magic.append(x)
r,c,m=map(int, map(int,input().split())) 
n=magic[r-1] [c-1]
doimau (M-1,N-1, magic,r-1, c-1,m,n)
for i in range(N): 
    for ii in range(M):   
        print(magic[i] [ii],end=' ')
    print()