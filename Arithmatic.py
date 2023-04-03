"""
Link to the question: https://open.kattis.com/problems/arithmetic
"""

import sys

def main():
    my_input = input()
    if my_input == '0' or int(my_input) < 0:
        sys.exit(0)
    digits = list(str(my_input))
    while (digits[0] == '0'):
        digits.remove('0')
    base10 = 0
    base16 = []

    # base16 letters
    map16 = {
    '10':'A',
    '11':'B',
    '12':'C',
    '13':'D',
    '14':'E',
    '15':'F'
    }
    
    # base8 to base10
    for i,digit in enumerate(digits):
        digit = int(digit)
        base10 = base10 + (digit* 8**(len(digits) - i - 1) )
        
    # base10 to base16
    while(base10>=16):
        y, r = divmod(base10, 16)
        if y<16:
            base16 = [str(y)] + [str(r)] + base16
        else: 
            base16 = [str(r)] + base16
        base10 = y
    
    # change to letters
    base16L = []
    for n in base16:
        if n in map16.keys():
            base16L.append(n.replace(n, map16[n]))
        else:
            base16L.append(n)
    output = str(''.join(map(str,base16L)))
    print(output)
    
if __name__ == "__main__":
	main()