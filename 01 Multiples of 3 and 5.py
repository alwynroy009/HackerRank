# Problem Statement
# https://www.hackerrank.com/contests/projecteuler/challenges/euler001/problem

# Explanation
# https://youtu.be/W9waywE2tfQ

def sum_of_N_numbers(N):
    return N*(N+1)//2

sum_N = sum_of_N_numbers

for _ in range(int(input())):
    n = int(input().strip())
    n -= 1
    print(3*sum_N(n//3) + 5*sum_N(n//5) - 15*sum_N(n//15))
