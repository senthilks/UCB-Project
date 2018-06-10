# -*- coding: utf-8 -*-
"""
@author: Senthil Subramaniam

"""
from numpy import random, matrix

print('Create matrix A with size (3,5) containing random numbers A = np.random.random(15)')
A = random.random(15)
A = A.reshape(3,5)
A = matrix(A)
print (A)

print('\n')
print('size and length of matrix A')
print (A.size)
print (len(A))
print (A.shape)

print('\n')
print('Resize (crop/slice) matrix A to size (3,4)')
A = A[:3,[0,1,2,3]]
print(A)

print('\n')
print('Find the transpose of matrix A and assign it to B')
B = A.transpose()
print (B)

print('\n')
print('Find the minimum value in column 1 of matrix B ')
print(B[:3,0].min())

print('\n')
print('Find the minimum and maximum values for the entire matrix A')
print(A.min())
print(A.max())

print('\n')
#Create vector X (an array) with 4 random numbers
#Create a function and pass vector X and matrix A in it
#In the new function multiply vector X with matrix A and assign the result to D
print ('Vector and function')
X = random.random(4)
print(X)
print('\n')
def multiply_vector(A,B):
    D = A * B
    return D

# D = multiply_vector(X,A)   - need to check

print('\n')  
print(' Create a complex number')
Z = complex(5,3)
print(Z.real)
print(Z.imag)
print(abs(Z))

print('\n') 
#Multiply result D with the absolute value of Z and record it to C
C= abs(Z) * B
print(C)   

print('\n') 
print('matrix to string')
B = str(B)
print(B)

print('\n') 
print('Senthil Subramaniam is done with HW2')