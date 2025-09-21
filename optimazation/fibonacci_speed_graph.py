from time import perf_counter_ns
import json
import functools
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
plt.subplots_adjust(left=0.2, bottom=0.1)
print()

save_and_load = False

def fib_mem(n, computed = {0: 0, 1: 1}):
    print(computed)
    if n not in computed:
        computed[n] = fib_mem(n-1, computed) + fib_mem(n-2, computed)
    return computed[n]
    

def fib_lis(n):
    lis = [0,1]
    for i in range(n):
        lis.append(lis[-1] + lis[-2])
    return lis

def time_fib():
    start = perf_counter_ns()
    fib_mem(500)
    end = perf_counter_ns()
    elapsed = end - start
    return elapsed / 1000

number = 10000
times = []
for i in range(number):
    times.append(time_fib())

print(f"num of loops: {number}  average time: {sum(times) / len(times)} μs")

if (save_and_load):
    with open("list_times.json", mode="r+") as f:
        old = []
        try:
            for line in f:
                old.exltend(json.loads(line))
        except json.decoder.JSONDecodeError:
            old = []
        json.dump(times,f)
        f.write('\n')
        times.extend(old)
    

plt.hist(times, bins=100, range=(min(times)-2,125), log=0)

plt.xticks(rotation=-45)
plt.xlabel('time')
plt.ylabel('how often')
plt.tight_layout()
plt.show()

# let's see how fast we can get this and plot and see what the different bell curves look like