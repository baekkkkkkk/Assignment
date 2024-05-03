def fibonacci_recursive(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fibonacci_recursive(n-1, memo) + fibonacci_recursive(n-2, memo)
    return memo[n]

def fibonacci_dp(n):
    if n <= 2:
        return 1
    a, b = 1, 1
    for i in range(3, n+1):
        a, b = b, a + b
    return b

import time
import matplotlib.pyplot as plt

times_recursive = []
times_dp = []

max_n = 100

for n in range(1, max_n + 1):
    start_time = time.time()
    fibonacci_recursive(n)
    times_recursive.append(time.time() - start_time)
    
    start_time = time.time()
    fibonacci_dp(n)
    times_dp.append(time.time() - start_time)

# 绘制结果
plt.figure(figsize=(12, 6))
plt.plot(range(1, max_n + 1), times_recursive, label='带备忘录的自顶向下递归')
plt.plot(range(1, max_n + 1), times_dp, label='自底向上动态规划')
plt.xlabel('第 N 个 Fibonacci 数')
plt.ylabel('执行时间（秒）')
plt.title('计算 Fibonacci 数的执行时间比较')
plt.legend()
plt.show()

def count_fib_calls(n, target, memo, count):
    if n in memo:
        return memo[n]
    if n == target:
        count[target] += 1
    if n <= 2:
        return 1
    memo[n] = count_fib_calls(n-1, target, memo, count) + count_fib_calls(n-2, target, memo, count)
    return memo[n]

target = 4
count = {target: 0}
memo = {}
counts = []

for i in range(5, 51):
    count[target] = 0
    count_fib_calls(i, target, memo, count)
    counts.append(count[target])

# 结果
plt.figure(figsize=(12, 6))
plt.plot(range(5, 51), counts, label=f'計算 F({target}) 的次數')
plt.xlabel('第 N 个 Fibonacci 數')
plt.ylabel(f'計算 F({target}) 的次數')
plt.title(f'在更大的 Fibonacci 数中 F({target}) 的計算頻率')
plt.legend()
plt.show()
