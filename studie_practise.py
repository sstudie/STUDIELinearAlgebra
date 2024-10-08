# -*- coding: utf-8 -*-
"""STUDIE_Practise.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10hbrydLo_3YpcVdzNj0wKn2aS5iyd9So
"""

import numpy as np
import matplotlib.pyplot as plt
import torch
import math

t = np.linspace(0,40,1000)

d_r =  2.5 * t
d_s = 3 * (t-5)

# RUN L2 NORM Idea
x =  np.array([25,2,2])
x

(25**2 + 2**2 + 2**2)**(1/2)

xx =  np.array([25,2,3,4])
xx

(25**2 + 2**2 + 3**2 + 4**2)**(1/2)

# automatically  do a L2 NORMALIZE  using python library
np.linalg.norm(x)

# RUN L1 NORM IDEA
x =  np.array([25.22,-2,2.34])
x

np.abs(25) + np.abs(-2) + np.abs(2)

# RUN Squared L2 Norm
x =  np.array([25,2,2])
x

np.dot(x,x)

# MAX NORM
x =  np.array([25,2,2])
x

np.max(x)

x = np.array([[1,2,3],[4,5,6]])
x

x[:,1]

x[1,:]

# REDUCTION

x =  np.array([[2,3],[4,5],[6,7]])
x

x.sum()

X_torch = torch.asarray([[2,3],[4,5],[6,7]])
X_torch

torch.sum(X_torch)

# DOT PRoduct in ML and DL
# Say 2 Vectors
x = np.array([2,3,4])
y =  np.array([4,3,2])

x

y

np.dot(x,y)

XP = np.linspace(-10,10,2000)
XP

#Frebenous NORM

Xfn = np.array([[2,3], [4,5]])
Xfn

np.linalg.norm(Xfn)

Xsym =  np.array([[1,2,3],[4,5,6],[7,8,9]])
Xsym

Xsym.T

Xsym == Xsym.T

XidentifyM =  np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
XidentifyM

XidentifyM.T

XidentifyM == XidentifyM.T

Xmat = np.array([2,3,4,5])
Xmat

np.dot(XidentifyM, Xmat)

Xnew =  np.array([[3,4],[5,60]])
Xnew

np.linalg.inv(Xnew)

# X * Xinversion =  Identity Matrix (output)
IdentityM = Xnew * np.linalg.inv(Xnew)

IdentityM

IdentityM.T

# EIGEN DECOMPOSITION

v = np.array([3,1])
v

E =  np.array([[1,0],[0,-1]])
E

Ev = np.dot(E,v)
Ev

Ve =  np.dot(v,E)
Ve

#PRACTISE EIGENVECTOR AND EIGENVALUE

A =  np.array([[2,3],[5,6]])
A

# EIgenVector  -  A X =  Lambda X
Lambdah , X =  np.linalg.eig(A)

Lambdah

X

LHS =  np.dot(A, X)
LHS

RHS1 =  np.dot(Lambdah[0], X)
RHS1

RHS2 =  np.dot(Lambdah[1], X)
RHS2

"""# FROM ABOVE EXAMPLE EigneValue = 1, since from the equ above lhs = rhs"""

# FROM AOVE EXAMPLE EigneValue = 1, since from the equ above lhs = rhs

"""# FINDING DETERNMINANT OF A SQUARE MATRIX"""

#PRACTISE EIGENVECTOR AND EIGENVALUE

A =  np.array([[2,3],[5,6]])
A

DETERMINANT_A = np.linalg.det(A)
DETERMINANT_A

#DETERMINANT EXAMPLE WITH 3 * 3 MATRIX
b =  np.array([[1,2,3],[-3,5,7],[9,0,3]])
b

DETERM_B =  np.linalg.det(b)
DETERM_B

# comparing eigenvalues and determinant
# DETERMINANT OF MATRIX X = PRODUCT OF LAMBDA OF MATRIX X

lambdaX, Vector = np.linalg.eig(b)
print(lambdaX)
print(Vector)

np.product(lambdaX)

#EIGENDECOMPOSITION

A =  np.array([[1,2,3,4],[4,5,3,4],[6,7,3,3],[4,2,6,0]])
A

lam, V = np.linalg.eig(A)

print(lam)

V

# eigendecomposition   = V A V-1
# v = vector, v-1 = inverse of vector, A = diagonal matrix
A =  np.array([[2,5],[6,8]])
A

lambdas , V =  np.linalg.eig(A)

lambdas

V

Vminus =  np.linalg.inv(V)
Vminus

diagonal =  np.diag(A)
diagonal

E = np.dot(V, np.dot(diagonal, Vminus))
E

"""# REAL World Applications of eigendecomposition use cases"""

# real world eigendecomposition use cases

# SVD for Decomposition EXAMPLE
A = np.array([[3,4],[6,7]])
A

#SVD = U * D * VT
U , D, VT =  np.linalg.svd(A)

# M * M Matrix
U

# M * N Matrix
D2 = np.diag(D)
D2

# N * N Matrix
VT

# LHS == RHS
A = np.dot(U, np.dot(D2, VT))
A

# SVD for Image Compression
#------------------
from PIL import Image

!wget https://static.scientificamerican.com/sciam/cache/file/4BC816FB-F21A-49C2-A9CB4D85FD64EF69_source.jpg

# Moore Penrose PseudoINverse for Non Square Matrix

# A+ = UT D+ V -  Moore Penrose equation for Non Square matrix

# We KNOW that SVD - is applied on square matrix
# SVD =  U D VT
# U = M * M matrix, VT =  N * N matrix, D = Diagonal, M * N matrix

A = np.array([[3,6],[6,2],[7,3]]) # NON Squared Matrix or Non SIngular Matrix
A

U,D,VT =  np.linalg.svd(A)

U

D
D = np.diag(D)
D

1/11.28019116

1/3.969545

VT

DPlus = np.linalg.inv(D)
DPlus

UT =  U.T
UT

V = VT.T
V

# DIRECT NUMPY LIBRARY TO FIND THE PSEUDOINVERSE
A =  np.array([[4,3,5],[2,6,7]])
A

MOOREPENROSE =  np.linalg.pinv(A)
MOOREPENROSE

# MOORE PENROSE PSEUDOINVERSE IN REAL LIFE LINEAR REGRESSION
# y = mx + B
#  m = slope, B = intercept
x =  [1,2,3,4,5,6]
y = [1.54,2.34,3.34,4.42,5.56,6.43]

x

len(x)

y

fig , ax =  plt.subplots()
plt.title('Linear regression Moore Penrose PSeudoInverse TEST')
plt.xlabel("X points")
plt.ylabel("Y points")
_ = ax.scatter(x,y)

X0 = np.ones(len(x))
X0

np.matrix(X0).T

np.matrix(x).T

Xnew = np.concatenate((np.matrix(X0).T, np.matrix(x).T), axis=1)
Xnew

# find wieghts from the equation
# WE WILL GET SLOPE AND INTERCEPT USING THE MOORE PENROSE PSEUDOINVERSE


# Y =  WX
# Y * X-1 = W
# W =  Y X+

W = np.dot(np.linalg.pinv(Xnew),y)
W

# Y INtercept =  W[0][0] = 0.41933333
# Slope of the Line =  W[0][1]

WValues =  np.asarray(W)
YIntercept = WValues[0][0]
YSlope = WValues[0][1]

YIntercept

YSlope

"""# PARTIAL Derivativrs using torch
#Example = volume of Cylinder
#V =  pie * r*r * l

---


"""

r =  torch.tensor(3.).requires_grad_()
r

l =  torch.tensor(5.).requires_grad_()
l

v =  math.pi * r**2 * l
v

v.backward()

l.grad

#derivate wrt to l
v=  math.pi * r**2
v

r.grad

#derivate wrt to r
v=  math.pi * l * 2 * r
v

