def merge_the_tools(string, k):
    string_list = list(string)
    if len(string)%k == 0:
        for i in range(int(len(string)/k)):
            new_string_list = []
            for j in range(k):
                popped_item = string_list.pop(0)
                new_string_list.append(popped_item)
            
            unique_list = []
            for item in new_string_list:
                if item not in unique_list:
                    unique_list.append(item)
            print("".join(unique_list))

merge_the_tools("AABCAAADA", 3)