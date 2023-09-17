# CSE6643-HW1

# Question 6
1. Import numpy to use its matrix method including tril (forms lower triangular matrices), linalg.norm (gets p-norm of a matrix), and linalg.cond (gets p-norm condition number).

2. In make_matrix, define a method that creates a lower triangular matrix with size of input m. Use numpy.random.normal to form a m-size matrix with entries of mean 0 and std sqr(m), and use numpy.tril to cut this matrix into a lower triangular matrix. Return this lower triangular matrix.

3. In main, perform the following process based on iteration i in [1:100]:

    a. get desired size cur by 100 * i;

    b. call make_matrix to make required matrix of size cur;

    c. use numpy.linal.norm to compute 2-norm and inf-norm (my GT ID# is odd), and calcualte the ratio;

    d. use numpy.linal.cond to compute 2-norm condition number;

    e. print the results;

4. Check sample output in the attached txt file.

# Question 7
1. Import numpy to create matrices and vectors using numpy.zeros. Import time to create stopwatches to calculate CPU times. Import matplotlib.pyplot to create plots and demonstrate end results.

2. In naive, performs naive gaussian elimination on input A and b similar to what we do by hands. Return reduced A and b.

3. In pivot, perform gaussian elimination with pivoting on input A and b. In each iteration, find the max_index, swap rows if necessary, and perform the elimination process in naive method. Return reduced A and b.

4. In backSub, perform backward substitution based on inputs (reduced A and b). Return result x.

5. In discretize, based on given funciton in Q7's prompt and input (size n and lambda), produce A and b to solve. First, calculate h = 1/n^2 and call numpy.zeros to create empty matrices A and b. Populate A such that: 

    a. A's diagonal entries are 2.0 - lambda * h**2;
    
    b. A's entries next to the diagonal entries are -1;

Popualte b such that b's entries are (3 * (i + 1)^2 * h^2 - 0.5) * h^2 for i in range [1, n]. Return populated A and b.

6. In main, store desired lambdas and n values for tests according to the prompt. Create empty maps (based on methods, keys are lambdas, values are CPU times) of lists to store computation results in the following steps and for demonstration use. For each lambda, perform the following steps on each n:

    a. call discretize with current n and lambda to retrieve A and b to start with;

    b. to avoid modification error, create copies of A and b for different methods;

    b. start the timer, perform naive methods, end the timer, and store the elapsed time;

    c. start the timer, perform pivot methods, end the timer, and store the elapsed time;

7. Demonstrate results of each lambdas by calling mathplotlib.pyplot. See results in attached screenshots.