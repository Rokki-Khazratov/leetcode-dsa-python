import timeit



def logarithmic(n) :
    start = timeit.default_timer()
    k = 0
    while n > 0:
        n = n // 2
        k += 1
    run_time = (timeit.default_timer() - start) * 1000
    print ("logarithmic: ({}) Time: {:.6f) ms".format(k, run_time))
    return k

def linear(n):
    start = timeit.default_timer()
    k = 0
    for _ in range(n):
        k += 1
    run_time = (timeit.default_timer() - start) * 1000
    print("linear: ({}) Time: {:.6f} ms".format(k, run_time))