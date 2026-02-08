import time

start_time = time.time()

my_list = list(range(100_000_000))
print(my_list[1_000_000])

end_time = time.time()

print('Time spent:', round(end_time - start_time, 2))