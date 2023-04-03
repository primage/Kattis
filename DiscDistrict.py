"""
Link to the question: https://open.kattis.com/problems/discdistrict
"""
from math import sqrt

def main():
    r = int(input())
    rnow = r
    rmin = 10**6 + 1
    for i in range(1, r+1):
        x = rnow
        y = i
        print(x, y, sqrt(x**2 + y**2))
        if (sqrt(x**2 + y**2) > r):
            rnow = rnow - 1
            if (rmin > sqrt(x**2 + y**2)):
                rmin = sqrt(x**2 + y**2)
                xmin = x
                ymin = y
                print(xmin, ymin, rmin)
   
if __name__ == "__main__":
    main()
