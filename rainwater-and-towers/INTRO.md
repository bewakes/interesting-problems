[Back to list](https://github.com/bewakes/interesting-problems/blob/master/README.md)

## Rainwater collection over towers

#### You are given an input array whose each element represents the height of a line towers. The width of every tower is 1. It starts raining. How much water is collected between the towers?

Here's an example image(Credit: a stackoverflow post) for towers with following heights: [5,3,7,2,6,4,5,9,1,2] 

![](https://i.stack.imgur.com/pksAK.png)

The basic idea for the solution is that, for any tower, the amount of water that accumulates over it is dependent on the towers with maximum
heights to its left and to its right.  
So if `t` is the tower height and `lm` is the maximum hight of a tower to its left(inclusive)
and `rm` is the max height of a tower to its right(inclusive), then the water collected above it is:  
 `min(lm, rm) - t`.  
 
Finally, sum that value for all towers
