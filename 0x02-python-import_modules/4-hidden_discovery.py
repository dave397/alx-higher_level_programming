#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4


    arr_list = dir(hidden_4)
    i = 0
    while (i < arr_list):
        if arr_list[i][:2] != "__":
            print(arr_list[i])
