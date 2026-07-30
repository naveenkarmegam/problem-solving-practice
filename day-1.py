# 1. Warm-up — Find the Max

def find_max(arr):
    max_num = arr[0]

    for e in arr:
        if e > max_num:
            max_num = e
    return max_num
    
print(find_max([3, 7, 2, 9, 4]))

# 2. Core — Find the Duplicate

def find_duplicate(arr):
    my_set = set()
    
    for e in arr:
        if e in my_set:
            return True
        else:
            my_set.add(e)
    return False
    

print(find_duplicate([1, 2, 3, 4, 2]))
print(find_duplicate([1, 2, 3, 4, 5]))


# 3. Stretch — Two Sum

nums = [2, 11, 15, 7]
target = 9

def find_two_sum(arr,target):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if target == arr[i] + arr[j] and i != j:
                return [i,j]
                
def find_two_sum_v2(arr,target):
    # pass
    
    my_dict = {}
    
    for i in range(len(arr)):
        val = target - arr[i]
        if val not in my_dict:
            my_dict[arr[i]] = i
        else:
            return [my_dict[val],i]
        


print(find_two_sum_v2(nums,target))
