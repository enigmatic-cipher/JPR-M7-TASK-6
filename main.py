"""
Given two numbers, m and n as input, calculate the nth power of m. Use recursion. Do not use loops. Do a dry run for each test case.
Input-> m=2, n=5
Output-> 32
"""

def recur(m,n):  
  if (n==0):
    return 1
  else:    
    return (m * recur(n-1))
    
m = int(input("Enter m: "))            
n = int(input("Enter n: "))
print(recur(m,n))
