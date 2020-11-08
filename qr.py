from math import *
import numpy as np

def formMatrix(m,n):
    arr=[0]*m
    for i in range(m):
        arr[i]=[0]*n
        for j in range(n):
            arr[i][j]=float(input("Enter for position "+str(i+1)+","+str(j+1)+": "))
    return arr

def printMatrix(arr,m,n):
    for i in range(m):
        for j in range(n):
            print(round(arr[i][j],2),end=" ")
        print()

def dotProduct(v1,v2,n):
    s=0
    for i in range(n):
        s=s+v1[i]*v2[i]
    return s

def scalarProduct(v,a,n):
    vf=[]
    for i in range(n):
        x=v[i]*a
        vf.append(x)
    return(vf)

def length(v,n):
    sqSum=0
    for i in range(n):
        sqSum=sqSum+v[i]**2
    return sqrt(sqSum)

def projectOn(v1,v2,n):
    vx=dotProduct(v1,v2,n)
    l=dotProduct(v1,v1,n)
    m=vx/l
    vf=[]
    for i in range(n):
        x=v1[i]*m*(-1)
        vf.append(x)
    return vf

def productMatrix(a1,a2):
    C=np.dot(a1,a2)
    D=C.tolist()
    return D
    
def vectorForm(a,c):
    v=[]
    for i in range(len(a)):
        x=a[i][c]
        v.append(x)
    return(v)

def vectorOp(v1,v2,n):
    vf=[]
    for i in range(n):
        x=v1[i]+v2[i]
        vf.append(x)
    return vf

def transpose(v,m,n):
    a=[0]*m
    for i in range(m):
        a[i]=[0]*n
        for j in range(n):
            a[i][j]=v[j][i]
    return a

if __name__ == "__main__":

    print()
    print("\t\tWelcome to the QR-Decomposer (A=QR)")
    print()
    m=int(input("Input no. of rows of matrix A: "))
    n=int(input("Input no. of columns of matrix A: "))
    print()
    A=formMatrix(m,n)
    print()
    printMatrix(A,m,n)
    Q1=[]

    xx=vectorForm(A,0)
    dpx=dotProduct(xx,xx,m)
    lx=length(xx,m)
    y=scalarProduct(xx,(1/lx),m)
    Q1.append(y)

    for i in range(1,n):
        x=vectorForm(A,i)
        temp=x
        for i in range(len(Q1)):
            e=projectOn(Q1[i],x,m)
            temp=vectorOp(temp,e,m)
        l=length(temp,m)
        f=scalarProduct(temp,(1/l),m)
        Q1.append(f) 

    R=productMatrix(Q1,A)
    Q=transpose(Q1,m,n)

    print()
    print("The final Q is: ")
    printMatrix(Q,m,n)
    print()
    print("The final R is: ")
    printMatrix(R,n,n)
    print()
    print()



