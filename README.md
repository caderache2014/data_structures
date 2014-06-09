data_structures
===============

Data structures for Python Dev Accelerator

Parenthetics:

The first thought would be to apply a recursive approach to build a solution for f(n) by
adding pairs of parenthesies to f(n-1).

Consider the solution for n = 3.
 
 (()()) ((())) ()(()) (())() ()()()

How do we build this from n = 2?
(()) ()()

We can do this by inserting pairs of parentheses inside every existing pair of parentheses
as well as one at the beginning of the string. Any other places we could insert parentheses would
reduce to the end of the string.

So we have the following:
(()) --> (()())  #insert pair after the 1st left paren
      --> ((()))   #insert pair after 2nd left paren
      --> ()(())   #insert pair at beginnign of string
()() --> (())()   #inserted pair after 1st left paren
      --> ()(())   #inserted pair after 2nd left paren
      --> ()()()   #inserted pair at beginning of string

Notice that the string ()(()) is listed twice
So we'll need to keep track of duplicate values

We build the string from scratch; under this approach we add left and right parens
as long as the expression stays valid

On each recusive call we have the index for a particular character in the string.
We need to select a left or right parens.

1. Left: as long as we havent' used up all the left parens, we can always insert a left parens
2. Right: we can insert a right paren as long as it won't lead to a syntax error.
             We only get a syntax error if there are more right parens than left.

So we keep track of the number of right and left parens allowed. 
If there are left parens remaining we'll insert  a left and recurse.
If there are more right parens remaining than left (i.e. if there are more
left parens in use than right parens), then we insert a right paren recurse