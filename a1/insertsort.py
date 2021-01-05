import time

#insert sort taken from: https://www.geeksforgeeks.org/python-program-for-insertion-sort/
def insertionSort(arr): 
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
        key = arr[i] 
        j = i-1
        while j >= 0 and key < arr[j]: 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key

fo = open("data.txt", "r")
lines = fo.readlines()
for line in lines:
    num_nums = int(line[0])
    int_arr = []
    i = 1
    for i in range(1, num_nums):
        if line[i].isdigit() == True:
            int_arr.append(i)
    insertionSort(int_arr)
    print(int_arr)    
    
# Currently, all numbers are not being read. The first numbers are correct,
# but it does not grab all of them. Get all of the numbers into the arrays first