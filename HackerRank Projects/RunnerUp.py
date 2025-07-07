if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split(" "))
    max_value = -1000000
    arr_list = list(arr)
    for item in arr_list:
        if item > max_value:
            max_value = item
    
    new_arr_list = [item for item in arr_list if item != max_value]
    print(new_arr_list)

    for item in new_arr_list:
        if item > max_value:
            max_value = item
    
    print(max_value)