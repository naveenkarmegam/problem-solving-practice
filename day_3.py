
# Day - 3

# 1. Warm-up — Check Palindrome

def check_palindrome(str):
    for i in range(len(str)//2):
        if str[i] != str[(len(str) - 1) - i]:
            return False
    
    return True
    
# def check_palindrome(s):
#     return s == s[::-1]

# print(check_palindrome("hello"))


print(check_palindrome("racecar"))



# 2. Core — Valid Anagram

def check_two_string_anagram(s1,s2):
    
    if(len(s1) != len(s2)): return False
    
    s1_fre = {}
    s2_fre = {}
    
    for i in s1:
        
        if i in s1_fre:
            s1_fre[i] += 1
        else:
            s1_fre[i] = 1
    for i in s2:    
        if i in s2_fre:
            s2_fre[i] += 1
        else:
            s2_fre[i] = 1
    return s1_fre == s2_fre
    
print(check_two_string_anagram(s1 = "listen", s2 = "silent"))
print(check_two_string_anagram(s1 = "hello", s2 = "world"))
print(check_two_string_anagram(s1 = "aab", s2 = "bba"))


# 3. Stretch — Remove Duplicates from Sorted Array

def remove_duplicates(arr):
    unique_arr = []
    unique_arr.append(arr[0])
    
    for i in range(1,len(arr)):
        if arr[i] != arr[i-1]:
            unique_arr.append(arr[i])
            
    return unique_arr

print(remove_duplicates([1, 1, 2, 3, 3, 3, 5]))
print(remove_duplicates([]))
