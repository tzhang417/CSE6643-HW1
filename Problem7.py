# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 14:00:10 2023

@author: ztk
"""
import numpy as np
import time
import matplotlib.pyplot as plt

def naive(A, b):
    n = len(b)
    for a in range(n - 1):
        for i in range(a + 1, n):
            ratio = A[i, a] / A[a, a]
            for j in range(a, n):
                A[i, j] -= ratio * A[a, j]
            b[i] -= ratio * b[a]
    return backSub(A, b)
            
            
def pivot(A, b):
    n = len(b)
    for a in range(n - 1):
        max_index = a
        max_val = abs(A[a, a])
        for i in range(a + 1, n):
            if abs(A[i, a]) > max_val:
                max_index = i
                max_val = abs(A[i, a])
        if max_index != a:
            for i in range(a + 1, n):
                A[a, i], A[max_index, i] = A[max_index, i], A[a, i]
            b[a], b[max_index] = b[max_index], b[a]
        for i in range(a + 1, n):
            ratio = A[i, a] / A[a, a]
            for j in range(a, n):
                A[i, j] -= ratio * A[a, j]
            b[i] -= ratio * b[a]
    return backSub(A, b)

def backSub(A, b):
    n = len(b)
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]
    return x

def discretize(n, lamb):
    A = np.zeros((n, n))
    b = np.zeros(n)
    h = 1.0/n
    for i in range(n):
        A[i, i] = 2.0 - lamb * h**2
        b[i] = (3 * (i + 1)**2 * h**2 - 0.5) * h**2
    for i in range(n - 1):
        A[i, i + 1] = -1
        A[i + 1, i] = -1
    return A, b

n_values = [200, 400, 800, 1000, 2000]
lambdas = [0, 8]
naive_res = {0:[], 8:[]}
pivot_res = {0:[], 8:[]}
for lamb in lambdas:
    for n in n_values:
        print(n)
        A, b = discretize(n, lamb)
        Acop, bcop = np.copy(A), np.copy(b)
        start = time.time()
        sol1 = naive(A, b)
        end = time.time()
        naive_time = end - start
        naive_res[lamb].append(naive_time)
        
        start = time.time()
        sol2 = pivot(Acop, bcop)
        end = time.time()
        pivot_time = end - start
        pivot_res[lamb].append(pivot_time)
        
for lamb in lambdas:
    plt.figure(figsize=(10, 5))
    plt.plot(n_values, naive_res[lamb], label='Naive')
    plt.plot(n_values, pivot_res[lamb], label='Pivot')
    plt.xlabel('Mesh Points')
    plt.ylabel('Time')
    plt.title(f'Lambda {lamb}')
    plt.legend()
    plt.grid(True)
    plt.show()
        


