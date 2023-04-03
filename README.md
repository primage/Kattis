# Kattis

This repository contains python scripts for several [Kattis](https://open.kattis.com/problems) exercise and test problems. The text below briefly describes the logic behind each script of the test problem.

## MathOperations.py

Question: Multiple sets of 3 numbers are given. The question asks to check if any of the plus, minus, times, and divide operations between any two numbers is equal to the other remaining number. If at least one operation gives the correct result, print 'Possible'. If none is correct, print 'Impossible'.

To avoid doing a nested for loop through all numbers in all input cases, the script finds the greatest number among the 3 and start from there. For addition and multiplication, the operation between the two smaller numbers, despite the order, is equal to the greatest number. As for subtraction and division, I start with the greatest number and operates with any other remaining number to get the another remaining one. 


## SortingPeanut.py

Question: Given the x and y coordinates of a peanut and its size, check if it is in a box or on the floor. If it is in a box, check if it is in the box that matches its size (small, medium, large). 

The box (peanut) coordinates and sizes are stored as a list in a box (peanut) dictionary. Here, the coordinates are converted from string to float. Three nested for loops are run in the following order for each test case: loop through the box and peanut dicts at the same time, then loop through all peanuts, then loop through all boxes.

Two corners of a square, i.e. a 2D-box in this case, are given: (x1, y1) and (x2,y2). The peanut's (x,y) coordinate is then checked if x1<=x<=x2 and y1<=y<=y2. If both conditions hold, then the peanut is in a box. Then, the box size is checked and the code breaks the box's 'for loop' in order to go to the next box. If the peanut is not in a box, then it is on the floor and the code breaks the peanut's 'for loop' in order to go to the next peanut. 


## ExitTheWood.py
Question: From the starting clearing where my friend is, find the average time it takes to get to the exit clearing -- given that he may run along any path to any clearing with an equal chance and that it takes him exactly 1 minute to walk from one clearing to another.

This is a probability question, where the probablty of being at each clearing for each time step (time step: moving from one clearing to the next) is calculated. This is done by using the probabilty distribution from the previous step and calculating the probabilty distribution of the next step. At each step, the probabilty of being at the exit clearing is accumulated and used as the average time of exiting the woods.

The calculation for expected time of exiting the wood is $$E = 1*P_1 + 2*P_2 + 3*P_3 + ... + N*P_N$$. Here, $P_i$ is the probabilty of being at the exit clearing at step i and $P_i$ is multiplied by the time it takes to take i steps (which is i minutes). This caulculation of E is within the absolute error of $10^{-5}$ if a large number of steps is taken, which in this case is achievable with 10,000 steps.

//
Prim Pasuwan
