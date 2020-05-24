- Even number:

If a number is even, then its LSB is always 0 because even number is just some number multiplies 2, which is a left shift with 0 padded in bitwise calculation. So the total number of 1s of an even number N is the same with the one of the number N/2.

- Odd number:

An odd number is an even number plus 1. Because the LSB of an even number is 0, the total number of 1s of an odd nubmer N is just the total number of 1s of its previous even number (N-1) plus 1.