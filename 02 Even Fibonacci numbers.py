# Problem Statement
https://www.hackerrank.com/contests/projecteuler/challenges/euler002

# Problem explanation


fib_numbers = [1,2]
fib_numbers_EVEN = [2]

while (fib_numbers[-1]+fib_numbers[-2]) <= 4 * 10**16:
    fib_numbers.append(fib_numbers[-1]+fib_numbers[-2])
    if fib_numbers[-1] % 2 == 0:
        fib_numbers_EVEN.append(fib_numbers[-1])

print(fib_numbers)
print(fib_numbers_EVEN)

for _ in range(int(input())):
    n = int(input())
    start_index = 0
    end_index = len(fib_numbers_EVEN)
    while True:
        
        mid_index = (start_index + end_index) // 2

        if start_index == mid_index or end_index == mid_index: break

        if fib_numbers_EVEN[mid_index] < n:
            start_index = mid_index
        else:
            end_index = mid_index
        
    print(sum(fib_numbers_EVEN[:mid_index+1]))

    
