from scripts.Wrapper import avg_10times

@avg_10times
def search(data_list, data_item):
    for n in data_list:
        if n == data_item:
            return
    print("The element cannot be found.")
    return 0