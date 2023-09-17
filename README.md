# CSE6643-HW1

# Question 6
1. Import numpy to use its matrix method including tril (forms lower triangular matrices), linalg.norm (gets p-norm of a matrix), and linalg.cond (gets p-norm condition number).

2. In make_matrix, define a method that creates a lower triangular matrix of size m. Use numpy.random.normal to form a m-size matrix with entries of mean 0 and std sqr(m), and use numpy.tril to cut this matrix into a lower triangular matrix.

3. In main, perform the following process based on iteration i in [1:100]:
    a. get desired size cur by 100 * i;
    b. call make_matrix to make required matrix of size cur;
    c. use numpy.linal.norm to compute 2-norm and inf-norm (my GT ID# is odd), and calcualte the ratio;
    d. use numpy.linal.cond to compute 2-norm condition number;
    e. print the results;

4. check sample output in the attached txt file.