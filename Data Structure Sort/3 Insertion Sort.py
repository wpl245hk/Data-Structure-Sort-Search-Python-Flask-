from scripts.Wrapper import avg_10times

# for each iteration, compare selected element to position 0
@avg_10times
def insertion_sort(data_list):
    data_list_end = len(data_list)

    # first iteration compare position 0 with position 0, hence no need
    for index in range(1,data_list_end):
        curr = index
        while curr > 0 :
            if data_list[curr] < data_list[curr-1] :
                data_list[curr], data_list[curr-1] = data_list[curr-1], data_list[curr]
                curr -= 1
            # stop swapping if encounter <= element
            else:
                break
    
    return data_list

# test case
#data_list = [-2, 45, 0, 11, 64, 34, 25, 12, 22, 11, 90,-9]
#print(insertion_sort(data_list))
