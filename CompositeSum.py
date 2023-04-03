import sys, math

def isprime(n):
    flag = False
    for i in range(2, math.floor(math.sqrt(n)+1)):
        x, r = divmod(n, i)
        if r==0 and x==n:
        flag = True
    return(flag)

def getY(N):
    x, r = divmod(N, 4) # 4 is the smallest composite number
    if (r==0):
        y = N-4
    elif (r==1):
        y = N-9
    elif (r==2):
        y = N-6
    else:
        y = N-15
    return(x, y)
            
def main():
    N = int(input())
    counter = 2
    if N<2 or N>1000000000000000000:
        sys.exit(0)
    if N%2 == 0: # even N
        x = int(N/2)
        y = int(N-x)
        print(counter)
        print(x, y)
    else: # odd N
        x, y = getY(N)
        
        while(isprime(y)): # y is a prime number
            counter = counter + 1
            if counter > 4:
                break                
        else:
            print(counter)
            print(x, y)
        for i in range(3, math.floor(math.sqrt(N))):
            x, r = divmod(N, i)
            if r==0:
                # prime number?
                y = N-x
                print(x, y)

if __name__ == "__main__":
    main()