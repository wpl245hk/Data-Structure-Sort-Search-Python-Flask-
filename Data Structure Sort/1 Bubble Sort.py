from scripts.Wrapper import avg_10times

# for each iteration, swap largest element to last comparation position
@avg_10times
def bubble_sort(data_list):
    data_list_end = len(data_list)

    # last iteration compare position 0 with position 0, hence no need
    for iteration in range(data_list_end-1):

        # last comparation position decreae by 1
        for curr in range(data_list_end - iteration -1) :
            if data_list[curr] > data_list[curr+1]:
                data_list[curr+1], data_list[curr] = data_list[curr], data_list[curr+1]
    
    return data_list

# test case
# data_list = [-2, 45, 0, 11, 64, 34, 25, 12, 22, 11, 90,-9]
# print(bubble_sort(data_list))
