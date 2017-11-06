# Determining the minimax value for given positions of the Reversi game, using Alpha-Beta Pruning.
## CSCI 561: Foundations of Artificial Intelligence
### Homework #1

In this project, you will write a program to determine the minimax value for given positions of the Reversi game, using the Alpha-Beta pruning algorithm with positional weight evaluation functions. The rules of the Reversi game can be found at  http://en.wikipedia.org/wiki/Reversi  and interactive examples can be found at  http://www.samsoft.org.uk/reversi/ .

The following input instance asks to compute a depth-2 alpha-beta search from the starting game position.
### Sample Input :
X
2
********
********
********
***OX***
***XO***
********
********
********

### Sample Output :
********
********
***X****
***XX***
***XO***
********                                          
********
********
Node,Depth,Value,Alpha,Beta
root,0,-Infinity,-Infinity,Infinity
d3,1,Infinity,-Infinity,Infinity
c3,2,-3,-Infinity,Infinity
d3,1,-3,-Infinity,-3
e3,2,0,-Infinity,-3
d3,1,-3,-Infinity,-3
c5,2,0.0,-Infinity,-3
d3,1,-3,-Infinity,-3
root,0,-3,-3,Infinity
c4,1,Infinity,-3,Infinity
c3,2,-3,-3,Infinity
c4,1,-3,-3,-3
root,0,-3,-3,Infinity
f5,1,Infinity,-3,Infinity
f4,2,0,-3,Infinity
f5,1,0,-3,0
d6,2,0,-3,0
f5,1,0,-3,0
f6,2,-3,-3,0
f5,1,-3,-3,-3
root,0,-3,-3,Infinity
e6,1,Infinity,-3,Infinity
f4,2,0,-3,Infinity
e6,1,0,-3,0
d6,2,0,-3,0
e6,1,0,-3,0
f6,2,-3,-3,0
e6,1,-3,-3,-3
root,0,-3,-3,Infinity
