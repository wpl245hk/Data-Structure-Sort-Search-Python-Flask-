import timeit

def search(data_list, data_item):
    starttime = timeit.default_timer()
    for n in data_list:
        if n == data_item:
            return timeit.default_timer() - starttime
    print("The element cannot be found.")
    return 0